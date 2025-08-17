from fastapi import APIRouter, Body
from fastapi.responses import JSONResponse
from app.utils.mongo import mongo_instance
from app.utils.core import get_user_id
from app.locales.translations import get_translation

rename_router = APIRouter()

@rename_router.post('/rename')
async def operator(
    projectId: str = Body(...),
    roleId: str = Body(...),
    figureName: str = Body(...)
):
    """
    重命名角色
    
    Args:
        projectId: 项目ID
        roleId: 角色ID
        figureName: 新的角色名称
        
    Returns:
        JSONResponse: 操作结果
    """
    # 获取当前用户ID
    user_id = get_user_id()
    
    # 转换为ObjectId
    project_id = mongo_instance.generate_object_id(projectId)
    role_id = mongo_instance.generate_object_id(roleId)
    
    # 获取当前时间
    current_time, _, _ = mongo_instance.get_current_time()
    
    role = await mongo_instance.find_one(
        "roles",
        {
            "_id": role_id,
            "project_id": project_id,
            "user_id": user_id
        }
    )

    if not role:
        return JSONResponse(content={
            "code": 1,
            "data": None,
            "msg": get_translation("role_not_exist_or_no_right"),
        })
                
    #更新角色名称
    await mongo_instance.update_one(
        "roles",
        {
            "_id": role_id,
            "project_id": project_id,
            "user_id": user_id
        },
        {
            "$set": {
                "role_name": figureName,
                "last_updated_at": current_time
            }
        }
    )
    
    #更新工程信息
    await mongo_instance.update_one(
        "projects",
        {
            "_id": project_id,
            "user_id": user_id
        },
        {
            "$set": {
                "last_updated_at": current_time,
            }
        }
    )
    
    return JSONResponse(content={
        "code": 0,
        "data": None,
        "msg": get_translation("role_rename_success"),
    })