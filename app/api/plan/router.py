from fastapi import APIRouter

plan_router = APIRouter(
    prefix='/plan',
    tags=['plan']
)

from .benefit.router import benefit_router
plan_router.include_router(benefit_router)

from .credit.router import credit_router
plan_router.include_router(credit_router)

from .detail.router import detail_router
plan_router.include_router(detail_router)

from .list.router import list_router
plan_router.include_router(list_router)