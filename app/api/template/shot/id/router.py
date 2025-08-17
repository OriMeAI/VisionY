from fastapi import APIRouter
from fastapi.responses import JSONResponse
from app.locales.translations import get_project_shot_item
from app.utils.mongo import mongo_instance
import logging
from app.locales.translations import get_translation

id_router = APIRouter()

@id_router.get('/{id}')
async def operator(id: str):
    # 先从数据库获取项目的所有分镜信息
    project_id = mongo_instance.generate_object_id(id)
    
    # 查询项目信息，获取shots_ids
    project = await mongo_instance.find_one(
        "projects",
        {
            "_id": project_id,
            "status": "active"
        }
    )
    
    shots_data = []
    
    if project and project.get("shot_ids"):
        
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

                
        # 遍历项目中的所有分镜ID
        for shot_id in project.get("shot_ids", []):
            shot = await mongo_instance.find_one(
                "shots",
                {
                    "_id": shot_id,
                    "status": "active"
                }
            )
            
            if not shot:
                continue
            
            shot_resource = await mongo_instance.find_one(
                "shot_resources",
                {"_id": shot.get("selected_shot_resource_id", "")}
            )
                
            # 构建分镜数据
            # 构建分镜数据
            shot_item = {}
            
            # 设置基本信息
            shot_item["shot_id"] = str(shot["_id"])
            
            # 设置镜头资源信息 - 添加空值检查
            if shot_resource:
                shot_item["shot_resource"] = {
                    "shot_resource_url": shot_resource.get("resource_url", ""),
                    "is_HD": shot_resource.get("is_HD", False),
                    "shot_resource_id": str(shot.get("selected_shot_resource_id", ""))
                }
            else:
                shot_item["shot_resource"] = {
                    "shot_resource_url": "",
                    "is_HD": False,
                    "shot_resource_id": ""
                }
            
            # 设置场景描述
            shot_item["scene_description"] = {
                "background": shot.get("background", ""),
                "characters": [{
                    "role_id": str(role["role_id"]),
                    "role_name": roles_info.get(str(role["role_id"]), {}).get("role_name", ""),
                    "action_and_emotion": role.get("action_and_emotion", "")
                } for role in shot.get("selected_roles", [])]
            }
            
            # 设置台词信息
            shot_item["dialogues"] = [{
                "role_id": str(dialogue["role_id"]),
                "content": dialogue.get("content", ""),
                "role_name": get_translation("voiceover") if str(dialogue["role_id"]) == "voiceover" else roles_info.get(str(dialogue["role_id"]), {}).get("role_name", "")
            } for dialogue in shot.get("dialogues", [])]
            
            # 获取角色信息
            shot_item["main_characters"] = [{
                "role_id": str(role["role_id"]),
                "role_name": roles_info.get(str(role["role_id"]), {}).get("role_name", ""),
                "role_resource_url": roles_info.get(str(role["role_id"]), {}).get("role_resource_url", "")
            } for role in shot.get("selected_roles", [])]
            
            # 获取翻译值
            size_values = get_translation("size_values")
            angle_values = get_translation("angle_values")
            type_values = get_translation("type_values")
            
            # 构建镜头参数对象
            shot_size = shot.get("shot_size", 1)
            camera_angle = shot.get("camera_angle", 0)
            shot_type = shot.get("shot_type", 0)
            
            shot_item["shot_size"] = {
                "value": size_values[shot_size],
                "size_values": size_values
            }
            
            shot_item["camera_angle"] = {
                "value": angle_values[camera_angle],
                "angle_values": angle_values
            }
            
            shot_item["shot_type"] = {
                "value": type_values[shot_type],
                "type_values": type_values
            }
            
            shot_item["shot_time"] = {
                "value": shot.get("shot_time", 3),
                "time_scale": get_translation("second"),
            }
            
            shots_data.append(shot_item)
    
    if shots_data:
        return JSONResponse(content={
            "code": 0,
            "data": shots_data,
            "msg": ""
        })
    else:
        # 如果数据库中没有，从模板获取
        items = get_project_shot_item(id)
        
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