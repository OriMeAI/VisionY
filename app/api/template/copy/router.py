from fastapi import APIRouter

copy_router = APIRouter(
    prefix='/copy',
    tags=['project-template-copy']
)

from .id.router import id_router
copy_router.include_router(id_router)