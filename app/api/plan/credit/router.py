from fastapi import APIRouter

# 创建路由器
credit_router = APIRouter(prefix='/credit')

# 导入子路由
from .list.router import list_router
credit_router.include_router(list_router)

from.purchase.router import purchase_router
credit_router.include_router(purchase_router)