from fastapi import APIRouter

# 创建路由器
index_router = APIRouter(
    prefix='/index',
    tags=['index']
)

# 导入子路由
from .statistics.router import statistics_router

# 注册子路由
index_router.include_router(statistics_router)