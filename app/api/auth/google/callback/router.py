from fastapi import APIRouter, Request
from fastapi.responses import RedirectResponse
from app.utils.auth import auth_instance
from app.utils.mongo import mongo_instance
from app.collections.user import create_user
import logging
from urllib.parse import unquote

callback_router = APIRouter()

@callback_router.get('/callback')
async def operator(request: Request):    
    # 获取原始页面路径（来自 state）
    raw_state = request.query_params.get("state", "/")
    redirect_url = unquote(raw_state)
     
    try:    
        # 获取 OAuth 令牌
        google_token = await auth_instance.oauth.google.authorize_access_token(request)
    except Exception as e:
        logging.error(f"authorize_access_token Error: {e}")
        # 拼接并重定向到前端 + 失败信息
        final_url = f"{redirect_url}?access_token=google_login_fail"
        return RedirectResponse(redirect_url)
    
    # 解析 ID 令牌获取用户信息
    user_info = google_token.get('userinfo')
    if not user_info:
        try:
            # 如果 userinfo 不存在，尝试解析 id_token
            user_info = await auth_instance.oauth.google.parse_id_token(request, google_token)
        except Exception as e:
            logging.error(f"Error parsing id_token: {e}")
            # 拼接并重定向到前端 + 失败信息
            final_url = f"{redirect_url}?access_token=google_login_fail"
            return RedirectResponse(final_url)
            
    # 获取用户基本信息
    user_email = user_info.get('email')
    user_name = user_info.get('given_name') if user_info.get('given_name', '') else user_info.get('family_name')
    avatar = user_info.get('picture')
    
    if not user_email:
        logging.error("No email found in Google user info")
        final_url = f"{redirect_url}?access_token=google_login_fail"
        return RedirectResponse(final_url)
    
    # 获取当前时间
    utc_now, beijing_formatted_time, utc_delta = mongo_instance.get_current_time(7200)  # token有效期2小时
    
    # 检查账号表是否已经注册，如果没有注册则先注册
    account = await mongo_instance.find_one("accounts", {"email": user_email})
    
    # 生成token
    token = mongo_instance.generate_token()
        
    if not account:
        # 创建新账号ID
        account_id = mongo_instance.generate_object_id()
        # 创建新用户ID
        user_id = mongo_instance.generate_object_id()
        # 创建账号记录
        account_data = {
            "_id": account_id,
            "email": user_email,
            "status":"active", 
            "account_type": "google",
            "user_id": user_id,
            "token": token,
            "token_created_at": utc_now,
            "token_expires_at": utc_delta,
            "verification_code": "",
            "code_created_at": utc_now,
            "code_expires_at": utc_now,
            "last_updated_at": utc_now,
            "created_at": utc_now,
            "created_at_str": beijing_formatted_time,
        }
        await mongo_instance.insert_one("accounts", account_data)
        
    else:
        user_id = account.get('user_id')
        # 更新已有账号的token
        await mongo_instance.update_one(
            "accounts",
            {"email": user_email},
            {"$set": {
                "token": token,
                "token_created_at": utc_now,
                "token_expires_at": utc_delta,
                "last_updated_at": utc_now
            }}
        )
        
    # 检查用户是否存在
    user = await mongo_instance.find_one("users", {"_id": user_id})
    if not user:
        await create_user(user_id, user_name, avatar, utc_now, beijing_formatted_time)
    
    # 拼接并重定向到前端 + token
    final_url = f"{redirect_url}?access_token={token}&user_id={user_id}"
    
    return RedirectResponse(final_url)