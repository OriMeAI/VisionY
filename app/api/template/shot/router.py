from fastapi import APIRouter

shot_router = APIRouter(
    prefix='/shot',
    tags=['project-template-shot']
)

from .id.router import id_router
shot_router.include_router(id_router)