from fastapi import APIRouter, Body
from fastapi.responses import JSONResponse
from app.utils.core import get_user_id
from app.utils.mongo import mongo_instance
from app.locales.translations import get_translation
import logging,math,time
from datetime import datetime, timezone

#叶子节点的blueprint不加url_prefix
recharge_record_router = APIRouter()

@recharge_record_router.post('/recharge_record')
async def operator(
    pageSize: int = Body(...),
    pageNum: int = Body(...),
    rechargeStatus: str = Body(...)
):
    # 获取当前用户ID
    user_id = get_user_id()
    
    # 构建聚合管道
    pipeline = [
        # 匹配用户
        {"$match": {"user_id": user_id}},
        # 展开 recharge_history 数组
        {"$unwind": "$recharge_history"},
    ]
    
    # 添加状态过滤条件（直接使用数据库状态）
    if rechargeStatus and rechargeStatus != "all":
        # 直接使用数据库中的状态：created、completed、failed、canceled、renewed
        if rechargeStatus in ["created", "completed", "failed", "canceled","subscribed", "renewed"]:
            pipeline.append({
                "$match": {"recharge_history.recharge_status": rechargeStatus}
            })
    
    # 添加排序（按时间倒序）
    pipeline.append({
        "$sort": {"recharge_history.recharge_time": -1}
    })
    
    # 添加分页前的计数
    count_pipeline = pipeline + [
        {"$count": "total"}
    ]
    
    # 添加分页
    pipeline.extend([
        {"$skip": (pageNum - 1) * pageSize},
        {"$limit": pageSize}
    ])
    
    # 投影需要的字段
    pipeline.append({
        "$project": {
            "_id": 0,
            "recharge_time": "$recharge_history.recharge_time",
            "recharge_type": "$recharge_history.recharge_type",
            "recharge_amount": "$recharge_history.recharge_amount",
            "recharge_token": "$recharge_history.recharge_token",
            "recharge_status": "$recharge_history.recharge_status",
            "recharge_credits": "$recharge_history.recharge_credits",
            "recharge_membership_level": "$recharge_history.recharge_membership_level"
        }
    })
    
    # 执行聚合查询获取数据
    records_result = await mongo_instance.aggregate("user_transactions", pipeline)
    
    # 执行聚合查询获取总数
    count_result = await mongo_instance.aggregate("user_transactions", count_pipeline)
    total_records = count_result[0]["total"] if count_result else 0
    
    # 计算总页数
    total_pages = math.ceil(total_records / pageSize) if pageSize > 0 else 0
    
    # 转换数据格式以匹配前端期望的格式
    records = []
    for record in records_result:
        # 根据充值状态设置显示文本（使用数据库原始状态）
        status_map = {
            "completed": get_translation("recharge_success"),
            "created": get_translation("recharge_pending"),
            "failed": get_translation("recharge_failed"),
            "canceled": get_translation("recharge_canceled"),
            "subscribed": get_translation("recharge_subscribed"),
            "renewed": get_translation("recharge_renewed")
        }
        
        recharge_status = record.get("recharge_status", "created")
        status_desc = status_map.get(recharge_status)
        
        # 根据充值类型设置描述
        recharge_type = record.get("recharge_type", "purchase_credits")
        if recharge_type == "membership_subscription":
            membership_level = record.get('recharge_membership_level')
            type_desc_key = f"subscription_membership_level_{membership_level}"
            type_desc = get_translation(type_desc_key)
        else:
            credits = record.get("recharge_credits", 0)
            type_desc = get_translation("purchase_some_credits").format(quantity=f"{credits:,}")
            
        # 处理 datetime 对象转换为字符串
        recharge_time = record.get("recharge_time", "")
        # 确保时间是UTC格式
        if recharge_time.tzinfo is None:
            # 如果没有时区信息，假设为UTC
            recharge_time = recharge_time.replace(tzinfo=timezone.utc)
        recharge_time_str = recharge_time.strftime("%Y-%m-%dT%H:%M:%SZ")
            
        # total_amount = "{:.2f}".format(record.get("recharge_amount", 0))
        recharge_amount = record.get("recharge_amount", 0)
        recharge_amount = float(recharge_amount) if recharge_amount else 0.0
        total_amount = "{:,.2f}".format(recharge_amount)
        total_amount_str = get_translation("total_amount").format(amount=total_amount)
        
        formatted_record = {
            "rechargeTime": recharge_time_str,
            "typeDesc": type_desc,
            "totalAmount": total_amount_str,
            "orderNo": record.get("recharge_token", ""),
            "rechargeStatus": recharge_status,
            "rechargeStatusDesc": status_desc,
        }
        records.append(formatted_record)
      
    return JSONResponse(content={
        "code": 0,
        "data": {
            "records": records,
            "total": total_records,
            "size": pageSize,
            "current": pageNum,
            "pages": total_pages
        },
        "msg": ""
    })