from fastapi import APIRouter

template_router = APIRouter(
    prefix='/template',
    tags=['project-template']
)



from .copy.router import copy_router
template_router.include_router(copy_router)

from .list.router import list_router
template_router.include_router(list_router)

from .role.router import role_router
template_router.include_router(role_router)

from .shot.router import shot_router
template_router.include_router(shot_router)

from .id.router import id_router
template_router.include_router(id_router)