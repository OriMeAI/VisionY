from fastapi import APIRouter, Body
from fastapi.responses import JSONResponse
from app.utils.core import get_user_id
from app.utils.mongo import mongo_instance
from app.locales.translations import get_translation
import logging,math,time
from datetime import datetime, timezone

#叶子节点的blueprint不加url_prefix
obtained_record_router = APIRouter()

@obtained_record_router.post('/obtained_record')
async def operator(
    pageSize: int = Body(...),
    pageNum: int = Body(...),
):
    # 获取当前用户ID
    user_id = get_user_id()
            
    # 构建聚合管道查询使用记录
    pipeline = [
        # 匹配用户
        {"$match": {"user_id": user_id}},
        # 展开 credits_used_history 数组
        {"$unwind": "$credits_obtained_history"},
        # 按时间倒序排序
        {"$sort": {"credits_obtained_history.obtained_time": -1}}
    ]
    
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
            "obtained_time": "$credits_obtained_history.obtained_time",
            "credits_type": "$credits_obtained_history.credits_type",
            "obtained_credits": "$credits_obtained_history.obtained_credits"
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
        # 处理时间格式
        obtained_time = record.get("obtained_time", "")
        if obtained_time.tzinfo is None:
            obtained_time = obtained_time.replace(tzinfo=timezone.utc)
        obtained_time_str = obtained_time.strftime("%Y-%m-%dT%H:%M:%SZ")
        
        # 根据使用类型设置描述
        credits_type = record.get("credits_type", "")
        type_desc = get_translation(credits_type)
                
        formatted_record = {
            "obtainedTime": obtained_time_str,
            "typeDesc": type_desc,
            "quantity": record.get("obtained_credits", 0)
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