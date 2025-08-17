from fastapi import APIRouter, Body
from fastapi.responses import JSONResponse
from app.utils.mongo import mongo_instance
from app.utils.core import get_user_id
from app.locales.translations import get_translation
import logging
from typing import Dict, Any, Optional, Union, List

update_router = APIRouter()

@update_router.post('/update')
async def operator(
    projectId: str = Body(...),
    storyboardId: str = Body(...),
    updateType: str = Body(...),
    data: Union[Dict[str, Any], List[Dict[str, Any]]] = Body(...)
):
    """
    更新镜头信息
    
    Args:
        projectId: 项目ID
        storyboardId: 镜头ID
        updateType: 更新类型，如 scene_description, dialogues 等
        data: 更新的数据
        
    Returns:
        JSONResponse: 更新结果
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
    
    # 验证镜头存在
    shot = await mongo_instance.find_one(
        "shots",
        {
            "_id": shot_id,
            "status": "active"
        }
    )
    
    if not shot:
        return JSONResponse(content={
            "code": 1,
            "data": None,
            "msg": get_translation("shot_not_found"),
        })
        
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
                
    # 获取当前时间
    current_time, _, _ = mongo_instance.get_current_time()
    
    # 根据更新类型处理不同的更新操作
    update_data = {"last_updated_at": current_time}
    
    if updateType == "scene_description":
        # 更新场景描述
        update_data["background"] = data.get("background", "")
                
        # 生成场景图的时间，如果该值为空。那么调用翻译模型。这里调用太慢了。。。。
        update_data["background_en"] = ""
        
        selected_roles = shot.get("selected_roles", [])
        
        # 如果有角色信息，也一并更新
        if "characters" in data:
            for character in data["characters"]:
                role_id = mongo_instance.generate_object_id(character.get("role_id", ""))
                if role_id:
                    # 只更新已存在的角色信息
                    for existing_role in selected_roles:
                        if existing_role.get("role_id") == role_id:
                            # 更新已存在的角色信息
                            existing_role["action_and_emotion"] = character.get("action_and_emotion", "")
                            
                            #生成场景图的时间，如果该值为空。那么调用翻译模型。这里调用太慢了。。。。
                            existing_role["action_and_emotion_en"] = ""                            
                            break
                                
        update_data["selected_roles"] = selected_roles
        
    elif updateType == "main_characters":
        # 获取当前镜头的selected_roles和dialogues
        current_selected_roles = shot.get("selected_roles", [])
        current_dialogues = shot.get("dialogues", [])
        
        # 创建角色ID到角色信息的映射，方便快速查找
        current_role_map = {str(role.get("role_id")): role for role in current_selected_roles}
        
        # 处理新的角色列表
        new_selected_roles = []
        new_role_ids = set()
                
        for character in data:
            role_id_str = character.get("role_id", "")
            if not role_id_str:
                continue
            
            new_role_ids.add(role_id_str)
                
            role_id = mongo_instance.generate_object_id(role_id_str)
                        
            # 构建角色信息
            role_info = {
                "role_id": role_id,
                "action_and_emotion": "",
                "action_and_emotion_en": ""
            }
            
            # 如果角色已存在，保留原有信息并添加到已有角色列表
            if role_id_str in current_role_map:
                existing_role = current_role_map[role_id_str]
                role_info["action_and_emotion"] = existing_role.get("action_and_emotion", "")
                role_info["action_and_emotion_en"] = existing_role.get("action_and_emotion_en", "")
                new_selected_roles.append(role_info)
            else:
                # 新增角色添加到新角色列表
                new_selected_roles.append(role_info)
                
        # 更新selected_roles
        update_data["selected_roles"] = new_selected_roles
        
        # 处理dialogues
        # 1. 创建一个新的台词列表，始终以旁白开始
        new_dialogues = []
        
        # 2. 查找现有旁白台词或创建新的
        voiceover_dialogue = {"role_id": "voiceover", "content": ""}
        
        # 3. 创建角色ID到台词的映射
        dialogue_map = {}
        
        for dialogue in current_dialogues:
            role_id = dialogue.get("role_id", "")
            if role_id == "voiceover":
                voiceover_dialogue = dialogue
            elif role_id in new_role_ids:
                dialogue_map[role_id] = dialogue
        
        # 4. 添加旁白台词（始终在第一位）
        new_dialogues.append(voiceover_dialogue)
                
        for role_id in new_role_ids:
            if role_id in dialogue_map:
                # 已有台词的角色
                new_dialogues.append(dialogue_map[role_id])
            else:
                # 新增角色，添加空台词
                new_dialogues.append({
                    "role_id": role_id,
                    "content": ""
                })
                
        # 更新dialogues
        update_data["dialogues"] = new_dialogues

    elif updateType == "dialogues":
        # 更新台词
        dialogues = []
        
        # 确保旁白台词始终在第一位
        voiceover_dialogue = None
        other_dialogues = []
        
        for dialogue in data:
            dialogue_item = {
                "role_id": dialogue.get("role_id", ""),
                "content": dialogue.get("content", "")
            }
            
            # 区分旁白和其他角色台词
            if dialogue_item["role_id"] == "voiceover":
                voiceover_dialogue = dialogue_item
            else:
                other_dialogues.append(dialogue_item)
        
        # 如果没有旁白台词，创建一个空的
        if not voiceover_dialogue:
            voiceover_dialogue = {
                "role_id": "voiceover",
                "content": ""
            }
        
        # 先添加旁白台词，再添加其他角色台词
        dialogues.append(voiceover_dialogue)
        dialogues.extend(other_dialogues)
        
        update_data["dialogues"] = dialogues
        
    elif updateType == "shot_size":
        value_index = data.get("value_index", 1)
        update_data["shot_size"] = value_index

    elif updateType == "camera_angle":
        value_index = data.get("value_index", 0)
        update_data["camera_angle"] = value_index
        
    elif updateType == "shot_type":
        value_index = data.get("value_index", 0)
        update_data["shot_type"] = value_index
        
    elif updateType == "shot_time":
        # 确保时间值是数字类型
        try:
            time_value = int(data.get("value", "3"))
        except (ValueError, TypeError):
            # 如果转换失败，使用默认值
            time_value = 3
        update_data["shot_time"] = time_value
        
    # 更新镜头信息
    await mongo_instance.update_one(
        "shots",
        {"_id": shot_id},
        {"$set": update_data}
    )
    
    # 更新项目
    await mongo_instance.update_one(
        "projects",
        {"_id": project_id},
        {
            "$set": {
                "last_updated_at": current_time
            }
        }
    )
    
    #最后返回一条完整的信息给前端
    # 更新项目
    await mongo_instance.update_one(
        "projects",
        {"_id": project_id},
        {
            "$set": {
                "last_updated_at": current_time
            }
        }
    )
    
    # 获取更新后的镜头信息
    updated_shot = await mongo_instance.find_one(
        "shots",
        {
            "_id": shot_id,
            "status": "active"
        }
    )
    
    # 构建分镜数据返回给前端
    formatted_shot = {}
    
    # 设置基本信息
    formatted_shot["shot_id"] = str(updated_shot["_id"])
    
    # 设置镜头资源信息
    shot_resource = await mongo_instance.find_one(
        "shot_resources",
        {"_id": updated_shot.get("selected_shot_resource_id", "")}
    )
    
    formatted_shot["shot_resource"] = {
        "shot_resource_url": shot_resource.get("resource_url", "") if shot_resource else "",
        "is_HD": shot_resource.get("is_HD", False) if shot_resource else False,
        "shot_resource_id": str(updated_shot.get("selected_shot_resource_id", ""))
    }
    
    # 设置场景描述
    formatted_shot["scene_description"] = {
        "background": updated_shot.get("background", ""),
        "characters": [{
            "role_id": str(role["role_id"]),
            "role_name": roles_info.get(str(role["role_id"]), {}).get("role_name", ""),
            "action_and_emotion": role.get("action_and_emotion", "")
        } for role in updated_shot.get("selected_roles", [])]
    }
    
    # 设置台词信息
    formatted_shot["dialogues"] = [{
        "role_id": str(dialogue["role_id"]),
        "content": dialogue.get("content", ""),
        "role_name": get_translation("voiceover") if str(dialogue["role_id"]) == "voiceover" else roles_info.get(str(dialogue["role_id"]), {}).get("role_name", "")
    } for dialogue in updated_shot.get("dialogues", [])]
    
    # 获取角色信息
    formatted_shot["main_characters"] = [{
        "role_id": str(role["role_id"]),
        "role_name": roles_info.get(str(role["role_id"]), {}).get("role_name", ""),
        "role_resource_url": roles_info.get(str(role["role_id"]), {}).get("role_resource_url", "")
    } for role in updated_shot.get("selected_roles", [])]
    
    # 获取翻译值
    size_values = get_translation("size_values")
    angle_values = get_translation("angle_values")
    type_values = get_translation("type_values")
    
    # 构建镜头参数对象
    shot_size = updated_shot.get("shot_size", 1)
    camera_angle = updated_shot.get("camera_angle", 0)
    shot_type = updated_shot.get("shot_type", 0)
    
    formatted_shot["shot_size"] = {
        "value": size_values[shot_size],
        "size_values": size_values
    }
    
    formatted_shot["camera_angle"] = {
        "value": angle_values[camera_angle],
        "angle_values": angle_values
    }
    
    formatted_shot["shot_type"] = {
        "value": type_values[shot_type],
        "type_values": type_values
    }
    
    formatted_shot["shot_time"] = {
        "value": updated_shot.get("shot_time", 3),
        "time_scale": get_translation("second"),
    }
            
    return JSONResponse(content={
        "code": 0,
        "data": formatted_shot,
        "msg": get_translation("shot_update_success"),
    })