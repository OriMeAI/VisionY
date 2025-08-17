"""

账号功能类
accounts= {
    "_id": ObjectID,
    "email": "XXXX@mail.com",
    "status":"active", #删除后变为inactive
    "account_type": "google", # email（自己的email）, google ,github or tiktok...
    "user_id": "user_1", 
    "token": 0,
    'token_created_at':  datetime.now(),
    'token_expires_at':  datetime.now() + 300,
    'verification_code': verification_code,
    'code_created_at':  datetime.now(),
    'code_expires_at':  datetime.now() + 300,
    "last_updated_at": datetime.now(),
    "created_at": datetime.now(),
    "created_at_str": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
}

user 结构的功能类
users= {
    "_id": ObjectID,
    "nickname": "",
    "avatar": "",
    "stripe_subscription_id": "", #paypal的会员订阅 subscription_id
    "free_credits": 400, #每个月剩余的免费的积分，积分分为免费积分、会员积分、购买积分。积分扣除的时间先扣除免费积分，再扣除会员积分，最后扣除购买积分。
    "membership_credits": 0, #每个月剩余的会员积分，每个月重置一次，会员到期后，会员积分清零。
    "purchase_credits": 0, #剩余的购买积分，永久有效。
    "project_count_limit": 10, #该等级会员项目数量
    "membership_created_at": datetime.now(), #membership购买时间
    "membership_expires_at" : datetime.now(), #membership结束时间
    "membership_level": 0, #membership等级 planId 从0开始，0代表普通会员
    "membership_next_month_update_at" : datetime.now(), #下个月权益更新时间，每次交互做更新检查
    "free_next_month_update_at" : datetime.now(), #下个月权益更新时间，每次交互做更新检查
    "is_first_recharge": True, #是否首次购买积分,购买后修改为False
    "last_login_at": datetime.now(), #最后登录时间
    "last_updated_at": datetime.now(),
    "created_at": datetime.now(),
    "created_at_str": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
}

user_transactions = {
    "_id": ObjectID,
    "user_id": ObjectID,
    "used_credits": 0, #已使用积分
    "credits_used_history": [ # 使用历史 "credits_type" 需要转换成翻译后的文字，发送给前端。 free_credits 代表免费积分，membership_credits 代表会员积分，purchase_credits 代表购买积分
        {"used_time": datetime.now(), "credits_type": "free_credits", "used_channel": "liblib", "used_type": "generate_image", "used_credits": 10, "used_token": ObjectID},
        {"used_time": datetime.now(), "credits_type": "membership_credits", "used_channel": "openAI", "used_type": "generate_image", "used_credits": 10, "used_token": ObjectID},
        {"used_time": datetime.now(), "credits_type": "purchase_credits", "used_channel": "Gemini", "used_type": "generate_image", "used_credits": 10, "used_token": ObjectID},
    ], 
    "credits_obtained_history": [ # 获取历史 "credits_type" 需要转换成翻译后的文字，发送给前端。不同的使用类型，决定obtained_credits的单位，比如积分，美元等。
        {"obtained_time": datetime.now(), "credits_type": "free_credits"", "obtained_credits": 10},
        {"obtained_time": datetime.now(), "credits_type": "membership_credits", "obtained_credits": 10},
        {"obtained_time": datetime.now(), "credits_type": "purchase_credits", "obtained_credits": 10},
    ], 
    "recharge_history":[ 
        # 充值记录 购买会员，或者是购买积分记录 recharge_amount 是花费的金额，单位是美元 
        # recharge_status purchase_credits 分为created，completed，failed, canceled, 
        # recharge_status membership_subscription 分为created，completed，failed, canceled, renewed,subscribed
        # recharge_membership_level 购买的会员等级
        {"recharge_time": datetime.now(), "recharge_type": "membership_subscription", "recharge_channel": "paypal", "recharge_amount": 10,"recharge_item_id": 0,"recharge_membership_level": 10, "recharge_token": ObjectID, "recharge_status": "created"},
        {"recharge_time": datetime.now(), "recharge_type": "purchase_credits", "recharge_channel": "paypal", "recharge_amount": 10,"recharge_item_id": 0, "recharge_credits": 10, "recharge_token": ObjectID, "recharge_status": "failed"},
    ], 
    "last_updated_at": datetime.now(),
    "created_at": datetime.now(),
    "created_at_str": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
}

free_credits 可以为负，但是会在每次积分更新，先补足free_credits。

"""
import time
import asyncio
import logging
from app.utils.mongo import mongo_instance
from app.data.membership import get_membership_benefit_item

