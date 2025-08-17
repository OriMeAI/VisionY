from fastapi import APIRouter
from fastapi.responses import JSONResponse
from app.utils.mongo import mongo_instance
from app.utils.core import get_user_id
from app.locales.translations import get_translation

logout_router = APIRouter()

@logout_router.get('/logout')
async def operator():
    user_id = get_user_id()
    if user_id is not None:
        # 查找用户对应的账号
        account = await mongo_instance.find_one("accounts", {"user_id": user_id})
        
        if account:
            # 重置token相关信息
            await mongo_instance.update_one(
                "accounts",
                {"user_id": user_id},
                {"$set": {
                    "token": "",
                    "token_created_at": 0,
                    "token_expires_at": 0
                }}
            )
            
    return JSONResponse(content={
        "code": 0,
        "data": {},
        "msg": get_translation("logout_success")
    })