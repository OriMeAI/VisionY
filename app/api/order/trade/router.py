from fastapi import APIRouter

trade_router = APIRouter(
    prefix='/trade',
    tags=['order-trade']
)

from .ali.router import ali_router
trade_router.include_router(ali_router)