#创建用户数据
async def create_user(user_id,nickname,avatar,utc_now,beijing_formatted_time):
    """
    创建用户
    """
    membership_items = get_membership_benefit_item()
    item_benefit = membership_items[0]["benefit"]
    free_credits_amount = item_benefit['free_credits']
    
    #用户表
    user_data = {
        "_id": user_id,
        "nickname": nickname,  # 默认用户名为邮箱前缀
        "avatar": avatar,
        "subscription_id":"", #会员订阅 subscription_id。具体哪个渠道需要查询交易记录
        "free_credits": free_credits_amount, #每个月免费的积分，积分分为免费积分、会员积分、购买积分。积分扣除的时间先扣除免费积分，再扣除会员积分，最后扣除购买积分。
        "membership_credits": 0, #会员积分，每个月重置一次，会员到期后，会员积分清零。
        "purchase_credits": 0, #购买积分，永久有效。
        "project_count_limit": item_benefit['project_count'], #该等级会员项目数量
        "membership_created_at": utc_now, #会员购买时间
        "membership_expires_at" : utc_now, #会员结束时间
        "membership_level": 0, #会员等级 从0开始，0代表免费用户
        "membership_next_month_update_at" : utc_now, #下个月权益更新时间，每次交互做更新检查
        "free_next_month_update_at" : mongo_instance.calculate_next_monthly_update_time(utc_now), #下个月权益更新时间，每次交互做更新检查
        "is_first_recharge": True, #是否首次购买文生图次数,购买后修改为False
        "last_updated_at": utc_now,
        "created_at": utc_now,
        "created_at_str": beijing_formatted_time
    }
    await mongo_instance.insert_one("users", user_data)
    
    #用户交易表
    transaction_id = mongo_instance.generate_object_id()
    transaction_data = {
        "_id": transaction_id,
        "user_id": user_id,
        "used_credits": 0, #已使用积分
        "credits_used_history": [], #使用历史
        "credits_obtained_history": [{
                        "obtained_time": utc_now,
                        "credits_type": "free_credits",
                        "obtained_credits": free_credits_amount
                    }], #获得历史
        "recharge_history":[], #充值记录
        "last_updated_at": utc_now,
        "created_at": utc_now,
        "created_at_str": beijing_formatted_time
    }
    await mongo_instance.insert_one("user_transactions", transaction_data)
    
