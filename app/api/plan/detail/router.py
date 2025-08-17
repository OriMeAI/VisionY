from fastapi import APIRouter

detail_router = APIRouter(
    prefix='/detail',
    tags=['plan-detail']
)

from .plan.router import plan_router
detail_router.include_router(plan_router)

from .credit.router import credit_router
detail_router.include_router(credit_router)