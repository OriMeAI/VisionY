from fastapi import APIRouter

order_router = APIRouter(
    prefix='/order',
    tags=['order']
)

from .create.router import create_router
order_router.include_router(create_router)

from .create_pre_pay.router import create_pre_pay_router
order_router.include_router(create_pre_pay_router)

from .trade.router import trade_router
order_router.include_router(trade_router)