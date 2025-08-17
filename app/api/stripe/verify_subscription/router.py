from fastapi import APIRouter, Body
from fastapi.responses import JSONResponse
from app.utils.stripe import stripe_instance
from app.utils.core import get_user_id
from app.utils.mongo import mongo_instance
from app.data.membership import get_membership_benefit_item
import logging
from app.locales.translations import get_translation
from app.collections.user import handle_subscribe_membership

verify_subscription_router = APIRouter()

@verify_subscription_router.post('/verify_subscription')
async def operator(
    token: str = Body(..., embed=True)
):
    user_id = get_user_id()
    current_time, _, _ = mongo_instance.get_current_time()
    
    # 使用聚合查询直接获取匹配的recharge记录（订阅类型）
    pipeline = [
        {
            "$match": {
                "user_id": user_id,
                "recharge_history": {
                    "$elemMatch": {
                        "recharge_token": token,
                        "recharge_status": "created",
                        "recharge_type": "membership_subscription"
                    }
                }
            }
        },
        {
            "$project": {
                "subscription_info": {
                    "$filter": {
                        "input": "$recharge_history",
                        "cond": {
                            "$and": [
                                {"$eq": ["$$this.recharge_token", token]},
                                {"$eq": ["$$this.recharge_status", "created"]},
                                {"$eq": ["$$this.recharge_type", "membership_subscription"]}
                            ]
                        }
                    }
                }
            }
        }
    ]
    
    aggregate_result = await mongo_instance.aggregate("user_transactions", pipeline)
    subscription_info = None
    if aggregate_result and len(aggregate_result) > 0 and aggregate_result[0].get('subscription_info'):
        subscription_info = aggregate_result[0]['subscription_info'][0]  # 取第一个匹配的记录
    
    if not subscription_info:
        logging.warning(f"user_id: {user_id}, token: {token}, subscription info not found")
        return JSONResponse(content={
            "code": 1,
            "data": None,
            "msg": get_translation("subscription_info_not_found"),
        })
        
    stripe_id = subscription_info['recharge_stripe_id']
    
    verify_result = stripe_instance.verify_subscription(stripe_id)
        
    if verify_result['result'] == 0:
        logging.info(f"user_id: {user_id}, token: {token}, verify subscription success")
                                
        # 更新recharge_history状态为completed
        await mongo_instance.update_one(
            "user_transactions",
            {
                "user_id": user_id,
                "recharge_history.recharge_token": token
            },
            {
                "$set": {
                    "recharge_history.$.recharge_status": "subscribed",
                    "recharge_history.$.recharge_extra": verify_result,
                    "last_updated_at": current_time
                }
            }
        )
        
        # 获取会员计划信息
        membership_level = subscription_info.get('recharge_membership_level', 0)
        membership_items = get_membership_benefit_item()
        
        # 查找对应的会员计划
        plan_info = None
        for item in membership_items:
            if item.get('id', 0) == membership_level:
                plan_info = item
                break
        
        if plan_info:
            expire_time = await handle_subscribe_membership(user_id, membership_level,stripe_id,current_time)            
            logging.info(f"user_id: {user_id}, membership updated: level {membership_level}, expire_time: {expire_time}")
            
            return JSONResponse(content={
                "code": 0,
                "data": None,
                "msg": get_translation("subscription_success"),
            })
        else:
            logging.error(f"Membership plan {membership_level} not found")
            return JSONResponse(content={
                "code": 1,
                "data": None,
                "msg": get_translation("invalid_membership_plan"),
            })
    else:
        # 更新recharge_history状态为failed
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
        
        logging.info(f"user_id: {user_id}, token: {token}, verify subscription failed")
        
        return JSONResponse(content={
            "code": 1,
            "data": None,
            "msg": get_translation("subscription_verification_failed"),
        })