from fastapi import APIRouter

# 创建主路由
api_router = APIRouter(prefix='/api')

@api_router.get("/health")
async def health_check():
    return {"status": "healthy"}

# 导入并包含所有子路由
from .auth.router import auth_router
from .captcha.router import captcha_router
from .index.router import index_router
from .order.router import order_router
from .oss.router import oss_router
from .plan.router import plan_router
from .template.router import template_router
from .storyboard.router import storyboard_router
from .transaction.router import transaction_router
from .user.router import user_router
from .stripe.router import stripe_router

# 注册所有子路由
api_router.include_router(auth_router)
api_router.include_router(captcha_router)
api_router.include_router(index_router)
api_router.include_router(order_router)
api_router.include_router(oss_router)
api_router.include_router(plan_router)
api_router.include_router(template_router)
api_router.include_router(storyboard_router)
api_router.include_router(transaction_router)
api_router.include_router(user_router)
api_router.include_router(stripe_router)