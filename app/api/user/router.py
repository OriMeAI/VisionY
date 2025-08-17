from fastapi import APIRouter, Request, HTTPException, Depends
from fastapi.responses import JSONResponse
from app.utils.core import get_user_id

user_router = APIRouter(
    prefix='/user',
    tags=['user']
)

async def verify_user():
    user_id = get_user_id()
    if not user_id:
        # 当 user_id 不存在时，抛出 HTTPException 异常
        # 这会阻止后续的路由函数执行，并返回 401 状态码和指定的 detail 信息
        raise HTTPException(
            status_code=401, # 或者使用 800，但 401 更符合 HTTP 语义
            detail={"code": 800, "msg": "need to login"} # detail 可以是字符串或字典/JSON
        )
    # 如果验证通过，可以返回 user_id，供后续路由函数使用
    return user_id

# 移除中间件方式
# user_router.middleware("http")(verify_user)

# 导入子路由
from .info.router import info_router
user_router.include_router(info_router, dependencies=[Depends(verify_user)])

from .update.router import update_router
user_router.include_router(update_router, dependencies=[Depends(verify_user)])