#更新用户权益      
async def update_user_benefits(user_id):
    """
    使用分布式锁确保用户权益更新的原子性和并发安全
    需要特殊处理 free_credits为负的情况。
    更新用户的权益并返回当前权益数据
    Returns:
        bool: 是否更新了权益
    """    
    # 最新的用户信息
    user = await mongo_instance.find_one("users", {"_id": user_id})
    if not user:
        return False
    
    # 基于用户数据的智能检查
    current_time, _, _ = mongo_instance.get_current_time()
    
    # 更新用户的登录记录
    await mongo_instance.update_one(
        "users",
        {"_id": user_id},
        {"$set": {"last_login_at": current_time}}
    )
    
    # 检查是否需要更新权益
    needs_update = False
    
    # 检查免费积分是否需要更新
    if mongo_instance.compare_time(current_time, user.get('free_next_month_update_at', 0)):
        needs_update = True
    
    # 检查会员积分是否需要更新
    membership_level = user.get('membership_level', 0)
    if membership_level > 0 and mongo_instance.compare_time(current_time, user.get('membership_next_month_update_at', 0)):
        needs_update = True
    
    # 检查会员是否过期
    if membership_level > 0 and mongo_instance.compare_time(current_time, user.get('membership_expires_at', 0)):
        needs_update = True
    
    # 只有在需要时才更新
    if not needs_update:
        return
    
    max_wait_time = 60  # 最大等待时间（秒）
    check_interval = 0.5  # 检查间隔（秒）
    start_time = time.time()
    
    while time.time() - start_time < max_wait_time:
        lock_current_time = time.time()
        lock_timeout = lock_current_time - 30 #30秒锁超时
        
        # 尝试获取锁
        lock_result = await mongo_instance.update_one(
            "user_benefits_locks",
            {
                "user_id": user_id,
                "$or": [
                    {"locked_at": {"$exists": False}},
                    {"locked_at": {"$lt": lock_timeout}}
                ]
            },
            {
                "$set": {
                    "user_id": user_id,
                    "locked_at": lock_current_time,
                    "process_id": f"{time.time()}_{id(object())}",
                    "operation": "update_user_benefits"
                }
            },
            upsert=True
        )
        
        if lock_result and lock_result.modified_count > 0:
            break
        else:
            # 等待后重试
            await asyncio.sleep(check_interval)
        
    if not lock_result or lock_result.modified_count == 0:
        # 获取锁失败，说明有其他进程正在处理
        logging.error(f"Critical Error for user {user_id}, when update_user_benefits")
    
    try:       
        # 获得锁后，重新查询最新的用户信息
        user = await mongo_instance.find_one("users", {"_id": user_id})
        if not user:
            return False     
        
        membership_items = get_membership_benefit_item()
        membership_level = user.get('membership_level', 0)
        # 获取当前的 free_credits 值
        current_free_credits = user.get('free_credits', 0)
        
        # 检查会员是否过期
        if membership_level > 0 and mongo_instance.compare_time(current_time, user['membership_expires_at']):
            # 会员过期，重置为免费用户
            item_benefit = membership_items[0]["benefit"]
            await mongo_instance.update_one(
                "users",
                {"_id": user_id},
                {"$set": {
                    "membership_level": 0,
                    "project_count_limit": item_benefit['project_count'],
                    "last_updated_at": current_time
                }}
            )
            membership_level = 0
        
        # 更新免费权益
        if mongo_instance.compare_time(current_time, user['free_next_month_update_at']):
            next_update_time = mongo_instance.calculate_next_monthly_update_time(current_time)
            
            item_benefit = membership_items[0]["benefit"]
            free_credits_amount = item_benefit['free_credits']
                            
            # 如果 free_credits 为负数，则设置为 free_credits + free_credits_amount
            if current_free_credits < 0:
                new_free_credits = current_free_credits + free_credits_amount
            else:
                new_free_credits = free_credits_amount
                
            current_free_credits = new_free_credits
                    
            await mongo_instance.update_one(
                "users",
                {"_id": user_id},
                {"$set": {
                    "free_credits": new_free_credits,
                    "free_next_month_update_at": next_update_time,
                    "last_updated_at": current_time
                }}
            )
            
            # 在 user_transactions 中记录免费积分获取历史
            await mongo_instance.update_one(
                "user_transactions",
                {"user_id": user_id},
                {
                    "$push": {
                        "credits_obtained_history": {
                            "obtained_time": current_time,
                            "credits_type": "free_credits",
                            "obtained_credits": free_credits_amount
                        }
                    },
                    "$set": {"last_updated_at": current_time}
                }
            )
                
        # 更新会员权益
        if membership_level > 0 and mongo_instance.compare_time(current_time, user['membership_next_month_update_at']):
            next_update_time = mongo_instance.calculate_next_update_time(user['membership_created_at'], current_time)
            item_benefit = membership_items[membership_level]["benefit"]
            
            if item_benefit:
                membership_credits_amount = item_benefit["membership_credits"]
                
                # 如果 free_credits 为负数，需要特殊处理
                if current_free_credits < 0:
                    # free_credits 设置为 free_credits + membership_credits_amount
                    new_free_credits = current_free_credits + membership_credits_amount
                    # membership_credits 设置为 membership_credits_amount + free_credits，但不能小于零
                    new_membership_credits = max(0, membership_credits_amount + current_free_credits)
                    
                    await mongo_instance.update_one(
                        "users",
                        {"_id": user_id},
                        {
                            "$set": {
                                "free_credits": new_free_credits,
                                "membership_next_month_update_at": next_update_time,
                                "last_updated_at": current_time
                            },
                            "$inc": {
                                "membership_credits": new_membership_credits
                            }
                        }
                    )
                else:
                    # free_credits 不为负数时，按原逻辑处理
                    await mongo_instance.update_one(
                        "users",
                        {"_id": user_id},
                        {
                            "$set": {
                                "membership_next_month_update_at": next_update_time,
                                "last_updated_at": current_time
                            },
                            "$inc": {
                                "membership_credits": membership_credits_amount
                            }
                        }
                    )
                
                # 在 user_transactions 中记录会员积分获取历史
                await mongo_instance.update_one(
                    "user_transactions",
                    {"user_id": user_id},
                    {
                        "$push": {
                            "credits_obtained_history": {
                                "obtained_time": current_time,
                                "credits_type": "membership_credits",
                                "obtained_credits": membership_credits_amount
                            }
                        },
                        "$set": {"last_updated_at": current_time}
                    }
                )
        
        return True
        
    finally:
        # 释放锁
        await mongo_instance.delete_one(
            "user_benefits_locks",
            {"user_id": user_id}
        )

