from fastapi import APIRouter

file_router = APIRouter(
    prefix='/file',
    tags=['oss-file']
)

from .upload.router import upload_router
file_router.include_router(upload_router)