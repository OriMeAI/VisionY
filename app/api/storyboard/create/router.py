from fastapi import APIRouter

create_router = APIRouter(
    prefix='/create',
    tags=['storyboard-create']
)

from .project.router import project_router
create_router.include_router(project_router)

from .expand_write.router import expand_write_router
create_router.include_router(expand_write_router)

from .role.router import role_router
create_router.include_router(role_router)

from .shot.router import shot_router
create_router.include_router(shot_router)