#判断当前用户项目是否已经超出上限
async def is_project_count_exceeded(user_id):
    """
    判断当前用户项目是否已经超出上限

    Args:
        user_id: 用户ID

    Returns:
        bool: True表示超出上限，False表示未超出上限
    """    
    # 获取用户当前的项目数量（只统计未删除的项目）
    project_count = await mongo_instance.count("projects", {
        "user_id": user_id,
        "status": "active"
    })
    
    # 从数据库查询用户信息
    user = await mongo_instance.find_one("users", {"_id": user_id})
    
    # 获取用户等级对应的项目数量限制
    project_count_limit = user.get('project_count_limit', 0)  # 默认为10个项目
        
    # 判断是否超出限制
    return project_count >= project_count_limit

#用户购买积分逻辑
async def handle_purchase_credits(user_id, recharge_credits, current_time):
    """
    使用分布式锁确保积分购买的原子性和并发安全
    用户购买积分
    """
    max_wait_time = 60  # 最大等待时间（秒）
    check_interval = 0.5  # 检查间隔（秒）
    start_time = time.time()
    
    while time.time() - start_time < max_wait_time:
        lock_current_time = time.time()
        lock_timeout = lock_current_time - 30 #30秒锁超时
        
        # 尝试获取锁
        lock_result = await mongo_instance.update_one(
            "user_benefits_locks",
            {
                "user_id": user_id,
                "$or": [
                    {"locked_at": {"$exists": False}},
                    {"locked_at": {"$lt": lock_timeout}}
                ]
            },
            {
                "$set": {
                    "user_id": user_id,
                    "locked_at": lock_current_time,
                    "process_id": f"{time.time()}_{id(object())}",
                    "operation": "handle_purchase_credits"
                }
            },
            upsert=True
        )
        
        if lock_result and lock_result.modified_count > 0:
            break
        else:
            # 等待后重试
            await asyncio.sleep(check_interval)
        
    if not lock_result or lock_result.modified_count == 0:
        # 获取锁失败，说明有其他进程正在处理
        logging.error(f"Critical Error for user {user_id}, when handle_purchase_credits")
    
    try:
        # 获得锁后，重新查询最新的用户信息
        user = await mongo_instance.find_one("users", {"_id": user_id})
        if not user:
            return False
            
        # 获取当前用户积分信息
        current_free_credits = user.get('free_credits', 0)
        
        # 如果 free_credits 为负数，需要特殊处理
        if current_free_credits < 0:
            # 计算需要弥补的负债金额
            debt_amount = abs(current_free_credits)
            # free_credits 弥补到0，最多弥补debt_amount
            free_credits_compensation = min(recharge_credits, debt_amount)
            # 剩余的充值积分加到purchase_credits
            remaining_credits = recharge_credits - free_credits_compensation
            
            update_result = await mongo_instance.update_one(
                "users",
                {"_id": user_id},
                {
                    "$inc": {
                        "free_credits": free_credits_compensation,
                        "purchase_credits": remaining_credits
                    },
                    "$set": {
                        "is_first_recharge": False,
                        "last_updated_at": current_time
                    }
                }
            )
        else:
            # free_credits 不为负数时，按原逻辑处理
            update_result = await mongo_instance.update_one(
                "users",
                {"_id": user_id},
                {
                    "$inc": {"purchase_credits": recharge_credits},
                    "$set": {
                        "is_first_recharge": False,
                        "last_updated_at": current_time
                    }
                }
            )
        
        # 如果更新成功，记录积分获取历史
        if update_result.modified_count > 0:
            await mongo_instance.update_one(
                "user_transactions",
                {"user_id": user_id},
                {
                    "$push": {
                        "credits_obtained_history": {
                            "obtained_time": current_time,
                            "credits_type": "purchase_credits",
                            "obtained_credits": recharge_credits
                        }
                    },
                    "$set": {"last_updated_at": current_time}
                }
            )
            return True
        
        return False
        
    finally:
        # 释放锁
        await mongo_instance.delete_one(
            "user_benefits_locks",
            {"user_id": user_id}
        )   

