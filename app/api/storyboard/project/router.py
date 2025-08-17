from fastapi import APIRouter

project_router = APIRouter(
    prefix='/project',
    tags=['storyboard-project']
)

from .benefit.router import benefit_router
project_router.include_router(benefit_router)

from .copy.router import copy_router
project_router.include_router(copy_router)

from .delete.router import delete_router
project_router.include_router(delete_router)

from .info.router import info_router
project_router.include_router(info_router)

from .list.router import list_router
project_router.include_router(list_router)

from .rename.router import rename_router
project_router.include_router(rename_router)

from .style.router import style_router
project_router.include_router(style_router)

from .stories.router import stories_router
project_router.include_router(stories_router)
