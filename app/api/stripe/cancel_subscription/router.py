from fastapi import APIRouter,Body
from fastapi.responses import JSONResponse
from app.utils.core import get_user_id
import logging
from app.utils.mongo import mongo_instance

cancel_subscription_router = APIRouter()

@cancel_subscription_router.post('/cancel_subscription')
async def operator(
    token: str = Body(..., embed=True)
):
    user_id = get_user_id()
    
    #查询数据，将订单修改为取消状态
    current_time, _, _ = mongo_instance.get_current_time()
    
    # 使用 $set 和位置操作符 $ 来更新数组中匹配的元素
    await mongo_instance.update_one(
        "user_transactions",
        {
            "user_id": user_id,  # 添加用户ID作为查询条件
            "recharge_history.recharge_token": token
        },  # 查询条件：recharge_history 数组中 recharge_token 等于 token
        {
            "$set": {
                "recharge_history.$.recharge_status": "canceled",  # 使用 $ 位置操作符更新匹配的数组元素
                "last_updated_at": current_time
            }
        }
    )
    
    logging.info(f"user_id: {user_id}, cancel subscription success, token: {token}")
    
    return JSONResponse(content={
        "code": 0,
        "data": None,
        "msg": "cancel subscription success",
    })
