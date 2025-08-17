from fastapi import APIRouter, Body
from fastapi.responses import JSONResponse
from app.utils.core import get_user_id
from app.utils.mongo import mongo_instance
from app.locales.translations import get_translation
import logging,math,time
from datetime import datetime, timezone

#叶子节点的blueprint不加url_prefix
usage_record_router = APIRouter()

@usage_record_router.post('/usage_record')
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
        {"$unwind": "$credits_used_history"},
        # 按时间倒序排序
        {"$sort": {"credits_used_history.used_time": -1}}
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
            "used_time": "$credits_used_history.used_time",
            "credits_type": "$credits_used_history.credits_type",
            "used_channel": "$credits_used_history.used_channel",
            "used_type": "$credits_used_history.used_type",
            "used_credits": "$credits_used_history.used_credits",
            "used_token": "$credits_used_history.used_token"
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
        used_time = record.get("used_time", "")
        if used_time.tzinfo is None:
            used_time = used_time.replace(tzinfo=timezone.utc)
        used_time_str = used_time.strftime("%Y-%m-%dT%H:%M:%SZ")
        
        # 根据使用类型设置描述
        used_type = record.get("used_type", "generate_image")
        # type_desc_map = {
        #     "generate_image": get_translation("generate_image", "图片生成"),
        #     "generate_storyboard": get_translation("generate_storyboard", "分镜图片生成"),
        #     "generate_character": get_translation("generate_character", "角色图片生成"),
        #     "translate_text": get_translation("translate_text", "文本翻译"),
        #     "other": get_translation("other_usage", "其他使用")
        # }
        # type_desc = type_desc_map.get(used_type, used_type)
        
        type_desc = get_translation(used_type)
        
        # 根据积分类型设置积分来源描述
        credits_type = record.get("credits_type", "")
        # credits_type_map = {
        #     "free_credits": get_translation("free_credits", "免费积分"),
        #     "membership_credits": get_translation("membership_credits", "会员积分"),
        #     "purchase_credits": get_translation("purchase_credits", "购买积分")
        # }
        # credits_source = credits_type_map.get(credits_type, credits_type)
        credits_source = get_translation(credits_type)
        
        formatted_record = {
            "usedToken": str(record.get("used_token", "")),
            "usedTime": used_time_str,
            "typeDesc": type_desc,
            "creditsSource": credits_source,
            "quantity": record.get("used_credits", 0)
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