from fastapi import APIRouter, Body
from fastapi.responses import JSONResponse
from app.utils.mongo import mongo_instance
from app.utils.core import get_user_id
from app.locales.translations import get_translation

delete_router = APIRouter()

@delete_router.post('/delete')
async def operator(
    projectId: str = Body(...),
    storyboardId: str = Body(...),
):
    """
    删除指定ID的镜头
    
    Args:
        projectId: 项目ID
        storyboardId: 镜头ID
        
    Returns:
        JSONResponse: 操作结果
    """
    # 获取当前用户ID
    user_id = get_user_id()
    
    # 转换为ObjectId
    project_id = mongo_instance.generate_object_id(projectId)
    shot_id = mongo_instance.generate_object_id(storyboardId)
    
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
        
    # 获取当前时间
    current_time, _, _ = mongo_instance.get_current_time()
    
    # 从项目的shot_ids中移除该镜头ID
    shot_ids = project.get("shot_ids", [])
    if shot_id in shot_ids:
        shot_ids.remove(shot_id)
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
        
        # 更新shot的status和最后更新时间
        await mongo_instance.update_one(
            "shots",
            {"_id": project_id},
            {
                "$set": 
                {
                    "status": "inactive",
                    "last_updated_at": current_time
                },
            }
        )
            
    return JSONResponse(content={
        "code": 0,
        "data": None,
        "msg": get_translation("delete_shot_success"),
    })