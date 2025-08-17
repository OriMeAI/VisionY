from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse
from app.utils.mongo import mongo_instance
from app.utils.core import get_user_id
from app.data.membership import get_membership_benefit_item
from app.collections.user import calculate_user_credits
from datetime import datetime, timezone

info_router = APIRouter()

@info_router.get('/info')
async def operator():
    user_id = get_user_id()
    user = await mongo_instance.find_one("users", {"_id": user_id})
        
    membership_level = user.get("membership_level", 0)
    membership_items = get_membership_benefit_item()
    
    default_name = membership_items[0].get("name")
    planName = membership_items[membership_level].get("name", default_name)
    
    #获取当前可用积分
    credits = await calculate_user_credits(user_id)
            
    #获取会员过期时间
    if membership_level > 0:
        # 处理时间格式
        membership_expires_at = user.get("membership_expires_at", "")
        if membership_expires_at.tzinfo is None:
            membership_expires_at = membership_expires_at.replace(tzinfo=timezone.utc)
        membership_expires_at_str = membership_expires_at.strftime("%Y-%m-%dT%H:%M:%SZ")
        plan_expiry_time = membership_expires_at_str
    else:
        plan_expiry_time = ""
    
    response_data = {
        "name": user.get("nickname", ""),
        "avatar": user.get("avatar", ""),
        "planId": membership_level,
        "planName": planName,
        "planExpiryTime": plan_expiry_time,
        "credits": credits,
    }
    
    return JSONResponse(content={
        "code": 0,
        "data": response_data,
        "msg": "",
    })