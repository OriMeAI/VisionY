import os
import json
import logging
import aiohttp
from typing import Dict, Any
from urllib.parse import urljoin
from .helper import generate_random_string

if __name__ == "__main__":
    # 设置环境变量
    import sys
    import os
    
    # 将项目根目录添加到Python路径
    sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
    from init_env import initialize_environment_variables
    initialize_environment_variables()

class Cloudflare:
    """
    Cloudflare Worker 资源管理工具类
    用于调用 Cloudflare Worker 提供的资源管理接口
    
    curl -X POST https://api-visual-story.unit-cdn.net/upload-from-url \
    -H "X-API-Key: api_key" \
    -H "Content-Type: application/json" \
    -d '{"url": "https://liblibai-online.liblib.cloud/train-img/b452266e79c349a3a3ee94b5f5f9d8e1/532132cf-a1ed-4bac-94ad-77a8a780e295.png"}'
    
    """
    
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def __init__(self):
        """
        初始化 Cloudflare 资源管理工具
        
        Args:
            api_key: API 密钥，如果不提供则从环境变量获取
            base_url: Worker 基础 URL，如果不提供则使用默认值
        """
        self.api_key = os.environ.get("CLOUDFLARE_VISUAL_STORY_RESOURCE_API_KEY", "")
        self.base_url = "https://api-visual-story.unit-cdn.net/"
        self.headers = {"X-API-Key": self.api_key}
        
    async def upload_file(self, resource_path: str) -> Dict[str, Any]:
        """
        上传文件到 Cloudflare Worker
        
        Args:
            resource_path: 本地文件路径或网络URL
            
        Returns:
            Dict: 上传结果
        """
        url = urljoin(self.base_url, "upload")
        
        try:
            # 判断是否为网络URL
            if resource_path.startswith(('http://', 'https://')):
                # 从网络URL下载文件
                async with aiohttp.ClientSession() as session:
                    async with session.get(resource_path) as file_response:
                        if file_response.status != 200:
                            return {
                                "status": "error",
                                "message": f"下载文件失败: HTTP {file_response.status}",
                                "code": file_response.status
                            }
                        
                        file_content = await file_response.read()
                        
                        # 从URL中提取文件名
                        from urllib.parse import urlparse
                        parsed_url = urlparse(resource_path)
                        filename = os.path.basename(parsed_url.path)
                        
                        # 如果URL没有文件名，生成随机文件名
                        if not filename or '.' not in filename:
                            # 尝试从Content-Type获取扩展名
                            content_type = file_response.headers.get('Content-Type', '')
                            ext_map = {
                                'image/jpeg': '.jpg',
                                'image/png': '.png',
                                'image/gif': '.gif',
                                'image/webp': '.webp',
                                'image/svg+xml': '.svg',
                                'video/mp4': '.mp4',
                                'video/webm': '.webm',
                                'audio/mpeg': '.mp3',
                                'audio/ogg': '.ogg',
                                'application/pdf': '.pdf'
                            }
                            ext = ext_map.get(content_type, '')
                            filename = f"{generate_random_string()}{ext}"
                        
                        # 从Content-Type获取内容类型
                        content_type = file_response.headers.get('Content-Type', 'application/octet-stream')
            else:
                # 处理本地文件
                if not os.path.isfile(resource_path):
                    return {
                        "status": "error",
                        "message": f"文件不存在: {resource_path}",
                        "code": 404
                    }
                
                # 读取文件内容
                with open(resource_path, 'rb') as f:
                    file_content = f.read()
                
                # 获取文件名和扩展名
                filename = os.path.basename(resource_path)
                ext = os.path.splitext(filename)[1].lower()
                
                # 根据扩展名判断内容类型
                content_type_map = {
                    '.jpg':'image/jpeg',
                    '.png':'image/png',
                    '.gif': 'image/gif',
                    '.webp': 'image/webp',
                    '.svg': 'image/svg+xml',
                    '.mp4':'video/mp4',
                    '.webm':'video/webm',
                    '.mp3':'audio/mpeg',
                    '.ogg':'audio/ogg',
                    '.pdf':'application/pdf'
                }
                content_type = content_type_map.get(ext, 'application/octet-stream')
            
            # 准备请求头
            headers = self.headers.copy()
            headers["Content-Type"] = content_type
            headers["X-Filename"] = filename
            
            # 发送请求
            async with aiohttp.ClientSession() as session:
                async with session.post(url, headers=headers, data=file_content) as response:
                    if response.status != 200:
                        if response.status == 401:
                            return {
                                "status": "error",
                                "message": "未授权访问",
                                "code": 401
                            }
                        else:
                            return {
                                "status": "error",
                                "message": f"上传文件失败: HTTP {response.status}",
                                "code": response.status
                            }
                    
                    # 解析响应
                    result = await response.json()
                    return {
                        "status": "success",
                        "message": "文件上传成功",
                        "data": result
                    }
        except aiohttp.ClientError as e:
            logging.error(f"上传文件失败: {str(e)}")
            return {
                "status": "error",
                "message": f"上传文件失败: {str(e)}",
                "code": 500
            }
        except Exception as e:
            logging.error(f"上传文件异常: {str(e)}")
            return {
                "status": "error",
                "message": f"上传文件异常: {str(e)}",
                "code": 500
            }
  
    async def upload_base64(self, base64_data: str, filename: str) -> Dict[str, Any]:
        """
        上传base64编码的文件到 Cloudflare Worker
        
        Args:
            base64_data: base64编码的文件内容
            filename: 文件名
            
        Returns:
            Dict: 上传结果
        """
        url = urljoin(self.base_url, "upload")
        
        try:
            # 处理base64数据
            # 检查是否包含data URI scheme (如 "data:image/png;base64,")
            if ";" in base64_data and "," in base64_data:
                # 提取实际的base64数据
                base64_data = base64_data.split(",", 1)[1]
            
            # 解码base64数据
            try:
                import base64 as b64
                file_content = b64.b64decode(base64_data)
            except Exception as e:
                return {
                    "status": "error",
                    "message": f"无效的base64数据: {str(e)}",
                    "code": 400
                }
            
            # 获取文件扩展名
            ext = os.path.splitext(filename)[1].lower()
            
            # 根据扩展名判断内容类型
            content_type_map = {
                '.jpg': 'image/jpeg',
                '.jpeg': 'image/jpeg',
                '.png': 'image/png',
                '.gif': 'image/gif',
                '.webp': 'image/webp',
                '.svg': 'image/svg+xml',
                '.mp4': 'video/mp4',
                '.webm': 'video/webm',
                '.mp3': 'audio/mpeg',
                '.ogg': 'audio/ogg',
                '.pdf': 'application/pdf'
            }
            content_type = content_type_map.get(ext, 'application/octet-stream')
            
            # 准备请求头
            headers = self.headers.copy()
            headers["Content-Type"] = content_type
            headers["X-Filename"] = filename
            
            # 发送请求
            async with aiohttp.ClientSession() as session:
                async with session.post(url, headers=headers, data=file_content) as response:
                    if response.status != 200:
                        if response.status == 401:
                            return {
                                "status": "error",
                                "message": "未授权访问",
                                "code": 401
                            }
                        else:
                            return {
                                "status": "error",
                                "message": f"上传文件失败: HTTP {response.status}",
                                "code": response.status
                            }
                    
                    # 解析响应
                    result = await response.json()
                    return {
                        "status": "success",
                        "message": "文件上传成功",
                        "resource_url": result["url"]
                    }
        except aiohttp.ClientError as e:
            logging.error(f"上传base64文件失败: {str(e)}")
            return {
                "status": "error",
                "message": f"上传base64文件失败: {str(e)}",
                "code": 500
            }
        except Exception as e:
            logging.error(f"上传base64文件异常: {str(e)}")
            return {
                "status": "error",
                "message": f"上传base64文件异常: {str(e)}",
                "code": 500
            }
  
    async def upload_from_url(self, source_url: str) -> Dict[str, Any]:
        """
        从 URL 上传资源
        
        Args:
            source_url: 源资源 URL
            
        Returns:
            Dict: 上传结果
        """
        url = urljoin(self.base_url, "upload_from_url")
        
        try:
            # 准备请求数据
            data = {
                "url": source_url
            }
            
            # 准备请求头
            headers = self.headers.copy()
            headers["Content-Type"] = "application/json"
            
            # 使用aiohttp进行异步请求
            async with aiohttp.ClientSession() as session:
                async with session.post(url, headers=headers, json=data) as response:
                    if response.status != 200:
                        if response.status == 401:
                            return {
                                "status": "error",
                                "message": "未授权访问",
                                "code": 401
                            }
                        else:
                            logging.error(f"从 URL 上传资源失败: HTTP {response.status}")
                            return {
                                "status": "error",
                                "message": f"从 URL 上传资源失败: HTTP {response.status}",
                                "code": response.status
                            }
                    
                    # 解析响应
                    result = await response.json()
                    return {
                        "status": "success",
                        "message": "从 URL 上传资源成功",
                        "resource_url": result["url"]
                    }
        except aiohttp.ClientError as e:
            logging.error(f"从 URL 上传资源失败: {str(e)}")
            return {
                "status": "error",
                "message": f"从 URL 上传资源失败: {str(e)}",
                "code": 500
            }
        except Exception as e:
            logging.error(f"从 URL 上传资源异常: {str(e)}")
            return {
                "status": "error",
                "message": f"从 URL 上传资源异常: {str(e)}",
                "code": 500
            }
        
cloudflare_instance = Cloudflare()

if __name__ == "__main__":
    import asyncio
    import base64
    
    async def test():
        print(generate_random_string())
        # 测试上传
        result = await cloudflare_instance.upload_from_url("https://example.com/image.jpg")
        print(result)
        
    # 测试从本地文件读取并使用base64上传
    async def test_upload_base64():
        # 指定要读取的本地文件路径
        local_file_path = "/Users/songxiulei/Downloads/images/face1.jpg"
        
        # 读取文件并转换为base64
        with open(local_file_path, "rb") as file:
            file_content = file.read()
            base64_data = base64.b64encode(file_content).decode('utf-8')
        
        # 获取文件名
        filename = os.path.basename(local_file_path)
        
        # 调用upload_base64方法
        result = await cloudflare_instance.upload_base64(base64_data, filename)
        print("上传结果:", result)
    
    asyncio.run(test_upload_base64())