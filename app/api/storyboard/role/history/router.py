import select
from fastapi import APIRouter, Body
from fastapi.responses import JSONResponse
from app.utils.mongo import mongo_instance
from app.utils.core import get_user_id
from app.locales.translations import get_translation

history_router = APIRouter()

@history_router.post('/history')
async def operator(
    projectId: str = Body(...),
    roleId: str = Body(...),
):
    # 获取当前用户ID    
    user_id = get_user_id()
    
    # 转换为ObjectId
    project_id = mongo_instance.generate_object_id(projectId)
    
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
    
    #获取角色信息
    role_id = mongo_instance.generate_object_id(roleId)
    
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
        
    selected_role_resource_id = role.get("selected_role_resource_id", None)
    
    role_name = role.get("role_name", "")

    # 获取角色资源信息        
    history_resources = []
    for resource_id in role.get("role_resource_ids", []):
        role_resource = await mongo_instance.find_one("role_resources", {"_id": resource_id})
        if role_resource:
            history_resources.append({
                "id": str(role_resource["_id"]),
                "url": role_resource.get("resource_url", ""),
                "figureName": role_name,
                "figureDesc": role_resource.get("description", ""),
                "selected": selected_role_resource_id == resource_id,
                "roleId": str(role_resource.get("role_id", ""))
            })

    return JSONResponse(content={
        "code": 0,
        "data": {
            "projectId": str(project_id),
            "figures": history_resources
        },
        "msg": ""
    })
