from fastapi import APIRouter,Body
from fastapi.responses import JSONResponse
from app.utils.stripe import stripe_instance
from app.utils.core import get_user_id
import logging
from app.utils.mongo import mongo_instance
from app.data.credit import get_credit_items
from app.locales.translations import get_translation

create_payment_router = APIRouter()

@create_payment_router.post('/create_payment')
async def operator(
    itemId: int = Body(...),
    amount: int = Body(...),
    returnUrl: str = Body(...),
    cancelUrl: str = Body(...)
):
    user_id = get_user_id()
    
    # 从数据库查询用户信息
    user = await mongo_instance.find_one("users", {"_id": user_id})
    is_first_recharge = user.get('is_first_recharge', False)
    
    
    #根据ID查询 item
    items = get_credit_items()
    
    # 从items中找到id为itemId的item
    item = next((item for item in items if item.get('id') == itemId), None)
    
    # 如果没有找到对应的item，返回错误
    if item is None:
        return JSONResponse(content={
            "code": 1,
            "data": None,
            "msg": get_translation("invalid_credit_item_id"),
        })
        
    if not is_first_recharge:
        item_is_first_recharge = item["isFirstRecharge"]
        if item_is_first_recharge:
            return JSONResponse(content={
                "code": 1,
                "data": None,
                "msg": get_translation("payment_creation_failed")
            })
            
        
    item_code = item["code"]
    purchase_credits = item["addonValue"]
    item_price = item["price"]
    
    #生成一个客户端自己的ID
    client_reference_id = mongo_instance.generate_token()
            
    create_result = stripe_instance.create_payment(
        client_reference_id = client_reference_id,
        item_code=item_code,
        success_url=f"{returnUrl}?credits_result=success&token={client_reference_id}",
        cancel_url=f"{cancelUrl}?credits_result=cancel&token={client_reference_id}"
    )
    
    if create_result['result'] == 0:
        approval_url = create_result['url']
            
        #这里需要获取到token,然后保存到数据库
        token = client_reference_id
        # print(token)  # 输出: 3PL745742H778692J
        
        #这里需要将交易信息插入到用户的user_transactions集合的recharge_history，状态为created
        current_time, _, _ = mongo_instance.get_current_time()
        
        # 插入交易记录到 user_transactions 集合的 recharge_history
        await mongo_instance.update_one(
            "user_transactions",
            {"user_id": user_id},
            {
                "$push": {
                    "recharge_history": {
                        "recharge_time": current_time,
                        "recharge_type": "purchase_credits",
                        "recharge_channel": "stripe",
                        "recharge_stripe_id":create_result['id'],
                        "recharge_amount": item_price,
                        "recharge_item_id": itemId,
                        "recharge_credits":purchase_credits,
                        "recharge_token": token,
                        "recharge_status": "created"
                    }
                },
                "$set": {"last_updated_at": current_time}
            }
        )
        
        logging.info(f"user_id: {user_id}, create payment success, approval_url: {approval_url}")
        
        return JSONResponse(content={
            "code": 0,
            "data": {"approval_url":approval_url},
            "msg": "create payment success",
        })
    else:
        return JSONResponse(content={
            "code": 1,
            "data": None,
            "msg": create_result['msg'],
        })
