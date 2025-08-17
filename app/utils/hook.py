from fastapi import FastAPI, Request, HTTPException
from starlette.middleware.base import BaseHTTPMiddleware
import time
from .mongo import mongo_instance
from app.collections.user import update_user_benefits
from .core import request_context
class HookMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        # 设置请求上下文
        context_marker = request_context.set(request) # type: ignore
        
        try:
            # 从请求头或查询参数中获取语言设置
            language = request.headers.get('Accept-Language') or request.query_params.get('lang', 'en-US')
            
            # 简单的语言代码处理
            if language.startswith('en'):
                request.state.language = 'en'
            elif language.startswith('zh-TW') or language.startswith('zh-HK'):
                request.state.language = 'tw'
            elif language.startswith('ja'):
                request.state.language = 'ja'
            else:
                request.state.language = 'cn'
                
            # 初始化用户信息
            request.state.user_id = None
            
            # 从Nginx传递的真实IP
            request.state.user_ip = request.headers.get('X-Real-IP', None)  
            
            # 检查请求头中是否包含Authorization
            auth_header = request.headers.get('Authorization')
            if auth_header and auth_header.startswith('Bearer '):
                token = auth_header.split(' ')[1]
                
                if len(token) > 0:
                    # 查询token是否有效
                    current_time = int(time.time())
                    account = await mongo_instance.find_one(
                        "accounts", 
                        {
                            "token": token,
                            #todo 是否启用token过期时间
                            # "token_expires_at": {"$gt": current_time}
                        }
                    )
                    
                    if account:
                        # 设置用户认证信息
                        request.state.user_id = account.get('user_id')
                        
                        #统一查询用户信息是否存在
                        user = await mongo_instance.find_one("users", {"_id": request.state.user_id})
                        if not user:
                            raise HTTPException(status_code=401, detail=f"User {request.state.user_id} does not exist")
                        else:
                            await update_user_benefits(request.state.user_id)

            response =  await call_next(request)
            return response
        
        finally:
            # 清理请求上下文
            request_context.reset(context_marker)
         
def register_hook_handlers(fast_app: FastAPI):
    fast_app.add_middleware(HookMiddleware)