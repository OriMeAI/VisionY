from fastapi import APIRouter, Body
from fastapi.responses import JSONResponse
from app.utils.mongo import mongo_instance
from app.utils.core import get_user_id
from app.locales.translations import get_translation
import logging

pic_apply_router = APIRouter()

@pic_apply_router.post('/pic_apply')
async def operator(
    projectId: str = Body(...),
    storyboardId: str = Body(...),
    targetId: str = Body(...),
):
    """
    更新镜头的默认资源
    
    Args:
        projectId: 项目ID
        storyboardId: 镜头ID
        targetId: 目标资源ID（要设为默认的资源ID）
    
    Returns:
        JSONResponse: 更新结果
    """
    # 获取当前用户ID
    user_id = get_user_id()
    
    # 转换为ObjectId
    project_id = mongo_instance.generate_object_id(projectId)
    shot_id = mongo_instance.generate_object_id(storyboardId)
    target_resource_id = mongo_instance.generate_object_id(targetId)
    
    # 验证项目和镜头存在且用户有权限
    shot = await mongo_instance.find_one(
        "shots",
        {
            "_id": shot_id,
            "project_id": project_id,
            "user_id": user_id,
            "status": "active"
        }
    )
    
    if not shot:
        return JSONResponse(content={
            "code": 1,
            "data": None,
            "msg": get_translation("shot_not_found_or_no_right"),
        })
    
    # 验证目标资源存在且属于该镜头
    shot_resource = await mongo_instance.find_one(
        "shot_resources",
        {
            "_id": target_resource_id,
            "shot_id": shot_id
        }
    )
    
    if not shot_resource:
        return JSONResponse(content={
            "code": 1,
            "data": None,
            "msg": get_translation("resource_not_found"),
        })
    
    # 获取当前时间
    current_time, _, _ = mongo_instance.get_current_time()
        
    # 更新镜头的默认资源ID
    await mongo_instance.update_one(
        "shots",
        {"_id": shot_id},
        {
            "$set": {
                "selected_shot_resource_id": target_resource_id,
                "last_updated_at": current_time
            }
        }
    )
    
    # 更新项目的最后更新时间
    await mongo_instance.update_one(
        "projects",
        {"_id": project_id},
        {
            "$set": {
                "last_updated_at": current_time
            }
        }
    )
    
    return JSONResponse(content={
        "code": 0,
        "data": {
                "shot_resource_id": str(target_resource_id),
                "is_HD": shot_resource.get("is_HD",False), 
                "shot_resource_url": shot_resource.get("resource_url", ""),
            },
        "msg": get_translation("update_success"),
    })