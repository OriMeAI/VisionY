from fastapi import APIRouter
from fastapi.responses import JSONResponse
from app.utils.mongo import mongo_instance
from pydantic import BaseModel, EmailStr
from app.locales.translations import get_translation
from app.utils.core import is_running_in_docker

from app.collections.user import create_user

# 请求模型
class EmailLoginRequest(BaseModel):
    email: EmailStr
    code: str

login_router = APIRouter()

@login_router.post('/login')
async def operator(request: EmailLoginRequest):
    if is_running_in_docker():
        # 验证码长度检查
        if len(request.code) != 6:
            return JSONResponse(content={
                "code": 400,
                "data": {},
                "msg": get_translation("verification_code_must_be_6_digits")
            })
            
        # 查询账号信息
        account = await mongo_instance.find_one("accounts", {"email": request.email})
        if not account:
            return JSONResponse(content={
                "code": 400,
                "data": {},
                "msg": get_translation("email_not_exist")
            })
        
        # 检查验证码是否匹配
        if str(account.get('verification_code')) != request.code:
            return JSONResponse(content={
                "code": 400,
                "data": {},
                "msg": get_translation("verification_code_error")
            })
        
    #设置token有效期为2小时 7200
    utc_now, beijing_formatted_time, utc_delta = mongo_instance.get_current_time(7200)
        
    # 检查验证码是否过期
    if mongo_instance.compare_time(utc_now, account.get('code_expires_at', 0)):
        return JSONResponse(content={
            "code": 400,
            "data": {},
            "msg": get_translation("verification_code_expired")
        })
    
    # 验证通过，生成新token
    token = mongo_instance.generate_token()
        
    await mongo_instance.update_one(
        "accounts",
        {"email": request.email},
        {"$set": {
            "token": token,
            "token_created_at": utc_now,
            "token_expires_at": utc_delta,
            "last_updated_at": utc_now
        }}
    )
    
    user_id = account.get('user_id')
        
    # 获取用户信息
    user = await mongo_instance.find_one("users", {"_id": user_id})
    
    if not user:
        await create_user(user_id, request.email.split('@')[0], "", utc_now, beijing_formatted_time)
    
    return JSONResponse(content={
        "code": 0,
        "data": {
            "userID":str(user_id),
            "accessToken": token
        },
        "msg": get_translation("login_success")
    })