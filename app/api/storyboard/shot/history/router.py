from fastapi import APIRouter, Body
from fastapi.responses import JSONResponse
from app.utils.mongo import mongo_instance
from app.locales.translations import get_translation
from app.utils.core import get_user_id

history_router = APIRouter()

@history_router.post('/history')
async def operator(
    projectId: str = Body(...),
    storyboardId: str = Body(...)
):
    # 从请求体中获取项目ID和镜头ID
    project_id = mongo_instance.generate_object_id(projectId)
    shot_id = mongo_instance.generate_object_id(storyboardId)
    
    user_id = get_user_id()
        
    # 查询镜头信息
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
            "data": [],
            "msg": get_translation("shot_not_found_or_no_right"),
        })
    
    # 获取镜头资源ID列表
    shot_resource_ids = shot.get("shot_resource_ids", [])
    selected_shot_resource_id = shot.get("selected_shot_resource_id")
    
    # 查询所有镜头资源
    history_resources = []
    
    for resource_id in shot_resource_ids:
        resource = await mongo_instance.find_one(
            "shot_resources",
            {"_id": resource_id}
        )
        
        if resource:
            # 判断是否为当前选中的资源
            is_selected = str(resource_id) == str(selected_shot_resource_id)
            
            history_resources.append({
                "id": str(resource_id),
                "projectId": str(project_id),
                "storyboardId": str(shot_id),
                "selected": is_selected,
                "url": resource.get("resource_url", ""),
                "is_HD": resource.get("is_HD", False),
            })
    
    return JSONResponse(content={
        "code": 0,
        "data": history_resources,
        "msg": "",
    })