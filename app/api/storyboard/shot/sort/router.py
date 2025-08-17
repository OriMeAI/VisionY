from fastapi import APIRouter, Body
from fastapi.responses import JSONResponse
from app.utils.mongo import mongo_instance
from app.utils.core import get_user_id
from app.locales.translations import get_translation
import logging

sort_router = APIRouter()

@sort_router.post('/sort')
async def sort_shots(
    projectId: str = Body(...),
    currentId: str = Body(...),
    targetId: str = Body(...),
):
    """
    交换两个镜头的位置
    
    Args:
        projectId: 项目ID
        currentId: 当前镜头ID
        targetId: 目标镜头ID
        
    Returns:
        JSONResponse: 操作结果
    """
    # 获取当前用户ID
    user_id = get_user_id()
    
    # 转换为ObjectId
    project_id = mongo_instance.generate_object_id(projectId)
    current_id = mongo_instance.generate_object_id(currentId)
    target_id = mongo_instance.generate_object_id(targetId)
    
    # 验证项目存在且用户有权限
    project = await mongo_instance.find_one(
        "projects",
        {
            "_id": project_id,
            "user_id": user_id,
            "status": "active"
        }
    )
    
    if not project: 
        return JSONResponse(content={
            "code": 1,
            "data": None,
            "msg": get_translation("project_not_found"),
        })
    
    # 获取shot_ids数组
    shot_ids = project.get("shot_ids", [])
    
    # 查找current_id和target_id在数组中的位置
    if current_id not in shot_ids:
        return JSONResponse(content={
            "code": 1,
            "data": None,
            "msg": get_translation("no_current_shot_id"),
        })
        
    if target_id not in shot_ids:
        return JSONResponse(content={
            "code": 1,
            "data": None,
            "msg": get_translation("no_target_shot_id"),
        })
    
    current_index = shot_ids.index(current_id)
    target_index = shot_ids.index(target_id)
    
    # 交换位置
    shot_ids[current_index], shot_ids[target_index] = shot_ids[target_index], shot_ids[current_index]
    
    # 获取当前时间
    current_time, _, _ = mongo_instance.get_current_time()
     
    # 更新项目的shot_ids和最后更新时间
    await mongo_instance.update_one(
        "projects",
        {"_id": project_id},
        {
            "$set": 
            {
                "shot_ids": shot_ids,
                "last_updated_at": current_time
            },
        }
    )
    
    return JSONResponse(content={
        "code": 0,
        "data": None,
        "msg": get_translation("change_shot_success"),
    })      