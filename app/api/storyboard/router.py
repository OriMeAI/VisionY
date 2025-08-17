from fastapi import APIRouter, Depends,HTTPException
from app.utils.core import get_user_id

storyboard_router = APIRouter(
    prefix='/storyboard',
    tags=['storyboard']
)

async def verify_user():
    user_id = get_user_id()
    if not user_id:
        # 当 user_id 不存在时，抛出 HTTPException 异常
        # 这会阻止后续的路由函数执行，并返回 401 状态码和指定的 detail 信息
        raise HTTPException(
            status_code=401, # 或者使用 800，但 401 更符合 HTTP 语义
            detail={"code": 800, "data": {}, "msg": "need to login"} # detail 可以是字符串或字典/JSON
        )
    # 如果验证通过，可以返回 user_id，供后续路由函数使用
    return user_id

from .create.router import create_router
storyboard_router.include_router(create_router, dependencies=[Depends(verify_user)])

from .export.router import export_router
storyboard_router.include_router(export_router, dependencies=[Depends(verify_user)])

from .fetch_img.router import fetch_img_router
storyboard_router.include_router(fetch_img_router, dependencies=[Depends(verify_user)])

from .project.router import project_router
storyboard_router.include_router(project_router, dependencies=[Depends(verify_user)])

from .role.router import role_router
storyboard_router.include_router(role_router, dependencies=[Depends(verify_user)])

from .role_example.router import role_example_router
storyboard_router.include_router(role_example_router, dependencies=[Depends(verify_user)])

from .script_to_shot.router import script_to_shot_router
storyboard_router.include_router(script_to_shot_router, dependencies=[Depends(verify_user)])

from .shot.router import shot_router
storyboard_router.include_router(shot_router, dependencies=[Depends(verify_user)])

from .status.router import status_router
storyboard_router.include_router(status_router, dependencies=[Depends(verify_user)])

from .swap.router import swap_router
storyboard_router.include_router(swap_router, dependencies=[Depends(verify_user)])