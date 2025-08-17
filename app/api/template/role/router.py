from fastapi import APIRouter

role_router = APIRouter(
    prefix='/role',
    tags=['project-template-role']
)

from .id.router import id_router
role_router.include_router(id_router)