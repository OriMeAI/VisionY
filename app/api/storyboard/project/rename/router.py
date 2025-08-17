from fastapi import APIRouter, Depends, Body
from fastapi.responses import JSONResponse
from app.utils.core import get_user_id
from app.utils.mongo import mongo_instance
from app.locales.translations import get_translation

import logging

rename_router = APIRouter()

@rename_router.post('/rename')
async def rename_project(    
    id: str = Body(...),
    name: str = Body(...)
):
    """
    重命名项目
    
    Args:
        project_data: 包含项目ID和新名称的字典
        
    Returns:
        JSONResponse: 操作结果响应
    """
    user_id = get_user_id()
    project_id = id
    new_name = name
        
    # 获取当前时间
    current_time, _, _ = mongo_instance.get_current_time()
    
    project_id = mongo_instance.generate_object_id(project_id)
    
    # 更新项目名称
    result = await mongo_instance.update_one(
        "projects",
        {"_id": project_id, "user_id": user_id},
        {"$set": {"project_name": new_name, "last_updated_at": current_time}}
    )
    
    if result and result.modified_count > 0:
        logging.info(f"User {user_id} renamed project {project_id} to {new_name}")
        return JSONResponse(content={
            "code": 0,
            "data": None,
            "msg": get_translation("rename_project_success")
        })
    else:
        logging.warning(f"User {user_id} failed to rename project {project_id}: project not found or no permission")
        return JSONResponse(content={
            "code": 1,
            "data": None,
            "msg": get_translation("rename_project_failed")
        }, status_code=404)