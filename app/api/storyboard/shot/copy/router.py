from fastapi.responses import JSONResponse
from fastapi import APIRouter, Body
from app.utils.mongo import mongo_instance
from app.utils.core import get_user_id
from app.locales.translations import get_translation
import copy

copy_router = APIRouter()

@copy_router.post('/copy')
async def operator(
    projectId: str = Body(...),
    storyboardId: str = Body(...),
):
    """
    复制指定ID的镜头并插入到该镜头之前
        
    Args:
        projectId: 项目ID
        storyboardId: 要复制的镜头ID
            
    Returns:
        JSONResponse: 新创建的镜头信息
    """
    # 获取当前用户ID
    user_id = get_user_id()
    
    # 转换为ObjectId
    project_id = mongo_instance.generate_object_id(projectId)
    source_shot_id = mongo_instance.generate_object_id(storyboardId)
    
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
        
    shot_ids = project.get("shot_ids", [])
    if source_shot_id not in shot_ids:
        return JSONResponse(content={
            "code": 1,
            "data": None,
            "msg": get_translation("shot_not_in_project"),
        })
    
    # 获取源镜头信息
    source_shot = await mongo_instance.find_one(
        "shots",
        {
            "_id": source_shot_id,
            "status": "active"
        }
    )
    
    if not source_shot:
        return JSONResponse(content={
            "code": 1,
            "data": None,
            "msg": get_translation("shot_not_found"),
        })
    
    # 获取当前时间
    current_time, beijing_formatted_time, _ = mongo_instance.get_current_time()
    
    # 创建新镜头数据，复制源镜头的数据
    new_shot = copy.deepcopy(source_shot)
    
    new_shot_id = mongo_instance.generate_object_id()
        
    # 更新创建时间和更新时间
    new_shot["_id"] = new_shot_id
    new_shot["created_at"] = current_time
    new_shot["last_updated_at"] = current_time
    new_shot["created_at_str"] = beijing_formatted_time
    
    # 处理资源ID复制
    original_resource_ids = source_shot.get("shot_resource_ids", [])
    original_selected_resource_id = source_shot.get("selected_shot_resource_id")
    
    # 新的资源ID列表
    new_resource_ids = []
    new_selected_resource_id = None
    
    # 复制所有资源
    for original_resource_id in original_resource_ids:
        original_resource = await mongo_instance.find_one(
            "shot_resources", 
            {"_id": original_resource_id}
        )
        
        if not original_resource:
            continue
            
        # 创建新的资源ID
        new_resource_id = mongo_instance.generate_object_id()
        
        # 创建新的资源记录
        new_resource = copy.deepcopy(original_resource)
        new_resource["_id"] = new_resource_id
        new_resource["shot_id"] = new_shot_id
        new_resource["created_at"] = current_time
        new_resource["last_updated_at"] = current_time
        new_resource["created_at_str"] = beijing_formatted_time
        
        # 插入新资源记录
        await mongo_instance.insert_one("shot_resources", new_resource)
        
        # 添加到新资源ID列表
        new_resource_ids.append(new_resource_id)
        
        # 如果是选中的资源，记录新的选中资源ID
        if str(original_resource_id) == str(original_selected_resource_id):
            new_selected_resource_id = new_resource_id
    
    # 更新镜头的资源ID引用
    new_shot["shot_resource_ids"] = new_resource_ids
    
    # 如果有选中的资源，更新选中资源ID
    if new_selected_resource_id:
        new_shot["selected_shot_resource_id"] = new_selected_resource_id
    elif new_resource_ids:
        # 如果没有找到选中资源但有资源列表，使用第一个资源作为选中资源
        new_shot["selected_shot_resource_id"] = new_resource_ids[0]
    
    # 插入新镜头
    await mongo_instance.insert_one("shots", new_shot)
    
    # 更新项目的shot_ids，将新镜头ID插入到源镜头ID之前
    shot_ids = project.get("shot_ids", [])
    index = shot_ids.index(source_shot_id)
    shot_ids.insert(index, new_shot_id)
    
    # 更新项目
    await mongo_instance.update_one(
        "projects",
        {"_id": project_id},
        {
            "$set": {
                "shot_ids": shot_ids,
                "last_updated_at": current_time
            }
        }
    )
            
    # 先构建角色信息字典
    roles_info = {}
    role_ids = project.get("role_ids", [])
    for role_id in role_ids:
        # 从roles集合中获取角色名称
        role_info = await mongo_instance.find_one(
            "roles",
            {"_id": role_id, "status": "active"}
        )
        
        if role_info:
            role_name = role_info.get("role_name", "")
            role_resource_id = role_info.get("selected_role_resource_id")
            role_resource_url = ""
            
            # 从role_resources集合中获取角色资源URL
            if role_resource_id:
                role_resource = await mongo_instance.find_one(
                    "role_resources",
                    {"_id": role_resource_id}
                )
                if role_resource:
                    role_resource_url = role_resource.get("resource_url", "")
            
            # 存储角色信息
            roles_info[str(role_id)] = {
                "role_name": role_name,
                "role_resource_url": role_resource_url,
            }

    # 获取新创建的镜头的资源信息
    selected_resource = await mongo_instance.find_one(
            "shot_resources", 
            {"_id": new_selected_resource_id}
        )
        
    # 格式化返回数据，按照前端需要的格式
    formatted_shot = {
        "shot_id": str(new_shot_id),
        "shot_resource": {
            "shot_resource_url": selected_resource.get("resource_url", "") if selected_resource else "",
            "is_HD": selected_resource.get("is_HD", False) if selected_resource else False,
            "shot_resource_id": str(new_selected_resource_id)
        },
        "scene_description": {
            "background": new_shot.get("background", ""),
            "characters": []
        },
        "dialogues": [],
        "main_characters": [],
    }
    
    # 构建角色列表，使用从角色表获取的名称
    for role in new_shot.get("selected_roles", []):
        role_id = str(role.get("role_id", ""))
        role_name = roles_info.get(role_id, {}).get("role_name", ""),
        char_info = {
            "role_id": role_id,
            "role_name": role_name,
            "action_and_emotion": role.get("action_and_emotion", ""),
        }
        formatted_shot["scene_description"]["characters"].append(char_info)
    
    # 构建台词列表，使用从角色表获取的名称
    for dialogue in new_shot.get("dialogues", []):
        role_id = str(dialogue.get("role_id", ""))
        if role_id == "voiceover":
            role_name = get_translation("voiceover")
        else:
            role_name = roles_info.get(role_id, {}).get("role_name", "")
        
        dialogue_info = {
            "role_id": role_id,
            "content": dialogue.get("content", ""),
            "role_name": role_name
        }
        formatted_shot["dialogues"].append(dialogue_info)
    
    # 构建主要角色列表，使用从角色表获取的名称
    for role in new_shot.get("selected_roles", []):
        role_id = str(role.get("role_id", ""))
        role_name = roles_info.get(role_id, {}).get("role_name", "")
        role_resource_url = roles_info.get(role_id, {}).get("role_resource_url", "")
        main_char_info = {
            "role_id": role_id,
            "role_name": role_name,
            "role_resource_url": role_resource_url
        }
        formatted_shot["main_characters"].append(main_char_info)
    
    # 构建镜头参数对象
    shot_size = new_shot.get("shot_size", 1)
    camera_angle = new_shot.get("camera_angle", 0)
    shot_type = new_shot.get("shot_type", 0)
    
    size_values = get_translation("size_values")
    formatted_shot["shot_size"] = {
        "value": size_values[shot_size] if 0 <= shot_size < len(size_values) else size_values[0],
        "size_values": size_values
    }
    
    angle_values = get_translation("angle_values")
    formatted_shot["camera_angle"] = {
        "value": angle_values[camera_angle] if 0 <= camera_angle < len(angle_values) else angle_values[0],
        "angle_values": angle_values
    }
    
    type_values = get_translation("type_values")
    formatted_shot["shot_type"] = {
        "value": type_values[shot_type] if 0 <= shot_type < len(type_values) else type_values[0],
        "type_values": type_values
    }
    
    formatted_shot["shot_time"] = {
        "value": new_shot.get("shot_time", 3),
        "time_scale": get_translation("second"),
    }
    
    return JSONResponse(content={
        "code": 0,
        "data": formatted_shot,
        "msg": get_translation("copy_shot_success"),
    })