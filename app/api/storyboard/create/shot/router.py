from fastapi import APIRouter, Request
from fastapi.responses import StreamingResponse, JSONResponse
from app.utils.core import get_user_id, encode_sse_data
from app.utils.mongo import mongo_instance
from app.models.model_factory import create_llm_model, create_image_model
from app.models.prompts.generate_image import get_shot_image_prompt
import json, logging, random,asyncio,time
from typing import AsyncGenerator

from app.locales.translations import get_translation

shot_router = APIRouter()

async def generate_shots_detail(user_id, project_id) -> AsyncGenerator[bytes, None]:
    try:
        """生成分镜内容的流式响应"""
        yield encode_sse_data("Connection successful")
                
        # 查询项目信息
        project = await mongo_instance.find_one("projects", {"_id": project_id, "user_id": user_id})
        if not project:
            logging.error(f"User {user_id} cannot access project {project_id}")
            yield encode_sse_data(get_translation("cannot_access_project"), event="error")
            return
        
        # 检查项目是否已经完成故事板和角色生成
        if not project.get("has_storyboard", False):
            logging.error(f"Project {project_id} does not have a storyboard yet")
            yield encode_sse_data(get_translation("please_parse_storyboard_first"), event="error")
            return
            
        if not project.get("has_role", False):
            logging.error(f"Project {project_id} does not have roles yet")
            yield encode_sse_data(get_translation("please_generate_roles_first"), event="error")
            return
        
        # 检查项目是否已经生成了分镜
        if project.get("has_shot", False):
            logging.info(f"Project {project_id} already has shots")
            yield encode_sse_data("Complete")
            return
        
        language = project.get("project_language", "zh-CN")
        
        # 获取项目脚本内容
        script_content = project.get("script_content", "")
        if not script_content:
            logging.error(f"Project {project_id} has no script content")
            yield encode_sse_data(get_translation("no_script_content_found"), event="error")
            return
        
        # 获取分镜信息
        shot_ids = project.get("shot_ids", [])
        if not shot_ids:
            logging.error(f"No shots found for project {project_id}")
            yield encode_sse_data(get_translation("no_shots_base_info_found"), event="error")
            return
        
        # 获取所有分镜基本信息
        shots = []
        for shot_id in shot_ids:
            shot = await mongo_instance.find_one("shots", {"_id": shot_id, "user_id": user_id})
            if shot:
                shots.append(shot)
        
        if not shots:
            logging.error(f"No valid shots found for project {project_id}")
            yield encode_sse_data(get_translation("no_shots_base_info_found"), event="error")
            return
                
        # 获取角色信息
        role_ids = project.get("role_ids", [])
        roles_with_no_id = [] #用户给llm提供的角色信息，用于生成分镜
        role_id_map = {}  # 角色ID到角色信息的映射
        name_to_role_id = {}  # 角色名称到ID的映射（用于台词处理）
        
        # 获取所有角色详细信息
        for role_id in role_ids:
            role = await mongo_instance.find_one("roles", {"_id": role_id, "user_id": user_id})
            if not role:
                continue
                
            role_name = role.get("role_name", "")
            role_resource_id = role.get("selected_role_resource_id", None)
                            
            role_resource = await mongo_instance.find_one("role_resources", {"_id": role_resource_id})
            if not role_resource:
                continue
            
            # 保存角色ID和资源ID映射
            role_id_map[str(role_id)] = {
                "name": role_name,
                "resource_id": role_resource_id,
                "description_en": role_resource.get("description_en", ""),
                "resource_url": role_resource.get("resource_url", "")
            }
            name_to_role_id[role_name] = str(role_id)  # 添加小写名称到ID的映射
            
            # 添加不包含ID的角色信息到角色列表
            roles_with_no_id.append({
                "name": role_name,
                "description_en": role_resource.get("description_en", ""),
            })
                        
        # 创建语言模型
        llm_model = create_llm_model()
        
        image_model_name = project.get("image_model_name")
        
        # 创建图像模型
        image_model = create_image_model(image_model_name)
        default_shot_image_url = image_model.get_default_shot_image_url()
        
        # 获取当前时间
        current_time, beijing_formatted_time, _ = mongo_instance.get_current_time()
        
        # 获取项目风格
        style_type = project.get("style_type", 0)
        style_type_desc = project.get("style_type_desc", "")
        times_and_culture = project.get("times_and_culture_en", "")
        
        # 处理每个分镜
        total_shots = len(shots)
                
        #拥有资源的分镜数量
        has_resource_shots = 0
        
        # 生成进度
        progress = 0
        
        # 处理每个分镜
        for idx, shot in enumerate(shots):
            shot_id = shot.get("_id")
            
            # 创建不包含ID的角色列表
            simplified_roles = []
            
            #创建用于生成分镜画面的角色信息
            image_roles = []
            
            selected_roles = shot.get("selected_roles", [])
            for role in selected_roles:
                role_id = str(role.get("role_id", ""))
                simplified_role = {
                    "role_name": role_id_map.get(role_id, {}).get("name", ""),
                    "action_and_emotion_en": role.get("action_and_emotion_en", "")
                }
                simplified_roles.append(simplified_role)
                
                image_role = {
                    "role_name": role_id_map.get(role_id, {}).get("name", ""),
                    "description_en": role_id_map.get(role_id, {}).get("description_en", ""),
                    "resource_url": role_id_map.get(role_id, {}).get("resource_url", ""),
                    "action_and_emotion_en": role.get("action_and_emotion_en", "")
                }
                image_roles.append(image_role)
                                        
            # 检查分镜是否已经有图像
            if shot.get("selected_shot_resource_id", None):                
                # 构建前端需要的已有分镜信息
                shot_resource_id = shot.get("selected_shot_resource_id", None)
                
                shot_resource = await mongo_instance.find_one("shot_resources", {"_id": shot_resource_id})
                
                shot_resource_url = shot_resource.get("resource_url", "")
                
                if shot_resource_url != default_shot_image_url:
                    logging.info(f"Shot {idx+1} already has image in project {project_id}, skipping")
                    progress = int(((idx + 1) / total_shots) * 100)
                      
                    # 构建ShotResource对象
                    frontend_shot_resource = {
                        "shot_resource_url": shot_resource.get("resource_url", ""),
                        "is_HD": shot_resource.get("is_HD", False) if shot_resource else False,
                        "shot_resource_id": str(shot_resource_id)
                    }
                    
                    # 构建Character列表
                    characters = []
                    for role in selected_roles:
                        role_id = str(role.get("role_id", ""))
                        characters.append({
                            "role_id": role_id,
                            "role_name": role_id_map.get(role_id, {}).get("name", ""),
                            "action_and_emotion": role.get("action_and_emotion", "")
                        })
                    
                    # 构建SceneDescription对象
                    scene_description = {
                        "background": shot.get("background", ""),
                        "characters": characters
                    }
                    
                    # 构建Dialogue列表
                    frontend_dialogues = []
                    for dialogue in shot.get("dialogues", []):
                        role_id = str(dialogue.get("role_id", ""))
                        role_name = ""
                        
                        # 查找角色名称
                        if role_id == "voiceover":
                            role_name = get_translation("voiceover")
                        elif role_id in role_id_map:
                            role_name = role_id_map[role_id]["name"]
                        
                        frontend_dialogues.append({
                            "role_id": role_id,
                            "content": dialogue.get("content", ""),
                            "role_name": role_name
                        })
                    
                    # 构建MainCharacter列表
                    main_characters = []
                    for role in selected_roles:
                        role_id = str(role.get("role_id", ""))
                        main_characters.append({
                            "role_id": role_id,
                            "role_name": role_id_map.get(role_id, {}).get("name", ""),
                            "role_resource_url": role_id_map.get(role_id, {}).get("resource_url", ""),
                        })
                    
                    # 构建ShotSize对象
                    size_values = get_translation("size_values") 
                    shot_size_obj = {
                        "value": size_values[shot.get("shot_size", 1)],
                        "size_values": size_values 
                    }
                    
                    # 构建CameraAngle对象
                    angle_values = get_translation("angle_values")   
                    camera_angle_obj = {
                        "value": angle_values[shot.get("camera_angle", 0)],
                        "angle_values": angle_values
                    }
                    
                    # 构建ShotType对象
                    type_values = get_translation("type_values")
                    shot_type_obj = {
                        "value": type_values[shot.get("shot_type", 0)],
                        "type_values": type_values
                    }
                    
                    # 构建ShotTime对象
                    shot_time_obj = {
                        "value": str(shot.get("shot_time", 3)),
                        "time_scale": get_translation("second")
                    }
                    
                    # 构建完整的StoryboardShot对象
                    frontend_shot = {
                        "shot_id": str(shot_id),
                        "shot_resource": frontend_shot_resource,
                        "scene_description": scene_description,
                        "dialogues": frontend_dialogues,
                        "main_characters": main_characters,
                        "shot_size": shot_size_obj,
                        "camera_angle": camera_angle_obj,
                        "shot_type": shot_type_obj,
                        "shot_time": shot_time_obj
                    }
                    
                    # 发送已有的分镜信息给前端
                    yield encode_sse_data(frontend_shot)
                    yield encode_sse_data(get_translation("shot_already_has_image").format(index=idx+1,progress=progress), event="progress")
                    
                    has_resource_shots += 1
                    # 继续检查没有资源的分镜
                    continue
                        
            # 获取镜头参数
            shot_size = int(shot.get("shot_size", 1))
            camera_angle = int(shot.get("camera_angle", 0))
            shot_type = int(shot.get("shot_type", 0))
            shot_time = int(shot.get("shot_time", 3))
                                    
            # 获取台词信息
            dialogues = shot.get("dialogues", [])
                    
            # 生成分镜图像
            logging.info(f"Generating image for shot {idx+1} in project {project_id}")
            yield encode_sse_data(get_translation("generating_image_for_shot").format(index=idx+1,progress=progress), event="progress")
                                            
            shot_data = {
                "shot_size": get_translation("size_values","en")[shot_size],
                "camera_angle": get_translation("angle_values","en")[camera_angle],
                "shot_type": get_translation("type_values","en")[shot_type],
                "shot_time": f"{shot_time} seconds",
                "background_en": shot.get("background_en", ""),
                "selected_roles": image_roles,
            }
            
            generate_seed = random.randint(100000, 999999)
            image_size = project.get("image_size", "1344x768")
                        
            # 构建提示词
            image_style = image_model.get_model_image_style(style_type)
            image_size = project.get("image_size", "1344x768")
            aspect_ratio = image_model.get_aspect_ratio(image_size)
            
            shot_system_prompt, shot_prompt = get_shot_image_prompt(shot_data,image_style,aspect_ratio)
            
            # logging.info(f"shot_prompt: {shot_prompt}")
            
            # 开始计时
            start_time = time.time()
            try:
                # 提取角色和场景信息        
                messages = [
                    {"role": "system", "content": shot_system_prompt},
                    {"role": "user", "content": shot_prompt}
                ]
                
                # 创建LLM调用任务
                llm_task = asyncio.create_task(
                    llm_model.generate_content(messages, is_json=False, used_type = "generate_shot_prompt")
                )
                
                # 等待任务完成，同时定期发送进度消息
                while not llm_task.done():
                    await asyncio.sleep(1)  # 每秒检查一次
                    yield encode_sse_data("", event="heartbeat")

                # 获取结果
                shot_prompt = await llm_task
                # logging.info(f"generate_shot_image llm_shot_prompt: {shot_prompt}")
                
            except Exception as e:
                logging.error(f"Error in generate_shot_image generate_shot_prompt: {e}",exc_info=True)
                
            end_time = time.time()
            duration = end_time - start_time
            logging.info(f"generate_shot_prompt duration: {duration:.2f} seconds")
            
            # 开始计时
            start_time = time.time()
            
            #使用类型
            used_type ="generate_shot_image"
                      
            # 构造角色参数，根据角色数量填充
            image_roles_count = len(image_roles)
            if image_roles_count == 0:
                first_character = None
                second_character = None
                third_character = None
            elif image_roles_count == 1:
                first_character = image_roles[0]["resource_url"]
                second_character = None
                third_character = None
            elif image_roles_count == 2:
                first_character = image_roles[0]["resource_url"]
                second_character = image_roles[1]["resource_url"]
                third_character = None
            else:
                first_character = image_roles[0]["resource_url"]
                second_character = image_roles[1]["resource_url"]
                third_character = image_roles[2]["resource_url"]
                
            logging.info(f"Generate image with {image_roles_count} characters using generate_shot_image_with_characters")  
            
            #设置默认值
            generate_id, shot_image_url, image_prompt =  "", "", ""
            
            try:
                # 创建生图调用任务
                image_task = asyncio.create_task(
                    image_model.generate_shot_image_with_characters(used_type,shot_prompt, style_type, image_size, generate_seed,first_character,second_character,third_character)
                )
                
                # 等待任务完成，同时定期发送进度消息
                while not image_task.done():
                    await asyncio.sleep(1)  # 每秒检查一次
                    yield encode_sse_data("", event="heartbeat")

                # 获取结果
                generate_result = await image_task
                                     
                if generate_result['code'] != 0:                    
                    generate_code = generate_result['code']
                    error_msg = generate_result["msg"]
                    warning_msg = f"Failed to generate image for shot {idx+1}"
                            
                    if generate_code == 2: # 积分不足
                        error_msg = get_translation("credits_not_enough")
                        warning_msg = error_msg
                        
                    elif generate_code == 7: # 提示词或者图片非法
                        error_msg = get_translation("prompt_or_image_illegal")
                        warning_msg = error_msg
                        
                    #不特殊处理其他类型                 
                    logging.error(f"Failed to generate image for shot {idx+1} in project {project_id}, reason is: {error_msg}")
                    yield encode_sse_data(warning_msg, event="warning")
                else:
                    # 计算耗时
                    end_time = time.time()
                    duration = end_time - start_time
                    
                    generate_id = generate_result["generate_id"]
                    image_prompt = generate_result['image_prompt']
                    shot_image_url = generate_result['image_url']
                    logging.info(f"Success to generate image for shot {idx+1} in project {project_id}, image_model: {image_model_name}, duration: {duration:.2f} seconds")
                
            except Exception as e:
                logging.error(f"Error in generate_shot_image_with_characters: {e}",exc_info=True)
                                                     
            if not shot_image_url:
                shot_image_url = default_shot_image_url
                
            if shot_image_url:
                # 创建镜头资源ID
                shot_resource_id = mongo_instance.generate_object_id()
                
                # 创建镜头资源
                shot_resource = {
                    "_id": shot_resource_id,
                    "user_id": user_id,
                    "project_id": project_id,
                    "shot_id": shot_id,
                    "style_type": style_type,
                    "style_type_desc": style_type_desc,
                    "image_size": project.get("image_size", "1344x768"),
                    "generate_seed": generate_seed,
                    "generate_id": generate_id,
                    "generate_status": "done",
                    "resource_type": 1,  # 1表示图片
                    "resource_url": shot_image_url,
                    "resource_prompt": image_prompt,
                    "image_model_name": image_model_name,
                    "is_HD": False,
                    "last_updated_at": current_time,
                    "created_at": current_time,
                    "created_at_str": beijing_formatted_time
                }
                
                # 保存镜头资源到数据库
                await mongo_instance.insert_one("shot_resources", shot_resource)
                
                # 更新分镜信息
                update_data = {
                    "selected_shot_resource_id": shot_resource_id,
                    "last_updated_at": current_time
                }
                                        
                await mongo_instance.update_one(
                    "shots",
                    {"_id": shot_id},
                    {
                        "$set": update_data, 
                        "$push": {"shot_resource_ids": shot_resource_id}
                    }
                )
                
                # 如果是第一个生成的分镜图像，并且项目封面为空，则更新项目封面
                project_cover = project.get("cover", "")
                if not project_cover or project_cover == default_shot_image_url:
                    if shot_image_url != default_shot_image_url:
                        await mongo_instance.update_one(
                            "projects",
                            {"_id": project_id},
                            {"$set": {"cover": shot_image_url, "last_updated_at": current_time}}
                        )
                        logging.info(f"Setting project {project_id} cover to first generated shot image")
                        # 更新本地项目对象，避免后续重复设置封面
                        project["cover"] = shot_image_url
                            
                progress = int(((idx + 1) / total_shots) * 100)
                
                # 构建前端需要的分镜信息
                frontend_shot_resource = {
                    "shot_resource_url": shot_image_url,
                    "is_HD": False,
                    "shot_resource_id": str(shot_resource_id)
                }
                
                # 构建Character列表
                characters = []
                for role in selected_roles:
                    role_id = str(role.get("role_id", ""))
                    characters.append({
                        "role_id": role_id,
                        "role_name": role_id_map.get(role_id, {}).get("name", ""),
                        "action_and_emotion": role.get("action_and_emotion", "")
                    })
                
                # 构建SceneDescription对象
                scene_description = {
                    "background": shot.get("background", ""),
                    "characters": characters
                }
                
                # 构建Dialogue列表
                frontend_dialogues = []
                for dialogue in dialogues:
                    role_id = str(dialogue.get("role_id", ""))
                    role_name = ""
                    
                    # 查找角色名称
                    if role_id == "voiceover":
                        role_name = get_translation("voiceover")
                    elif role_id in role_id_map:
                        role_name = role_id_map[role_id]["name"]
                    
                    frontend_dialogues.append({
                        "role_id": role_id,
                        "content": dialogue.get("content", ""),
                        "role_name": role_name
                    })
                
                # 构建MainCharacter列表
                main_characters = []
                for role in selected_roles:
                    role_id = str(role.get("role_id", ""))
                    main_characters.append({
                        "role_id": role_id,
                        "role_name": role_id_map.get(role_id, {}).get("name", ""),
                        "role_resource_url": role_id_map.get(role_id, {}).get("resource_url", "")
                    })
                
                # 构建ShotSize对象
                size_values = get_translation("size_values")
                shot_size_obj = {
                    "value": size_values[shot_size],
                    "size_values": size_values 
                }
                
                # 构建CameraAngle对象
                angle_values = get_translation("angle_values")   
                camera_angle_obj = {
                    "value": angle_values[camera_angle],
                    "angle_values": angle_values
                }
                
                # 构建ShotType对象
                type_values = get_translation("type_values")
                shot_type_obj = {
                    "value": type_values[shot_type],
                    "type_values": type_values
                }
                
                # 构建ShotTime对象
                shot_time_obj = {
                    "value": str(shot_time),
                    "time_scale": get_translation("second")
                }
                
                # 构建完整的StoryboardShot对象
                frontend_shot = {
                    "shot_id": str(shot_id),
                    "shot_resource": frontend_shot_resource,
                    "scene_description": scene_description,
                    "dialogues": frontend_dialogues,
                    "main_characters": main_characters,
                    "shot_size": shot_size_obj,
                    "camera_angle": camera_angle_obj,
                    "shot_type": shot_type_obj,
                    "shot_time": shot_time_obj
                }
                
                has_resource_shots += 1
                
                # 发送新生成的分镜信息给前端
                yield encode_sse_data(frontend_shot)
                yield encode_sse_data(get_translation("generated_image_for_shot").format(index=idx+1,total_shots=total_shots,progress=progress), event="progress")
        
        # 更新项目信息
        if has_resource_shots == total_shots:
            project_update = {
                "has_shot": True,
                "last_updated_at": current_time
            }

            await mongo_instance.update_one(
                "projects",
                {"_id": project_id},
                {"$set": project_update}
            )
            
            logging.info(f"All shot details generated for project {project_id}, total: {total_shots}")
            yield encode_sse_data("Complete")
        else:
            logging.warning(f"Failed to generate image for some shots in project {project_id}")
            yield encode_sse_data(get_translation("failed_to_generate_image_for_some_shots"), event="warning")
            
    except Exception as e:
        logging.error(f"Error in generate_shots_detail: {e}", exc_info=True)
        yield encode_sse_data(get_translation("server_error"), event="error")
      
@shot_router.get('/shot')
async def operator(projectId: str):
    project_id = mongo_instance.generate_object_id(projectId)
    
    # 获取用户ID
    user_id = get_user_id()
            
    # 检查项目是否存在
    project = await mongo_instance.find_one("projects", {"_id": project_id, "user_id": user_id, "status": "active"})
    if not project:
        logging.error(f"User {user_id} cannot access project {project_id}")
        return JSONResponse(
            content={"code": 404, "msg": get_translation("project_not_found"), "data": {}}
        )
    
    logging.info(f"Starting shot generation for project {project_id}")
    return StreamingResponse(
        generate_shots_detail(user_id, project_id),
        media_type='text/event-stream; charset=utf-8',
        headers={
            'Cache-Control': 'no-cache',
            'Connection': 'keep-alive',
        }
    )