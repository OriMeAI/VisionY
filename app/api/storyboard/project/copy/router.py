from fastapi import APIRouter, Query
from fastapi.responses import JSONResponse
from app.collections.project import copy_project_from_db
from app.utils.mongo import mongo_instance
from app.utils.core import get_user_id
from app.locales.translations import get_translation

copy_router = APIRouter()

@copy_router.post('/copy')
async def operator(projectId: str = Query(...)):
    """
    复制一个已有的项目
    
    Args:
        projectId: 要复制的项目ID
        current_user: 当前登录用户信息
        
    Returns:
        JSONResponse: 包含新项目ID的响应
    """
    user_id = get_user_id()
    project_id = mongo_instance.generate_object_id(projectId)
    
    
    # 检查用户的项目数量是否超过限制
    user = await mongo_instance.find_one("users", {"_id": user_id})
    total_count = user.get("project_count_limit", 0)
    
    used_count = await mongo_instance.count("projects", {
        "user_id": user_id,
        "status": "active"
    })
    
    if used_count >= total_count:
        return JSONResponse(content={
            "code": 1,
            "data": None,
            "msg": get_translation("paypal_purchase_credits_description").format(total_count=total_count)
        })
    
    # 调用复制项目的函数
    new_project_id, new_project_name = await copy_project_from_db(user_id, project_id)
    
    if new_project_id:
        return JSONResponse(content={
            "code": 0,
            "data": {
                "projectId": str(new_project_id),
                "projectName": new_project_name,
            },
            "msg": get_translation("copy_project_success")
        })
    else:
        return JSONResponse(content={
            "code": 1,
            "data": None,
            "msg": get_translation("copy_project_failed")
        })