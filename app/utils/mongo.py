import uuid,calendar,os,logging
from motor.motor_asyncio import AsyncIOMotorClient
from pymongo.results import UpdateResult, DeleteResult
from pymongo.errors import DuplicateKeyError
from typing import Optional, Dict, List, Union
from datetime import datetime,timezone,timedelta
from bson.objectid import ObjectId
from app.utils.core import is_running_in_docker

"""数据结构
见 helper下的文件
"""

#不需要处理异常，会在flask的error里统一处理
class MongoDB:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    

    def __init__(self):
        """
        初始化MongoDB连接
        
        Args:
            uri: MongoDB连接字符串，示例 mongodb://admin:admin@localhost:27017/
            database: 默认数据库名称
            max_pool_size: 最大连接池大小
        """
        mongo_user = os.environ.get("MONGO_USER", "") 
        mongo_password = os.environ.get("MONGO_PASSWORD", "")
        mongo_host = 'mongo' if is_running_in_docker() else os.environ.get("MONGO_HOST", "")
        mongo_port = os.environ.get("MONGO_PORT", "")
        mongo_database = os.environ.get("MONGO_DATABASE", "")
        
        uri =  f"mongodb://{mongo_user}:{mongo_password}@{mongo_host}:{mongo_port}/"

        self.client = AsyncIOMotorClient(uri, maxPoolSize=50)
        self.db = self.client[mongo_database]
        
        logging.info("MongoDB connection established successfully")
        
    def is_available(self) -> bool:
        try:
            # 简单检查客户端和数据库是否存在
            return self.client is not None and self.db is not None
        except:
            return False
            
    def generate_token(self):
        return uuid.uuid4().hex

    def generate_object_id(self, id_str:str="") -> ObjectId:
        """
        生成唯一的ObjectId, ObejctId是12字节的二进制数据，由时间戳、机器标识符和进程标识符组成
        是mongodb特有的，mongodb有很多优化
        如果 id_str 非空，则转换为 ObjectId
        object_id = str(ObjectId())转换为字符串
        字符串转换为ObjectId
        user_id = ObjectId("60d21b4667d0d31684b0fa4f")
        """
        try:
            if id_str:
                return ObjectId(id_str)
            else:
                return ObjectId()
        except Exception as e:
            return None
    
    def compare_time(self,current_time,database_time) -> bool:
        """
        比较两个时间戳，返回True表示current_time大于database_time
        """  
        # 给 MongoDB 返回的时间添加 UTC 时区信息
        if database_time and not database_time.tzinfo:
            database_time = database_time.replace(tzinfo=timezone.utc)
        
        # print(f"current_time: {current_time} database_time: {database_time}")
        
        return current_time >= database_time
    
    def get_current_time(self,delta=0) -> tuple:
        """
        获取当前时间，支持时间偏移，返回UTC时间、北京时间字符串和偏移后的UTC时间
        
        Args:
            delta: 时间偏移量，单位为秒，默认为0。正数表示未来时间，负数表示过去时间
            
        Returns:
            tuple: 包含三个元素:
                - datetime: UTC当前时间，带时区信息
                - str: 北京时间格式化字符串，格式为 "YYYY-MM-DD HH:MM:SS GMT+8"
                - datetime: 偏移后的UTC时间，带时区信息
        """
        utc_now = datetime.now(timezone.utc)
        # 计算偏移后的时间
        utc_delta = utc_now + timedelta(seconds=delta)
        # 转换为北京时间
        beijing_timezone = timezone(timedelta(hours=8))
        beijing_now = utc_now.astimezone(beijing_timezone)
        # 格式化时间为北京时间字符串
        beijing_formatted_time = beijing_now.strftime("%Y-%m-%d %H:%M:%S GMT+8")
        
        return utc_now, beijing_formatted_time, utc_delta
    
    def get_local_formatted_time(self,time: datetime = None) -> str:
        """
        将datetime对象转换为本地时间格式化字符串，格式为 "YYYY-MM-DD HH:MM:SS"
        """
        if not time:
            time = datetime.now()

        # 如果时间没有时区信息，添加 UTC 时区
        if not time.tzinfo:
            time = time.replace(tzinfo=timezone.utc)
            
        # 转换到本地时区
        local_time = time.astimezone()

        # 格式化时间时间字符串    
        formatted_time = local_time.strftime("%Y-%m-%d %H:%M:%S")

        return formatted_time
    
    def calculate_next_monthly_update_time(self, current_time: datetime) -> datetime:
        """
        为免费用户计算下次更新时间
        更新时间固定为下个月的第一天 00:00:00
        例如: 
        - 1月5日创建，下次更新时间为2月1日 00:00:00
        - 1月31日创建，下次更新时间为2月1日 00:00:00
        """
        # 计算下个月的年和月
        next_year = current_time.year
        next_month = current_time.month + 1
        
        if next_month > 12:
            next_month = 1
            next_year += 1
        
        # 创建下次更新时间，固定为下个月1号的00:00:00
        next_update_time = datetime(
            next_year,
            next_month,
            1,  # 固定为每月1号
            0,  # 小时设为0
            0,  # 分钟设为0
            0,  # 秒设为0
            tzinfo=current_time.tzinfo
        )
        
        return next_update_time
        
    def calculate_next_update_time(self,create_time: datetime, current_time: datetime) -> datetime:
        """
        基于创建时间计算下次更新时间
        保持与创建时间相同的时分秒
        例如: 
        - 1月31日 12:30:45创建，2月会在28日 12:30:45更新，3月会在31日 12:30:45更新
        """
        # 获取创建时间的具体时间部分
        create_day = create_time.day
        create_hour = create_time.hour
        create_minute = create_time.minute
        create_second = create_time.second  # 保持原始秒数
        
        # 计算下个月的年和月
        next_year = current_time.year
        next_month = current_time.month + 1
        
        if next_month > 12:
            next_month = 1
            next_year += 1
        
        # 获取下个月的最后一天
        _, last_day_of_next_month = calendar.monthrange(next_year, next_month)
        
        # 如果创建日期大于下个月的最后一天，使用下个月的最后一天
        # 否则使用创建时的日期
        next_day = min(create_day, last_day_of_next_month)
        
        # 创建下次更新时间，保持原始的时分秒
        next_update_time = datetime(
            next_year,
            next_month,
            next_day,
            create_hour,
            create_minute,
            create_second,
            tzinfo=current_time.tzinfo
        )
        
        return next_update_time
    
    def calculate_membership_expire_time(self,start_time: datetime,month_count: int) -> datetime:
        """
        基于创建时间和月数计算到期时间
        例如: 
        - 1月31日 12:30:45创建，1个月后到期时间为2月28日 12:30:44
        - 1月31日 12:30:45创建，3个月后到期时间为4月30日 12:30:44
        """
        # 计算到期时间
        # 获取当前年月日时分秒
        year = start_time.year
        month = start_time.month
        day = start_time.day
        hour = start_time.hour
        minute = start_time.minute
        second = start_time.second
        
        # 计算目标月份
        target_month = month + month_count
        target_year = year
        
        # 处理跨年情况
        while target_month > 12:
            target_month -= 12
            target_year += 1
        
        # 处理月末日期问题（如1月31日+1个月应该是2月28日或29日）
        import calendar
        max_day = calendar.monthrange(target_year, target_month)[1]
        target_day = min(day, max_day)
        
        # 创建目标日期时间
        expire_time = datetime(
            target_year, 
            target_month, 
            target_day, 
            hour, 
            minute, 
            second, 
            tzinfo=start_time.tzinfo
        )
        
        # expire_time = expire_time - timedelta(seconds=1)
        
        return expire_time

    async def count(self,
             collection_name: str,
             query: dict) -> int:
        """
        计算符合查询条件的文档数量
        
        Args:
            collection_name: 集合名称
            query: 查询条件
            
        Returns:
            int: 文档数量
        """
        return await self.db[collection_name].count_documents(query)
    
    async def insert_one(self,
                  collection_name: str,
                  document: dict) -> Optional[str]:
        """插入单个文档"""
        result = await self.db[collection_name].insert_one(document)
        return str(result.inserted_id)
        
    async def find_one(self,
                 collection_name: str,
                 query: dict) -> Optional[dict]:
        """查询单个文档"""
        return await self.db[collection_name].find_one(query)
    
    async def update_one(self,
                   collection_name: str,
                   query: dict,
                   update: dict,
                   upsert: bool = False) -> Optional[UpdateResult]:
        """
        更新单个文档

        Args:
            collection_name: 集合名称
            query: 查询条件
            update: 更新操作
            upsert: 如果不存在是否创建

        Returns:
            UpdateResult: 更新结果
        """
        result = await self.db[collection_name].update_one(
            query,
            update,
            upsert=upsert
        )
        return result
    
    async def delete_one(self,
                  collection_name: str,
                  query: dict) -> Optional[DeleteResult]:
        """
        删除单个文档
        
        Args:
            collection_name: 集合名称
            query: 查询条件
            
        Returns:
            DeleteResult: 删除结果
        """
        return await self.db[collection_name].delete_one(query)
            
    async def insert_many(self,
                   collection_name: str,
                   documents: List[dict],
                   ordered: bool = False) -> Optional[List[str]]:
        """
        批量插入多个文档
        
        Args:
            collection_name: 集合名称
            documents: 要插入的文档列表
            ordered: 是否按顺序插入，True表示按顺序插入，遇到错误会停止；False表示并行插入，遇到错误会继续
            
        Returns:
            List[str]: 插入成功的文档ID列表，如果插入失败返回None
        """
        result = await self.db[collection_name].insert_many(documents, ordered=ordered)
        return [str(id) for id in result.inserted_ids]
        
    async def find_many(self,
             collection_name: str,
             query: dict,
             projection: dict = None,
             skip: int = 0,
             limit: int = 0,
             sort: Optional[List[tuple]] = None) -> List[dict]:
        """
        查询多个文档，支持投影、分页和排序
        
        Args:
            collection_name: 集合名称
            query: 查询条件
            projection: 投影，指定返回的字段
            skip: 跳过的文档数量
            limit: 返回数量限制，0表示无限制
            sort: 排序条件，例如[("field", 1)]表示升序
            
        Returns:
            List[dict]: 查询结果列表
        """
        cursor = self.db[collection_name].find(query, projection)
        
        if sort:
            cursor = cursor.sort(sort)
        
        if skip > 0:
            cursor = cursor.skip(skip)
            
        if limit > 0:
            cursor = cursor.limit(limit)
                        
        return await cursor.to_list(length=None)
            
    async def update_many(self,
                   collection_name: str,
                   query: dict,
                   update: dict,
                   upsert: bool = False) -> Optional[UpdateResult]:
        """
        更新多个文档
        
        Args:
            collection_name: 集合名称
            query: 查询条件
            update: 更新操作
            upsert: 如果不存在是否创建
            
        Returns:
            UpdateResult: 更新结果
        """
        result = await self.db[collection_name].update_many(
            query,
            update,
            upsert=upsert
        )
        return result
    
    async def delete_many(self,
                   collection_name: str,
                   query: dict) -> Optional[DeleteResult]:
        """
        删除多个文档
        
        Args:
            collection_name: 集合名称
            query: 查询条件
            
        Returns:
            DeleteResult: 删除结果
        """
        return await self.db[collection_name].delete_many(query)

    async def increment_field(self,
                       collection_name: str,
                       query: dict,
                       field: str,
                       increment: int = 1,
                       upsert: bool = False,
                       many: bool = False) -> Union[Optional[dict], Optional[UpdateResult]]:
        """
        对文档字段进行自增操作，支持单文档或多文档
        
        Args:
            collection_name: 集合名称
            query: 查询条件
            field: 要自增的字段
            increment: 自增量
            upsert: 如果文档不存在是否创建
            many: 是否更新多个文档
            
        Returns:
            dict/UpdateResult: 单文档更新返回更新后的文档，多文档更新返回UpdateResult
        """
        if many:
            return await self.update_many(
                collection_name,
                query,
                {"$inc": {field: increment}},
                upsert
            )
        else:
            return await self.db[collection_name].find_one_and_update(
                query,
                {"$inc": {field: increment}},
                upsert=upsert,
                return_document=ReturnDocument.AFTER
            )
            
    async def aggregate(self,
                       collection_name: str,
                       pipeline: List[dict]) -> List[dict]:
        """
        执行聚合查询
        
        Args:
            collection_name: 集合名称
            pipeline: 聚合管道，包含聚合操作的列表
            
        Returns:
            List[dict]: 聚合查询结果列表
        """
        cursor = self.db[collection_name].aggregate(pipeline)
        return await cursor.to_list(length=None)

    async def close(self):
        """关闭连接"""
        await self.client.close()

mongo_instance = MongoDB()