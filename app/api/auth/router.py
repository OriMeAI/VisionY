from fastapi import APIRouter

# 创建主路由
auth_router = APIRouter(prefix='/auth',tags=['auth'])

# 导入子路由
from .google.router import google_router
from .email.router import email_router
from .logout.router import logout_router

# 注册子路由
auth_router.include_router(google_router)
auth_router.include_router(email_router)
auth_router.include_router(logout_router)