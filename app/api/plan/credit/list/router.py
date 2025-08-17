from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse
from app.data.credit import get_credit_items
from app.utils.mongo import mongo_instance
import copy
from app.utils.core import get_user_id

# 创建路由器
#叶子节点的blueprint不加url_prefix
list_router = APIRouter()

@list_router.get('/list')
async def operator():
    items = get_credit_items()
    
    # 深拷贝items，避免修改原始数据
    items_copy = copy.deepcopy(items)
    
    is_first_recharge = True
    
    # 如果用户已登录，根据用户的首充状态修改isFirstRecharge
    user_id = get_user_id()
    if user_id is not None:
        user = await mongo_instance.find_one("users", {"_id": user_id})
        if user:
            is_first_recharge = user.get('is_first_recharge', False)
                
    if is_first_recharge:
        items_copy.pop(1)
    else:
        items_copy = items_copy[1:]
        
    return JSONResponse(
        content={
            "code": 0,
            "data": items_copy,
            "msg": ""
        }
    )