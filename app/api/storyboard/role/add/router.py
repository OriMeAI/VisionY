from fastapi import APIRouter, Body
from fastapi.responses import JSONResponse
from app.utils.mongo import mongo_instance
from app.utils.core import get_user_id
import random
from app.locales.translations import get_translation
from app.models.model_factory import create_image_model

add_router = APIRouter()

@add_router.post('/add')
async def operator( projectId: str = Body(..., embed=True) ):
    # 获取当前用户ID
    user_id = get_user_id()
    
    # 转换为ObjectId
    project_id = mongo_instance.generate_object_id(projectId)
    
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
        
    # 检查是否有未选择资源的角色
    role_ids = project.get("role_ids", [])
    if role_ids:
        for role_id in role_ids:
            role = await mongo_instance.find_one(
                "roles",
                {
                    "_id": role_id,
                    "user_id": user_id,
                    "project_id": project_id,
                    "status": "active"
                }
            )
            
            if role and role.get("selected_role_resource_id"):
                # 获取角色选中的资源
                resource = await mongo_instance.find_one(
                    "role_resources",
                    {
                        "_id": role.get("selected_role_resource_id")
                    }
                )
                
                # 检查资源是否存在且URL是否为空
                if not resource or not resource.get("resource_url"):
                    return JSONResponse(content={
                        "code": 1,
                        "data": None,
                        "msg": get_translation("exist_incomplete_role"),
                    })
            elif role:
                # 如果角色没有选中的资源ID
                return JSONResponse(content={
                    "code": 1,
                    "data": None,
                    "msg": get_translation("exist_incomplete_role"),
                })
    
    # 获取当前时间
    current_time, beijing_formatted_time, _ = mongo_instance.get_current_time()
    
    # 创建新角色ID
    new_role_id = mongo_instance.generate_object_id()
    
    # 创建新资源ID
    new_resource_id = mongo_instance.generate_object_id()
    
    # 查询项目中已有的角色数量，用于生成角色名称
    role_count = await mongo_instance.count(
        "roles",
        {
            "project_id": project_id,
            "user_id": user_id,
            "status": "active"
        }
    )
    
    role_name = f"new_role_{role_count + 1}"
    
    # 生成随机种子
    generate_seed = random.randint(100000, 999999)
    
    image_model_name = project.get("image_model_name", "")
    
    image_model = create_image_model(image_model_name)
    
    # 创建空的角色资源
    new_resource = {
        "_id": new_resource_id,
        "user_id": user_id,
        "project_id": project_id,
        "role_id": new_role_id,
        "description": get_translation("default_role_description"),
        "description_en": "",
        "image_model_name": image_model_name,
        "style_type": project.get("style_type", ""),
        "style_type_desc": project.get("style_type_desc", ""),
        "image_size": image_model.get_role_image_size(),
        "generate_seed": project.get("generate_seed", generate_seed),
        "generate_id": "",
        "generate_status": "",
        "resource_url": "",
        "resource_prompt": "",
        "voice_model_name": "",
        "face_image": "",
        "projection_image": [],
        "created_at": current_time,
        "last_updated_at": current_time,
        "created_at_str": beijing_formatted_time
    }
    
    # 插入新资源
    await mongo_instance.insert_one("role_resources", new_resource)
    
    # 创建新角色
    new_role = {
        "_id": new_role_id,
        "user_id": user_id,
        "project_id": project_id,
        "role_name": role_name,
        "selected_role_resource_id": new_resource_id,
        "status": "active",
        "role_resource_ids": [new_resource_id],
        "created_at": current_time,
        "last_updated_at": current_time,
        "created_at_str": beijing_formatted_time
    }
    
    # 插入新角色
    await mongo_instance.insert_one("roles", new_role)
    
    # 更新项目的最后更新时间
    await mongo_instance.update_one(
        "projects",
        {"_id": project_id},
        {
            "$set": {"last_updated_at": current_time},
            "$push": { 
                    "role_ids": {
                        "$each": [new_role_id],
                        "$position": 0  # 将新ID插入到数组的开头位置
                    }
                }
        }
    )
    
    # 返回结果
    return JSONResponse(content={
        "code": 0,
        "data": {
            "roleId": str(new_role_id),
            "projectId": str(project_id),
            "figureDesc": new_resource["description"],
            "figureName": role_name,
            "url": "",
        },
        "msg": "",
    })