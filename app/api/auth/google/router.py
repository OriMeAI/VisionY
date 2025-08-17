from fastapi import APIRouter

# 创建主路由
google_router = APIRouter(prefix='/google',tags=['google'])

# 导入子路由
#google 服务器回调
from .callback.router import callback_router
#前端登录验证
from .login.router import login_router

# 注册子路由
google_router.include_router(callback_router)
google_router.include_router(login_router)