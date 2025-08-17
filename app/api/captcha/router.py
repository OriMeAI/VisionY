from fastapi import APIRouter

# 创建路由器
captcha_router = APIRouter(
    prefix='/captcha',
    tags=['captcha']
)

# 导入子路由
from .verify.router import verify_router

# 注册子路由
captcha_router.include_router(verify_router)