from fastapi import APIRouter

shot_router = APIRouter(
    prefix='/shot',
    tags=['storyboard-shot']
)

from .copy.router import copy_router
shot_router.include_router(copy_router)

from .delete.router import delete_router
shot_router.include_router(delete_router)

from .detail.router import detail_router
shot_router.include_router(detail_router)

from .hd_resolution.router import hd_resolution_router
shot_router.include_router(hd_resolution_router)

from .history.router import history_router
shot_router.include_router(history_router)

from .pic_upload.router import pic_upload_router
shot_router.include_router(pic_upload_router)

from .list.router import list_router
shot_router.include_router(list_router)

from .regenerate.router import regenerate_router
shot_router.include_router(regenerate_router)

from .repaint.router import repaint_router
shot_router.include_router(repaint_router)

from .sort.router import sort_router
shot_router.include_router(sort_router)

from .update.router import update_router
shot_router.include_router(update_router)

from .pic_apply.router import pic_apply_router
shot_router.include_router(pic_apply_router)