from fastapi import APIRouter, Body
from fastapi.responses import JSONResponse
from app.utils.mongo import mongo_instance
from app.utils.core import get_user_id
from app.locales.translations import get_translation

update_default_router = APIRouter()

@update_default_router.post('/update_default')
async def operator(
    projectId: str = Body(...),
    roleId: str = Body(...),
    targetId: str = Body(...)
):
    # 获取当前用户ID
    user_id = get_user_id()
    
    # 转换为ObjectId
    project_id = mongo_instance.generate_object_id(projectId)
    role_id = mongo_instance.generate_object_id(roleId)
    target_resource_id = mongo_instance.generate_object_id(targetId)
    
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
    
    # 验证角色存在且属于该项目
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
    
    # 验证目标资源存在且属于该角色
    role_resource = await mongo_instance.find_one(
        "role_resources",
        {
            "_id": target_resource_id,
            "role_id": role_id,
            "project_id": project_id,
            "user_id": user_id
        }
    )
    
    if not role_resource:
        return JSONResponse(content={
            "code": 1,
            "data": None,
            "msg": get_translation("resource_not_found"),  
        })
        
    role_name = role.get("role_name")
    
    # 获取当前时间
    current_time, _, _ = mongo_instance.get_current_time()
    
    # 更新角色的默认资源
    update_result = await mongo_instance.update_one(
        "roles",
        {
            "_id": role_id,
            "project_id": project_id,
            "user_id": user_id
        },
        {
            "$set": {
                "selected_role_resource_id": target_resource_id,
                "last_updated_at": current_time
            }
        }
    )
    
    if update_result.modified_count > 0:
        return JSONResponse(content={
            "code": 0,
            "data": {
                "figureName": role_name,
                "figureDesc": role_resource.get("description"),
                "roleId": str(role_id),
                "url": role_resource.get("resource_url")
            },
            "msg": get_translation("update_default_success"),
        })
    else:
        return JSONResponse(content={
            "code": 1,
            "data": None,
            "msg": get_translation("update_default_failed"),
        })