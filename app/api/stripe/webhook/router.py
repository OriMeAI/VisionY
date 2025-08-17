from fastapi import APIRouter, HTTPException, Request, status
import logging
from app.data.membership import get_membership_benefit_item
from app.utils.mongo import mongo_instance
from app.utils.stripe import stripe_instance
from pydantic import BaseModel

class SubscriptionData(BaseModel):
    id: str
    customer: str
    status: str  # 用于过滤续订事件

webhook_router = APIRouter()

@webhook_router.post('/webhook')
async def operator(request: Request):
    """
    处理 Stripe Webhook 请求，包括签名验证和事件处理。
    """
    
    payload = await request.body()
    sig_header = request.headers.get("stripe-signature")

    try:
        # 验证签名确保请求来自 Stripe
        verify_result = stripe_instance.verify_webhook_signature(payload,sig_header)
        
        if verify_result['result'] != 0:
            logging.error("Webhook signature verification failed")
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid webhook signature")
        
        event = verify_result['event']

        # 仅处理订阅相关事件
        if event.type == "customer.subscription.updated":
            subscription = SubscriptionData(**event["data"]["object"])
            if subscription.status == "active":  
                # 续订成功逻辑（需检查是否是新周期）
                await handle_subscription_renewal(subscription)
        elif event.type == "customer.subscription.deleted":
            subscription = SubscriptionData(**event["data"]["object"])
            #await handle_subscription_cancellation(subscription)

        return {"status": "success"}
    
    except HTTPException as e:
        raise e
    except Exception as e:
        logging.error(f"Handle Webhook error: {str(e)}", exc_info=True)
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Internal server error")
    
async def handle_subscription_renewal(subscription: dict) -> bool:
    """
    处理订阅续费事件 (BILLING.SUBSCRIPTION.UPDATED)
    """
    current_time, _, _ = mongo_instance.get_current_time()
    
    subscription_id = subscription.get("id")  # 订阅ID
    
    if not subscription_id:
        logging.error(f"Subscription ID is missing in the event: {subscription}")
        return False
    
    subscription_status = subscription.get("status")
    
    # 只处理活跃状态的订阅
    if subscription_status != "active":
        logging.info(f"Subscription status is {subscription_status}, not processing as renewal")
        return False
    
    logging.info(f"Processing subscription renewal for subscription_id: {subscription_id}, status: {subscription_status}")
    
    try:
        # 查找对应的用户
        user = await mongo_instance.find_one(
            "users",
            {"stripe_subscription_id": subscription_id}
        )
        
        if not user:
            logging.error(f"User not found for subscription_id: {subscription_id}")
            return False
        
        user_id = user["_id"]
        
        # 判断是否为续订
        current_created_at = user.get("membership_created_at")
        current_expires_at = user.get("membership_expires_at")
        #当第一次订阅的时间 会让 current_expires_at 与 current_created_at 不同。并且 续订的时间 一定小于当前时间
        is_renewal = current_expires_at > current_created_at and current_expires_at > current_time
        
        if not is_renewal:
            logging.info(f"Subscription is not a renewal for user {user_id}")            
            return False
                
        # 获取会员等级
        membership_level = user['membership_level']
        
        if membership_level is None:
            logging.error(f"Unable to determine membership level for subscription {subscription_id}")
            return False
            
        # 获取会员权益
        membership_benefits = get_membership_benefit_item()
        
        # 找到对应等级的权益
        item_benefit = None
        plan_info = None
        for item in membership_benefits:
            if item["id"] == membership_level:
                item_benefit = item["benefit"]
                plan_info = item
                break
                
        if not item_benefit:
            logging.error(f"Membership benefit not found for level {membership_level}")
            return False
                                    
        # 计算会员到期时间
        month_count = item_benefit.get("month_count", 1)
        new_expires_at = mongo_instance.calculate_membership_expire_time(current_expires_at, month_count)
        
        #生成一个客户端自己的ID
        token = mongo_instance.generate_token()
        
        # 插入订阅记录到 user_transactions 集合的 recharge_history
        await mongo_instance.update_one(
            "user_transactions",
            {"user_id": user_id},
            {
                "$push": {
                    "recharge_history": {
                        "recharge_time": current_time,
                        "recharge_type": "membership_subscription",
                        "recharge_channel": "stripe",
                        "recharge_stripe_id":subscription_id,
                        "recharge_amount": float(plan_info.get('price', 0)),
                        "recharge_item_id": int(membership_level),
                        "recharge_membership_level": int(membership_level),
                        "recharge_token": token,
                        "recharge_status": "renewed"
                    }
                },
                "$set": {"last_updated_at": current_time}
            }
        )
        
        # 更新用户会员信息
        await mongo_instance.update_one(
            "users",
            {"_id": user_id},
            {
                "$set": {
                    "membership_level": membership_level,
                    "membership_expires_at": new_expires_at,
                    "last_updated_at": current_time
                }
            }
        )
        
        return True
            
    except Exception as e:
        logging.error(f"Error processing subscription renewal: {str(e)}", exc_info=True)
        return False