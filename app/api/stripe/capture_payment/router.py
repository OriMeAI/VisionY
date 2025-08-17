from fastapi import APIRouter, Body
from fastapi.responses import JSONResponse
from app.utils.stripe import stripe_instance
from app.utils.core import get_user_id
from app.utils.mongo import mongo_instance
import logging
from app.locales.translations import get_translation
from app.collections.user import handle_purchase_credits

capture_payment_router = APIRouter()

@capture_payment_router.post('/capture_payment')
async def operator(
    token: str = Body(..., embed=True)
):
    user_id = get_user_id()
    current_time, _, _ = mongo_instance.get_current_time()
            
    # 使用聚合查询直接获取匹配的recharge记录
    pipeline = [
        {
            "$match": {
                "user_id": user_id,
                "recharge_history": {
                    "$elemMatch": {
                        "recharge_token": token,
                        "recharge_status": "created"
                    }
                }
            }
        },
        {
            "$project": {
                "recharge_info": {
                    "$filter": {
                        "input": "$recharge_history",
                        "cond": {
                            "$and": [
                                {"$eq": ["$$this.recharge_token", token]},
                                {"$eq": ["$$this.recharge_status", "created"]}
                            ]
                        }
                    }
                }
            }
        }
    ]

    aggregate_result = await mongo_instance.aggregate("user_transactions", pipeline)
    recharge_info = None
    if aggregate_result and len(aggregate_result) > 0 and aggregate_result[0].get('recharge_info'):
        recharge_info = aggregate_result[0]['recharge_info'][0]  # 取第一个匹配的记录
    
    if not recharge_info:
        logging.warning(f"user_id: {user_id}, token: {token}, recharge info not found")
        return JSONResponse(content={
            "code": 1,
            "data": None,
            "msg": get_translation("recharge_info_not_found"),
        })
        
    
    stripe_id = recharge_info['recharge_stripe_id']
    capture_result = stripe_instance.capture_payment(stripe_id)
    
    if capture_result['result'] == 0:        
        logging.info(f"user_id: {user_id}, token: {token}, capture payment success")
        
        # 更新recharge_history状态为completed
        await mongo_instance.update_one(
            "user_transactions",
            {
                "user_id": user_id,
                "recharge_history.recharge_token": token
            },
            {
                "$set": {
                    "recharge_history.$.recharge_status": "completed",
                    "recharge_history.$.recharge_extra": capture_result,
                    "last_updated_at": current_time
                }
            }
        )
        
        # 只处理购买积分的逻辑
        # 购买积分：增加purchase_credits
        recharge_credits = recharge_info.get('recharge_credits', 0)
        await handle_purchase_credits(user_id, recharge_credits, current_time)
                
        logging.info(f"user_id: {user_id}, purchase_credits added: {recharge_credits}")

        
        return JSONResponse(content={
            "code": 0,
            "data": None,
            "msg": get_translation("purchase_success"),
        })
    else:
        # 使用 $set 和位置操作符 $ 来更新数组中匹配的元素
        await mongo_instance.update_one(
            "user_transactions",
            {
                "user_id": user_id,
                "recharge_history.recharge_token": token
            },
            {
                "$set": {
                    "recharge_history.$.recharge_status": "failed",
                    "last_updated_at": current_time
                }
            }
        )
        
        logging.info(f"user_id: {user_id}, token: {token}, capture payment failed, msg is: {capture_result['msg']}")
        
        return JSONResponse(content={
            "code": 1,
            "data": None,
            "msg": capture_result['msg'],
        })