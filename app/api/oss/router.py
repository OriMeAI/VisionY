from fastapi import APIRouter

oss_router = APIRouter(
    prefix='/oss',
    tags=['oss']
)

from .file.router import file_router
oss_router.include_router(file_router)