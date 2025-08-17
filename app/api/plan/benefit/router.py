from fastapi import APIRouter

benefit_router = APIRouter(
    prefix='/benefit',
    tags=['plan-benefit']
)

from .list.router import list_router
benefit_router.include_router(list_router)