#用户订阅会员
import time

async def handle_subscribe_membership(user_id, membership_level, stripe_id, current_time):
    """
    使用分布式锁确保会员订阅的原子性和并发安全
    用户订阅会员
    """
    max_wait_time = 60  # 最大等待时间（秒）
    check_interval = 0.5  # 检查间隔（秒）
    start_time = time.time()
    
    while time.time() - start_time < max_wait_time:
        lock_current_time = time.time()
        lock_timeout = lock_current_time - 30 #30秒锁超时
        
        # 尝试获取锁
        lock_result = await mongo_instance.update_one(
            "user_benefits_locks",
            {
                "user_id": user_id,
                "$or": [
                    {"locked_at": {"$exists": False}},
                    {"locked_at": {"$lt": lock_timeout}}
                ]
            },
            {
                "$set": {
                    "user_id": user_id,
                    "locked_at": lock_current_time,
                    "process_id": f"{time.time()}_{id(object())}",
                    "operation": "handle_subscribe_membership"
                }
            },
            upsert=True
        )
        
        if lock_result and lock_result.modified_count > 0:
            break
        else:
            # 等待后重试
            await asyncio.sleep(check_interval)
        
    if not lock_result or lock_result.modified_count == 0:
        # 获取锁失败，说明有其他进程正在处理
        logging.error(f"Critical Error for user {user_id}, when handle_subscribe_membership")
    
    try:
        # 获得锁后，重新查询最新的用户信息
        user = await mongo_instance.find_one("users", {"_id": user_id})
        if not user:
            return None
            
        membership_items = get_membership_benefit_item()
        plan_info = membership_items[membership_level]
        
        # 获取会员权益
        item_benefit = plan_info["benefit"]
        month_count = item_benefit.get("month_count", 1)
        # 计算会员到期时间
        expire_time = mongo_instance.calculate_membership_expire_time(current_time, month_count)
        
        membership_credits_amount = item_benefit.get("membership_credits", 0)
        project_count_limit = item_benefit.get("project_count", 10)
        
        # 获取当前用户积分信息
        current_free_credits = user.get('free_credits', 0)
        
        # 如果 free_credits 为负数，需要特殊处理
        if current_free_credits < 0:
            # 计算需要弥补的负债金额
            debt_amount = abs(current_free_credits)
            # free_credits 弥补到0，最多弥补debt_amount
            free_credits_compensation = min(membership_credits_amount, debt_amount)
            # 剩余的会员积分加到membership_credits
            remaining_credits = membership_credits_amount - free_credits_compensation
            
            # 更新用户会员信息
            update_result = await mongo_instance.update_one(
                "users",
                {"_id": user_id},
                {
                    "$inc": {
                        "free_credits": free_credits_compensation,
                        "membership_credits": remaining_credits
                    },
                    "$set": {
                        "stripe_subscription_id": stripe_id,
                        "membership_level": membership_level,
                        "membership_expires_at": expire_time,
                        "membership_created_at": current_time,
                        "membership_next_month_update_at": mongo_instance.calculate_next_update_time(current_time, current_time),
                        "project_count_limit": project_count_limit,
                        "last_updated_at": current_time
                    }
                }
            )
        else:
            # free_credits 不为负数时，按原逻辑处理
            update_result = await mongo_instance.update_one(
                "users",
                {"_id": user_id},
                {
                    "$set": {
                        "stripe_subscription_id": stripe_id,
                        "membership_level": membership_level,
                        "membership_expires_at": expire_time,
                        "membership_created_at": current_time,
                        "membership_next_month_update_at": mongo_instance.calculate_next_update_time(current_time, current_time),
                        "project_count_limit": project_count_limit,
                        "last_updated_at": current_time
                    },
                    "$inc": {
                        "membership_credits": membership_credits_amount
                    }
                }
            )
        
        # 如果更新成功，记录会员积分获取历史
        if update_result.modified_count > 0 and membership_credits_amount > 0:
            await mongo_instance.update_one(
                "user_transactions",
                {"user_id": user_id},
                {
                    "$push": {
                        "credits_obtained_history": {
                            "obtained_time": current_time,
                            "credits_type": "membership_credits",
                            "obtained_credits": membership_credits_amount
                        }
                    },
                    "$set": {"last_updated_at": current_time}
                }
            )
        
        return expire_time if update_result.modified_count > 0 else None
        
    finally:
        # 释放锁
        await mongo_instance.delete_one(
            "user_benefits_locks",
            {"user_id": user_id}
        )

