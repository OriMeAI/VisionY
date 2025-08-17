from fastapi import APIRouter

role_router = APIRouter(
    prefix='/role',
    tags=['storyboard-role']
)

from .add.router import add_router
role_router.include_router(add_router)

from .copy.router import copy_router
role_router.include_router(copy_router)

from .recent.router import recent_router
role_router.include_router(recent_router)

from .delete.router import delete_router
role_router.include_router(delete_router)

from .history.router import history_router
role_router.include_router(history_router)

from .list.router import list_router
role_router.include_router(list_router)

from .regenerate.router import regenerate_router
role_router.include_router(regenerate_router)

from .rename.router import rename_router
role_router.include_router(rename_router)

from .update_default.router import update_default_router
role_router.include_router(update_default_router)

from .upload_example_figure.router import upload_example_figure_router
role_router.include_router(upload_example_figure_router)