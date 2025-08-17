from fastapi import APIRouter,HTTPException,Depends
from app.utils.core import get_user_id

stripe_router = APIRouter(
    prefix='/stripe',
    tags=['stripe']
)

async def verify_user():
    user_id = get_user_id()
    if not user_id:
        # 当 user_id 不存在时，抛出 HTTPException 异常
        # 这会阻止后续的路由函数执行，并返回 401 状态码和指定的 detail 信息
        raise HTTPException(
            status_code=401, # 或者使用 800，但 401 更符合 HTTP 语义
            detail={"code": 800, "msg": "need to login"} # detail 可以是字符串或字典/JSON
        )
    # 如果验证通过，可以返回 user_id，供后续路由函数使用
    return user_id

from .cancel_payment.router import cancel_payment_router
stripe_router.include_router(cancel_payment_router, dependencies=[Depends(verify_user)])

from .capture_payment.router import capture_payment_router
stripe_router.include_router(capture_payment_router, dependencies=[Depends(verify_user)])

from .create_payment.router import create_payment_router
stripe_router.include_router(create_payment_router, dependencies=[Depends(verify_user)])

from .create_subscription.router import create_subscription_router
stripe_router.include_router(create_subscription_router, dependencies=[Depends(verify_user)])

from .verify_subscription.router import verify_subscription_router
stripe_router.include_router(verify_subscription_router, dependencies=[Depends(verify_user)])

from .cancel_subscription.router import cancel_subscription_router
stripe_router.include_router(cancel_subscription_router, dependencies=[Depends(verify_user)])

from .webhook.router import webhook_router
stripe_router.include_router(webhook_router)