#计算用户当前积分
async def calculate_user_credits(user_id):
    """
    计算用户当前积分
    """
    user = await mongo_instance.find_one("users", {"_id": user_id})
    free_credits = user.get('free_credits', 0)
    membership_credits = user.get('membership_credits', 0)
    purchase_credits = user.get('purchase_credits', 0)

    return free_credits + membership_credits + purchase_credits

#判断用户当前是否有积分
async def is_user_has_credits(user_id):
    """
    判断用户当前是否有积分
    """
    user = await mongo_instance.find_one("users", {"_id": user_id})
    free_credits = user.get('free_credits', 0)
    membership_credits = user.get('membership_credits', 0)
    purchase_credits = user.get('purchase_credits', 0)
    return free_credits + membership_credits + purchase_credits > 0

#获取用户拥有的积分详情
async def get_user_credits_record(user_id):
    """
    获取用户当前积分信息
    """
    user = await mongo_instance.find_one("users", {"_id": user_id})
    free_credits = user.get('free_credits', 0)
    membership_credits = user.get('membership_credits', 0)
    purchase_credits = user.get('purchase_credits', 0)
    return {
        "free_credits": free_credits,
        "membership_credits": membership_credits,
        "purchase_credits": purchase_credits,
        "total_credits": free_credits + membership_credits + purchase_credits
    }

#扣除积分并记录使用渠道
import time

