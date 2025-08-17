from fastapi import APIRouter

# 创建主路由
email_router = APIRouter(prefix='/email',tags=['email'])

# 导入子路由
from .login.router import login_router
from .send_code.router import send_code_router

# 注册子路由
email_router.include_router(login_router)
email_router.include_router(send_code_router)