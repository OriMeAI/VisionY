from fastapi import APIRouter, Depends,HTTPException
from app.utils.core import get_user_id

transaction_router = APIRouter(
    prefix='/transaction',
    tags=['transaction']
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

from .credits_record.router import credits_record_router
transaction_router.include_router(credits_record_router, dependencies=[Depends(verify_user)])

from .obtained_record.router import obtained_record_router
transaction_router.include_router(obtained_record_router, dependencies=[Depends(verify_user)])

from .recharge_record.router import recharge_record_router
transaction_router.include_router(recharge_record_router, dependencies=[Depends(verify_user)])

from .usage_record.router import usage_record_router
transaction_router.include_router(usage_record_router, dependencies=[Depends(verify_user)])