async def deduct_user_credits(used_channel, user_id, used_type, used_token, used_credits) -> bool:
    """
    使用分布式锁确保积分扣除的原子性和并发安全
    扣除积分并记录使用历史
    1. 如果total_credits <= 0，返回False
    2. 如果足够扣除，按照free_credits -> membership_credits -> purchase_credits顺序依次扣除
    3. 如果不足够扣除，按照membership_credits -> purchase_credits -> free_credits顺序扣除，确保free_credits只有一条扣除记录
    """
    max_wait_time = 60  # 最大等待时间（秒）
    check_interval = 0.5  # 检查间隔（秒）
    start_time = time.time()
    
    while time.time() - start_time < max_wait_time:
        lock_current_time = time.time()
        lock_timeout = lock_current_time - 30 #30秒锁超时
        
        # 尝试获取锁
        lock_result = await mongo_instance.update_one(
            "user_benefits_locks",
            {
                "user_id": user_id,
                "$or": [
                    {"locked_at": {"$exists": False}},
                    {"locked_at": {"$lt": lock_timeout}}
                ]
            },
            {
                "$set": {
                    "user_id": user_id,
                    "locked_at": lock_current_time,
                    "process_id": f"{time.time()}_{id(object())}",
                    "operation": "deduct_user_credits"
                }
            },
            upsert=True
        )
        
        if lock_result and lock_result.modified_count > 0:
            break
        else:
            # 等待后重试
            await asyncio.sleep(check_interval)
        
    if not lock_result or lock_result.modified_count == 0:
        # 获取锁失败，说明有其他进程正在处理
        logging.error(f"Critical Error for user {user_id}, when deduct_user_credits")
            
    try:

        current_time, _, _ = mongo_instance.get_current_time()
        
        # 获得锁后，重新查询最新的用户积分
        user = await mongo_instance.find_one("users", {"_id": user_id})
        if not user:
            return False
            
        free_credits = user.get('free_credits', 0)
        membership_credits = user.get('membership_credits', 0)
        purchase_credits = user.get('purchase_credits', 0)
        total_credits = free_credits + membership_credits + purchase_credits
        
        # 如果总积分小于等于零，返回False
        if total_credits <= 0:
            return False
        
        # 计算各类积分的扣除量
        remaining_amount = used_credits
        free_deduct = 0
        membership_deduct = 0
        purchase_deduct = 0
        usage_records = []
        
        # 积分扣除策略计算
        if total_credits >= used_credits:
            # 足够扣除：free_credits -> membership_credits -> purchase_credits
            if remaining_amount > 0 and free_credits > 0:
                free_deduct = min(remaining_amount, free_credits)
                remaining_amount -= free_deduct
                if free_deduct > 0:
                    usage_records.append({
                        "used_time": current_time,
                        "credits_type": "free_credits",
                        "used_channel": used_channel,
                        "used_type": used_type,
                        "used_credits": free_deduct,
                        "used_token": used_token
                    })
            
            if remaining_amount > 0 and membership_credits > 0:
                membership_deduct = min(remaining_amount, membership_credits)
                remaining_amount -= membership_deduct
                if membership_deduct > 0:
                    usage_records.append({
                        "used_time": current_time,
                        "credits_type": "membership_credits",
                        "used_channel": used_channel,
                        "used_type": used_type,
                        "used_credits": membership_deduct,
                        "used_token": used_token
                    })
            
            if remaining_amount > 0 and purchase_credits > 0:
                purchase_deduct = min(remaining_amount, purchase_credits)
                remaining_amount -= purchase_deduct
                if purchase_deduct > 0:
                    usage_records.append({
                        "used_time": current_time,
                        "credits_type": "purchase_credits",
                        "used_channel": used_channel,
                        "used_type": used_type,
                        "used_credits": purchase_deduct,
                        "used_token": used_token
                    })
        else:
            # 不足扣除：membership_credits -> purchase_credits -> free_credits
            if remaining_amount > 0 and membership_credits > 0:
                membership_deduct = min(remaining_amount, membership_credits)
                remaining_amount -= membership_deduct
                if membership_deduct > 0:
                    usage_records.append({
                        "used_time": current_time,
                        "credits_type": "membership_credits",
                        "used_channel": used_channel,
                        "used_type": used_type,
                        "used_credits": membership_deduct,
                        "used_token": used_token
                    })
            
            if remaining_amount > 0 and purchase_credits > 0:
                purchase_deduct = min(remaining_amount, purchase_credits)
                remaining_amount -= purchase_deduct
                if purchase_deduct > 0:
                    usage_records.append({
                        "used_time": current_time,
                        "credits_type": "purchase_credits",
                        "used_channel": used_channel,
                        "used_type": used_type,
                        "used_credits": purchase_deduct,
                        "used_token": used_token
                    })
            
            # 剩余部分从 free_credits 扣除（可以为负数）
            if remaining_amount > 0:
                free_deduct = remaining_amount
                usage_records.append({
                    "used_time": current_time,
                    "credits_type": "free_credits",
                    "used_channel": used_channel,
                    "used_type": used_type,
                    "used_credits": free_deduct,
                    "used_token": used_token
                })
        
        # 使用原子操作更新积分
        update_result = await mongo_instance.update_one(
            "users",
            {"_id": user_id},
            {
                "$inc": {
                    "free_credits": -free_deduct,  # 负数表示减少
                    "membership_credits": -membership_deduct,
                    "purchase_credits": -purchase_deduct
                },
                "$set": {
                    "last_updated_at": current_time
                }
            }
        )
        
        # 如果更新成功，记录交易历史
        if update_result.modified_count > 0:
            # 更新交易记录
            user_transaction = await mongo_instance.find_one("user_transactions", {"user_id": user_id})
            
            if user_transaction:
                await mongo_instance.update_one(
                    "user_transactions",
                    {"user_id": user_id},
                    {
                        "$inc": {"used_credits": used_credits},
                        "$set": {"last_updated_at": current_time},
                        "$push": {"credits_used_history": {"$each": usage_records}}
                    }
                )
            
            return True
        
        return False
        
    finally:
        # 释放锁
        await mongo_instance.delete_one(
            "user_benefits_locks",
            {"user_id": user_id}
        )
        

