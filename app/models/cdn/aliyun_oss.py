import os
import time
import random
import string
from urllib.parse import urlparse
import base64
import io
import asyncio
import aiohttp
from typing import Dict, Any
import logging

import oss2

class AliyunOss:
    """
    阿里云OSS客户端,用于上传图片到OSS
    https://github.com/aliyun/aliyun-oss-python-sdk
    """
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def __init__(self):
        """
        初始化阿里云OSS客户端
        """        
        self.access_key = os.environ.get("ALIYUN_ACCESS_KEY", "")
        self.secret_key = os.environ.get("ALIYUN_SECRET_KEY", "")
        self.bucket_name = os.environ.get("ALIYUN_OSS_BUCKET_NAME", "")
        self.endpoint = os.environ.get("ALIYUN_OSS_ENDPOINT", "")
        self.resource_base_url = "https://resource.visiony.cc"
        
        # logging.info(f"初始化腾讯云COS客户端，secret_id: {self.secret_id}, secret_key: {self.secret_key}, bucket_name: {self.bucket_name}, region: {self.region}")
        
        auth = oss2.Auth(self.access_key, self.secret_key)
        self.bucket = oss2.Bucket(auth, self.endpoint, self.bucket_name)
        
        #重试次数
        self.max_retries = 3
                        
    def generate_unique_key(self, extension):
        timestamp = int(time.time() * 1000)  # Convert to milliseconds
        random_string = ''.join(random.choices(string.ascii_lowercase + string.digits, k=6))
        
        return f"image/{timestamp}-{random_string}{extension}"
        
    async def upload_from_url(self, source_url: str) -> Dict[str, Any]:
        """
        从URL上传图片到OSS
        
        Args:
            source_url: 图片URL
        """   
        
        for attempt in range(self.max_retries):     
            try:
                # 3. 获取图片二进制流（避免本地保存）
                async with aiohttp.ClientSession() as session:
                    async with session.get(source_url) as response:
                        if response.status != 200:
                            logging.error(f"Download image failed, HTTP status code: {response.status}")
                            continue
                        
                        # 读取响应内容
                        content = await response.read()
                        
                # 4. 将图片流上传至COS
                file_stream = io.BytesIO(content)  # 转换为内存中的二进制流
                    
                object_key = self.generate_unique_key(".png")
                
                # 使用 asyncio.to_thread 在线程池中执行同步操作
                await asyncio.to_thread(
                    self.bucket.put_object,
                    key=object_key,
                    data=file_stream,
                )
                
                return {
                    "status": "success",
                    "message": "Image uploaded successfully",
                    "resource_url": f"{self.resource_base_url}/{object_key}"
                }
                            
            except Exception as e:
                # 其他未预期的错误
                error_message = f"upload url image to oss failed: {str(e)}"
                logging.error(error_message)
                
            if attempt == self.max_retries - 1:  # 最后一次重试
                error_msg = f"upload url image to oss failed after {self.max_retries} attempts"
                return {
                    "status": "error",
                    "message": error_msg
                }
            else:
                logging.warning(f"upload url image to oss attempt {attempt + 1}, retrying...")
                await asyncio.sleep(2 ** attempt)  # 指数退避
                
        
    async def upload_base64(self, base64_data: str, filename: str) -> Dict[str, Any]:
        """
        从Base64字符串上传图片到OSS
        
        Args:
            base64_data: Base64字符串
        """
        for attempt in range(self.max_retries):    
            try:
                # 处理base64数据
                # 检查是否包含data URI scheme (如 "data:image/png;base64,")
                if ";" in base64_data and "," in base64_data:
                    # 提取实际的base64数据
                    encoded = base64_data.split(",", 1)[1]
                else:
                    encoded = base64_data
                    
                file_bytes = base64.b64decode(encoded)
                file_stream = io.BytesIO(file_bytes)
                                        
                object_key = self.generate_unique_key(f"_{filename}")
                
                # response = self.cos_client.put_object(
                #     Bucket=self.bucket_name,
                #     Key=object_key,
                #     Body=file_stream,
                # )
                
                # 使用 asyncio.to_thread 在线程池中执行同步操作
                await asyncio.to_thread(
                    self.bucket.put_object,
                    key=object_key,
                    data=file_stream
                )
                
                return {
                    "status": "success",
                    "message": "Image uploaded successfully",
                    "resource_url": f"{self.resource_base_url}/{object_key}"
                }
                            
            except Exception as e:
                # 其他未预期的错误
                error_message = f"upload base64 image to oss failed: {str(e)}"
                logging.error(error_message)
                
            if attempt == self.max_retries - 1:  # 最后一次重试
                error_msg = f"upload base64 image to oss failed after {self.max_retries} attempts"
                return {
                    "status": "error",
                    "message": error_msg
                }
            else:
                logging.warning(f"upload base64 image to oss attempt {attempt + 1}, retrying...")
                await asyncio.sleep(2 ** attempt)  # 指数退避
            
aliyun_oss_instance = AliyunOss()
