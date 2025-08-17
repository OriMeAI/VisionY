from fastapi import APIRouter, Body
from fastapi.responses import JSONResponse
from app.utils.mongo import mongo_instance
from app.locales.translations import get_translation
from app.utils.core import get_user_id

copy_router = APIRouter()

@copy_router.post('/copy')
async def operator(
    projectId: str = Body(...),
    roleId: str = Body(...),
):
    # 获取当前用户ID
    user_id = get_user_id()
    
    # 转换为ObjectId
    project_id = mongo_instance.generate_object_id(projectId)
    role_id = mongo_instance.generate_object_id(roleId)
    
    # 查询原始角色
    original_role = await mongo_instance.find_one(
        "roles",
        {
            "_id": role_id,
            "user_id": user_id,
            "status": "active"
        }
    )
    
    if not original_role:
        return JSONResponse(content={
            "code": 1,
            "data": None,
            "msg": get_translation("role_not_exist_or_no_right"),
        })
    
    # 获取选中的资源ID
    selected_resource_id = original_role.get("selected_role_resource_id")
        
    # 查询选中的资源
    selected_resource = await mongo_instance.find_one(
        "role_resources",
        {
            "_id": selected_resource_id
        }
    )
    
    if not selected_resource:
        return JSONResponse(content={
            "code": 1,
            "data": None,
            "msg": get_translation("role_has_no_resource"),
        })
    
    # 获取当前时间
    current_time, beijing_formatted_time, _ = mongo_instance.get_current_time()
    
    # 先创建新角色ID
    new_role_id = mongo_instance.generate_object_id()
    
    # 获取原始角色的所有资源ID
    original_resource_ids = original_role.get("role_resource_ids", [])
    
    # 创建新的资源ID映射表和新资源ID列表
    resource_id_map = {}
    new_resource_ids = []
    
    # 复制所有角色资源
    for original_resource_id in original_resource_ids:
        # 查询原始资源
        original_resource = await mongo_instance.find_one(
            "role_resources",
            {
                "_id": original_resource_id
            }
        )
        
        if not original_resource:
            continue
        
        # 创建新的资源ID
        new_resource_id = mongo_instance.generate_object_id()
        
        # 记录ID映射关系
        resource_id_map[str(original_resource_id)] = new_resource_id
        new_resource_ids.append(new_resource_id)
        
        # 复制资源数据
        new_resource = original_resource.copy()
        new_resource.update({
            "_id": new_resource_id,
            "user_id": user_id,
            "project_id": project_id,
            "role_id": new_role_id,  # 使用新创建的角色ID
            "created_at": current_time,
            "last_updated_at": current_time,
            "created_at_str": beijing_formatted_time
        })
        
        # 插入新资源
        await mongo_instance.insert_one("role_resources", new_resource)
    
    # 角色名称
    role_name = original_role.get("role_name", "") + "_copy"
    
    # 复制原始角色的所有字段
    new_role = original_role.copy()
    
    # 确定新的选中资源ID
    new_selected_resource_id = resource_id_map.get(str(selected_resource_id))
    
    # 更新新角色的必要字段
    new_role.update({
        "_id": new_role_id,
        "user_id": user_id,
        "project_id": project_id,
        "status": "active",
        "role_name": role_name,
        "selected_role_resource_id": new_selected_resource_id,  # 使用新资源ID
        "role_resource_ids": new_resource_ids,  # 使用所有新资源ID
        "created_at": current_time,
        "created_at_str": beijing_formatted_time,
        "last_updated_at": current_time
    })
    
    # 插入新角色
    await mongo_instance.insert_one("roles", new_role)
    
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
    
    # 获取选中资源的信息用于返回
    selected_new_resource = await mongo_instance.find_one(
        "role_resources",
        {
            "_id": new_selected_resource_id
        }
    )
    
    # 返回结果
    return JSONResponse(content={
        "code": 0,
        "data": {
            "roleId": str(new_role_id),
            "projectId": projectId,
            "figureDesc": selected_new_resource.get("description", ""),
            "figureName": new_role.get("role_name", ""),
            "url": selected_new_resource.get("resource_url", ""),
        },
        "msg": get_translation("role_copy_success"),
    })