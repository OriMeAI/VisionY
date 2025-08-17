import os
from contextvars import ContextVar
from typing import Optional

# 创建上下文变量
request_context = ContextVar('request_context', default=None)

#全局获取语言入口
def get_language():
    """获取当前请求的语言设置"""
    request = request_context.get()
    return request.state.language if request else 'en'

#全局获取用户id入口
def get_user_id():
    """获取当前请求的用户id"""
    request = request_context.get()
    return request.state.user_id if request else None

#获取用户IP地址
def get_user_ip():
    """获取当前请求的用户IP"""
    request = request_context.get()
    return request.state.user_ip if request else None

#将数据编码为SSE格式
def encode_sse_data(data, event: Optional[str] = None) -> bytes:
    """
    编码SSE数据，支持字符串和其他数据类型，并可指定事件类型
    
    Args:
        data: 可以是字符串或其他可JSON序列化的数据类型
        event: 事件类型，如果提供则会添加event字段, 如果未提供则添加 message事件
        
        - `event: message` 代表正常数据
        - `event: error` 代表错误
        - `event: process` 代表正在处理
        - `event: complete` 代表任务完成
        - `event: warning` 代表警告信息
        - 需要对生成函数整体做异常处理，出现问题直接发送event:error 事件
        
    Returns:
        bytes: 编码后的SSE数据
    """
    if isinstance(data, str):
        json_data = data
    else:
        try:
            import json
            json_data = json.dumps(data)
        except:
            json_data = str(data)
    
    result = ""
    if event:
        result += f"event: {event}\n"
    else:
        result += "event: message\n"
    result += f"data: {json_data}\n\n"
    
    return result.encode('utf-8')

def is_running_in_docker():
    return os.getenv("RUNNING_IN_DOCKER") == "true"

