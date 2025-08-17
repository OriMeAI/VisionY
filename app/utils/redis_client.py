import redis
import os
import logging
import uuid
import time
import asyncio
from typing import Optional
from app.utils.core import is_running_in_docker

class RedisClient:
    _instance = None
    
    # 在类中定义 Lua 脚本
    ACQUIRE_SLOT_SCRIPT = """
    local redis_key = KEYS[1]
    local max_concurrent = tonumber(ARGV[1])
    local request_id = ARGV[2]
    local expire_time = tonumber(ARGV[3])
    local current_time = tonumber(ARGV[4])

    -- 清理过期请求
    redis.call('ZREMRANGEBYSCORE', redis_key, 0, current_time)

    -- 检查当前活跃请求数
    local active_count = redis.call('ZCARD', redis_key)

    if active_count < max_concurrent then
        -- 添加新请求
        redis.call('ZADD', redis_key, expire_time, request_id)
        return {1, active_count + 1}  -- 成功，返回新的活跃数量
    else
        return {0, active_count}      -- 失败，返回当前活跃数量
    end
    """
    
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def __init__(self):
        try:                
            self.client = redis.Redis(
                host='redis' if is_running_in_docker() else os.getenv("REDIS_HOST", "127.0.0.1"),
                port=int(os.getenv("REDIS_PORT", "6379")),
                db=int(os.getenv("REDIS_DB", "0")),
                password= os.getenv("REDIS_PASSWORD") or None,
                decode_responses=bool(os.getenv("REDIS_DECODE_RESPONSES", "True")),
                socket_connect_timeout=5,
                socket_timeout=5,
                retry_on_timeout=True
            )
            # 测试连接
            self.client.ping()
            logging.info("Redis connection established successfully")
        except Exception as e:
            logging.error(f"Failed to connect to Redis: {e}")
            # 如果 Redis 不可用，使用内存字典作为降级方案
            self.client = None
    
    def is_available(self) -> bool:
        try:
            return self.client is not None and self.client.ping()
        except:
            return False
    
    # 以下接口用于并发控制
    async def acquire_request_slot(self, redis_key: str, max_concurrent_requests: int, request_timeout: int = 300):
        request_id = str(uuid.uuid4())
        start_time = time.time()
        
        try:
            if self.client is None:
                logging.warning("Redis not available, using local fallback for concurrent control")
                return request_id
            
            while True:
                current_time = time.time()
                expire_time = current_time + request_timeout
                
                # 执行 Lua 脚本（原子操作）
                result = self.client.eval(
                    self.ACQUIRE_SLOT_SCRIPT,
                    1,  # 键的数量
                    redis_key,
                    max_concurrent_requests,
                    request_id,
                    expire_time,
                    current_time
                )
                
                success, active_count = result
                
                if success:
                    logging.info(f"Acquired request slot: {request_id}, active requests: {active_count}")
                    return request_id
                
                # 如果没有可用槽位，等待一段时间后重试
                await asyncio.sleep(0.1)
                
                # 防止无限等待
                if time.time() - start_time > request_timeout:
                    raise Exception("Request timeout waiting for slot")
                    
        except Exception as e:
            logging.warning(f"Redis concurrent control failed, using local fallback: {str(e)}")
            return request_id
    
    async def release_request_slot(self, redis_key: str, request_id: str):
        """
        释放请求槽位
        
        Args:
            redis_key: Redis键名
            request_id: 请求ID
        """
        try:
            if self.client is None:
                logging.warning(f"Redis not available, cannot release request slot {request_id}")
                return
                
            self.client.zrem(redis_key, request_id)
            
            active_count = self.client.zcard(redis_key)
            logging.info(f"Released request slot: {request_id}, active requests: {active_count}")
            
        except Exception as e:
            logging.warning(f"Failed to release request slot {request_id}: {str(e)}")
            
    async def _cleanup_expired_requests(self, redis_key: str, current_time: float):
        """
        清理过期的请求
        
        Args:
            redis_key: Redis键名
            current_time: 当前时间戳
        """
        try:
            # 移除所有过期的请求（分数小于当前时间的）
            removed_count = self.client.zremrangebyscore(redis_key, 0, current_time)
            if removed_count > 0:
                logging.info(f"Cleaned up {removed_count} expired requests")
        except Exception as e:
            logging.warning(f"Failed to cleanup expired requests: {str(e)}")

redis_instance = RedisClient()