from fastapi import APIRouter, Body
from fastapi.responses import JSONResponse
from app.utils.mongo import mongo_instance
from app.utils.core import get_user_id
from app.locales.translations import get_translation

list_router = APIRouter()

@list_router.post('/list')
async def operator( projectId: str = Body(..., embed=True) ):
    
    user_id = get_user_id()
    project_id = mongo_instance.generate_object_id(projectId)
    
    # 查询项目信息
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
            "code": 801,
            "data": None,
            "msg": get_translation("project_not_found"),    
        })
    
    # 获取项目中的角色ID列表
    role_ids = project.get("role_ids", [])
    
    result = []
    for role_id in role_ids:
        # 查询角色信息
        role = await mongo_instance.find_one(
            "roles",
            {
                "_id": role_id,
                "user_id": user_id,
                "status": "active"
            }
        )
        
        if not role:
            continue
        
        # 获取最新的角色资源
        role_resource = None
        if role.get("selected_role_resource_id",None):
            role_resource = await mongo_instance.find_one(
                "role_resources",
                {"_id": role["selected_role_resource_id"]}
            )
        
        if role_resource:
            result.append({
                "roleId": str(role["_id"]),
                "figureName": role.get("role_name", ""),
                "figureDesc": role_resource.get("description", ""),
                "url": role_resource.get("resource_url", ""),
            })
    
    return JSONResponse(content={
        "code": 0,
        "data": result,
        "msg": "",
    })