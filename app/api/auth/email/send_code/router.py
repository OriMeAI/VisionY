import random
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from email.mime.text import MIMEText
from email.header import Header
from app.utils.mongo import mongo_instance
from pydantic import BaseModel, EmailStr
from app.locales.translations import get_translation
import logging

from app.utils.email_sender import send_user_login_sign_number

# 请求模型
class EmailRequest(BaseModel):
    email: EmailStr

send_code_router = APIRouter()

@send_code_router.post('/send_code')
async def operator(request: EmailRequest):
    # 生成六位数字验证码和token，写入账号表
    verification_code = str(random.randint(100000, 999999))
    
    #验证码5分钟过期，为300秒
    utc_now, beijing_formatted_time, utc_delta = mongo_instance.get_current_time(300)
    
    # 检查账号表是否已经注册，如果没有注册 则先注册
    account = await mongo_instance.find_one("accounts", {"email": request.email})
    
    if not account:
        # 创建新账号ID
        account_id = mongo_instance.generate_object_id()
        # 创建新用户ID
        user_id = mongo_instance.generate_object_id()
        # 创建账号记录
        account_data = {
            "_id": account_id,
            "email": request.email,
            "status":"active", 
            "account_type":"email",
            "user_id": user_id,
            "token": "",
            "token_created_at": utc_now,
            "token_expires_at": utc_now,  
            "verification_code": verification_code,
            "code_created_at": utc_now,
            "code_expires_at": utc_delta,  # 5分钟过期
            "last_updated_at": utc_now,
            "created_at": utc_now,
            "created_at_str": beijing_formatted_time,
        }
        await mongo_instance.insert_one("accounts", account_data)
            
    else:
        # 更新已有账号的验证码和token
        await mongo_instance.update_one(
            "accounts",
            {"email": request.email},
            {"$set": {
                "token": "",
                "token_created_at": utc_now,
                "token_expires_at": utc_now,  
                "verification_code": verification_code,
                "code_created_at": utc_now,
                "code_expires_at": utc_delta,
                "last_updated_at": utc_now
            }}
        )

    # 通过邮箱发送，根据发送结果给出信息
    send_result = await send_user_login_sign_number(request.email, verification_code)

    if send_result.get('state',1) == 0:
        return JSONResponse(content={
            "code": 0,
            "data": {},
            "msg": get_translation("verification_code_sent_to_your_email")
        })
    else:
        logging.error(f"Failed to send verification code to {request.email}: {send_result}")
        return JSONResponse(content={
                "code": 500,
                "data": {},
                "msg": get_translation("verification_code_sent_failed")
            })

 