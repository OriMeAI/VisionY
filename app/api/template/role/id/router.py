from fastapi import APIRouter
from fastapi.responses import JSONResponse
from app.locales.translations import get_project_role_item
from app.utils.mongo import mongo_instance

id_router = APIRouter()

@id_router.get('/{id}')
async def operator(id: str):    
    # 先从数据库获取项目信息
    project_id = mongo_instance.generate_object_id(id)
    project = await mongo_instance.find_one(
        "projects", 
        {
            "_id": project_id,
            "status": "active"
        }
    )
        
    if project:
        roles_data = []
        role_ids = project.get("role_ids", [])
        
        # 遍历项目中的所有角色ID
        for role_id in role_ids:
            role = await mongo_instance.find_one(
                "roles",
                {
                    "_id": role_id,
                    "status": "active"
                }
            )
            
            if not role:
                continue
                
            # 获取角色资源
            role_resource = await mongo_instance.find_one("role_resources",{"_id": role.get("selected_role_resource_id",None)})
            
            # 构建角色数据
            role_data = {
                "id": str(role["_id"]),
                "figureName": role.get("role_name", ""),
                "figureDesc": role_resource.get("description", "") ,
                "url": role_resource.get("resource_url", "")
            }
            
            roles_data.append(role_data)
    
        return JSONResponse(content={
            "code": 0,
            "data": roles_data,
            "msg": ""
        })
        
    else:
        # 如果数据库中没有，从模板获取
        items = get_project_role_item(id)
        
        if items is not None:
            return JSONResponse(content={
                "code": 0,
                "data": items,
                "msg": ""
            })
        else:
            # 如果模板中也没有，返回空列表
            return JSONResponse(content={
                "code": 0,
                "data": [],
                "msg": ""
            })