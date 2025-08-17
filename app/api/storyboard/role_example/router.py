from fastapi import APIRouter

role_example_router = APIRouter(
    prefix='/role_example',
    tags=['storyboard-role-example']
)

from .delete.router import delete_router
role_example_router.include_router(delete_router)