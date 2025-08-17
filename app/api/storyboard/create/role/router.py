from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse, StreamingResponse
import logging
import asyncio
import time
import random
import json
from datetime import datetime, timezone, timedelta

from app.utils.mongo import mongo_instance
from app.models.model_factory import create_llm_model, create_image_model, create_translator_model
from app.models.prompts.extract_storyboard import get_extract_complete_storyboard_prompt
from app.models.prompts.generate_image import get_role_image_prompt
from app.utils.core import get_user_id, encode_sse_data
from app.locales.translations import get_translation

role_router = APIRouter()

MAX_RETRIES = 3

async def generate_complete_storyboard(user_id: str, project_id: str):
    """一次性生成完整的故事板，包括角色和分镜详细信息"""
    try:
        """生成角色内容的流式响应"""
        yield encode_sse_data("Connection successful")
        
        # 获取项目信息
        project = await mongo_instance.find_one("projects", {"_id": project_id, "user_id": user_id, "status": "active"})
            
        script_content = project.get("script_content", "")
        
        if project.get("has_storyboard", False):
            #查找所有角色信息给前端发送            
            role_ids = project.get("role_ids", [])
        
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
                    role_info = {
                        "roleId": str(role["_id"]),
                        "figureName": role.get("role_name", ""),
                        "figureDesc": role_resource.get("description", ""),
                        "url": role_resource.get("resource_url", ""),
                    }            
                    yield encode_sse_data(role_info)
            
            yield encode_sse_data("Complete")
        
        if not script_content:
            yield encode_sse_data(get_translation("script_content_empty"), event="error")
            yield encode_sse_data("Complete")
            return
            
        yield encode_sse_data(get_translation("extracting_roles_and_shots_from_script"), event="progress")
        
        #翻译模型
        translator_model = create_translator_model()
        
        # 使用大模型从内容中提取角色和场景信息
        llm_model = create_llm_model()
        
        #获取分镜画面风格
        image_model_name = project["image_model_name"]
        
        # 创建图像模型
        image_model = create_image_model(image_model_name)
        image_style = image_model.get_model_image_style(project["style_type"])
        image_size = project.get("image_size", "1344x768")
        aspect_ratio = image_model.get_aspect_ratio(image_size)
        
        # 开始计时
        start_time = time.time()
        for attempt in range(MAX_RETRIES):  
            try:
                # 提取角色和场景信息 
                messages = [
                    {"role": "system", "content": get_extract_complete_storyboard_prompt(image_style,aspect_ratio)},
                    {"role": "user", "content": script_content}
                ]
            
                # 创建LLM调用任务
                llm_task = asyncio.create_task(
                    llm_model.generate_content(messages, is_json=True, used_type="parse_script")
                )
                
                # 等待任务完成，同时定期发送进度消息
                while not llm_task.done():
                    await asyncio.sleep(1)
                    yield encode_sse_data("", event="heartbeat")

                # 获取结果
                response = await llm_task
                
                # logging.info(f"parse result is {response}")
                # 提取JSON部分
                json_start = response.find('{')
                json_end = response.rfind('}') + 1
                if json_start >= 0 and json_end > json_start:
                    json_str = response[json_start:json_end]
                    story_elements = json.loads(json_str)
                    break
                                    
            except Exception as e:
                logging.warning(f"Failed to extract roles and shots for project {project_id}: {e}")
            
            if attempt == MAX_RETRIES - 1:  # 最后一次重试
                logging.error(f"Failed to extract roles and shots for project {project_id} after {MAX_RETRIES} attempts")
                yield encode_sse_data(get_translation("failed_to_parse_extracted_data"), event="error")
                yield encode_sse_data("Complete")
                return
            else:
                logging.warning(f"Failed to extract roles and shots for project {project_id} after {attempt + 1} attempts, retrying...")
                await asyncio.sleep(2 ** attempt)  # 指数退避
                yield encode_sse_data("", event="heartbeat")
                    
        roles = story_elements.get("roles", [])
        shots = story_elements.get("shots", [])
        
        if not roles or not shots:
            yield encode_sse_data(get_translation("cannot_extract_story_elements_from_script"), event="error")
            yield encode_sse_data("Complete")
            return
        
        end_time = time.time()
        duration = end_time - start_time
            
        logging.info(f"Extracted {len(roles)} roles and {len(shots)} shots for project {project_id} in {duration:.2f} seconds")
        
        # 更新项目语言信息和年代文化信息
        language = story_elements.get("language", "zh-CN")
        times_and_culture = story_elements.get("times_and_culture", "")
        
        # 翻译年代文化信息
        translate_result = await translator_model.translate(times_and_culture, "en")
        if translate_result['code'] == 0:
            times_and_culture_en = translate_result["data"]
        else:
            times_and_culture_en = times_and_culture
        
        # 获取当前时间
        current_time, beijing_formatted_time, _ = mongo_instance.get_current_time()
        
        # 第一阶段：生成角色图像
        yield encode_sse_data(get_translation("creating_roles_and_generating_images"), event="progress")
        
        generate_seed = random.randint(100000, 999999)
        image_size = image_model.get_role_image_size()  # 添加固定尺寸
        
        role_id_map = {}
        role_ids = []
        total_roles = len(roles)
        progress = 0
        processed_roles = 0
        
        for idx, role in enumerate(roles):                
            # 创建角色ID
            new_role_id = mongo_instance.generate_object_id()
            role_ids.append(new_role_id)
            role_name = role.get("name", f"role_{idx+1}")
            role_id_map[role_name] = new_role_id
            
            
            role_desc = role.get("description", "")
            
            # 翻译角色描述
            translate_result = await translator_model.translate(role_desc, "en")
            if translate_result['code'] == 0:
                role_desc_en = translate_result["data"]
            else:
                role_desc_en = role_desc
            
            # 创建角色资源
            new_role_resource_id = mongo_instance.generate_object_id()
                                                            
            new_role_resource = {
                "_id": new_role_resource_id,
                "user_id": user_id,
                "project_id": project_id,
                "role_id": new_role_id,
                "description": role_desc,
                "description_en": role_desc_en,
                "style_type": project["style_type"],
                "style_type_desc": project["style_type_desc"],
                "voice_model_name": "",
                "face_image": "",
                "projection_image": [],
                "last_updated_at": current_time,
                "created_at": current_time,
                "created_at_str": beijing_formatted_time
            }
                                            
            # 生成角色图像
            logging.info(f"Generating image for role {role_name} in project {project_id}")
            yield encode_sse_data(get_translation("generating_image_for_role").format(role_name=role_name,progress=progress), event="progress")
                
            # 根据角色描述生成提示词
            image_style = image_model.get_model_image_style(new_role_resource.get("style_type"))
            role_system_prompt, role_prompt = get_role_image_prompt(new_role_resource["description_en"],image_style,times_and_culture_en)
            
            # logging.info(f"role_prompt: {role_prompt}")
            
            # 初始化变量，避免UnboundLocalError
            optimized_prompt = role_prompt
            height_percentage = 85
            image_size = None
            
            # 开始计时
            start_time = time.time()
            #这里需要引入语言模型，进行他或者是她的转换
            for attempt in range(MAX_RETRIES): 
                try:
                    # 提取角色和场景信息        
                    messages = [
                        {"role": "system", "content": role_system_prompt},
                        {"role": "user", "content": role_prompt}
                    ]
                    
                    # 创建LLM调用任务
                    llm_task = asyncio.create_task(
                        llm_model.generate_content(messages, is_json=True, used_type = "generate_role_prompt")
                    )
                    
                    # 等待任务完成，同时定期发送进度消息
                    while not llm_task.done():
                        await asyncio.sleep(1)  # 每秒检查一次
                        yield encode_sse_data("", event="heartbeat")

                    # 获取结果
                    response = await llm_task
                    
                    #response = await llm_model.generate_content(messages, is_json=True, used_type = "generate_role_prompt")
                    # logging.info(f"generate_role_image llm_role_prompt: {response}")
                    
                    # 尝试从响应中提取JSON
                    start_idx = response.find('{')
                    end_idx = response.rfind('}') + 1
                    if start_idx >= 0 and end_idx > start_idx:
                        json_str = response[start_idx:end_idx]
                    
                        # 解析JSON
                        json_response = json.loads(json_str)
                        optimized_prompt = json_response['optimized_prompt']
                        
                        #height_percentage指的是人物占画面的高度。
                        height_percentage = json_response['height_percentage']
                        image_size = image_model.get_role_image_size_by_height_percentage(height_percentage) 
                        
                        break
                    
                except Exception as e:
                    logging.warning(f"Error in generate_role_image generate_role_prompt: {e}",exc_info=True)
                    
                if attempt == MAX_RETRIES - 1:  # 最后一次重试
                    logging.warning(f"Failed in generate_role_image generate_role_prompt after {MAX_RETRIES} attempts")
                    optimized_prompt = role_prompt
                    height_percentage = 85
                    image_size = image_model.get_role_image_size_by_height_percentage(height_percentage) 
                else:
                    logging.warning(f"Failed in generate_role_image generate_role_prompt after {attempt + 1} attempts, retrying...")
                    await asyncio.sleep(2 ** attempt)  # 指数退避
                    yield encode_sse_data("", event="heartbeat")
                        
            end_time = time.time()
            duration = end_time - start_time
            logging.info(f"generate_role_prompt duration: {duration:.2f} seconds")
            
            start_time = time.time()
                   
            #使用类型
            used_type = "generate_role_image"
            
            #设置默认值
            generate_id, role_image_url, role_prompt =  "", "", ""  
            
            try:
                
                # 创建生图调用任务
                image_task = asyncio.create_task(
                    image_model.generate_character_image(used_type, optimized_prompt, style_type=new_role_resource.get("style_type", None), size=image_size, seed=generate_seed)
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
                            
                    if generate_code == 2: # 积分不足
                        error_msg = get_translation("credits_not_enough")
                        warning_msg = error_msg
                    
                    elif generate_code == 7: # 提示词或者图片非法
                        error_msg = get_translation("prompt_or_image_illegal")
                        warning_msg = error_msg
                    
                    else:
                        warning_msg = get_translation("failed_to_generate_image_for_role").format(role_name=role_name)
                        
                    logging.error(f"Failed to generate image for role {role_name} in project {project_id}, reason is: {error_msg}")
                    
                    yield encode_sse_data(warning_msg, event="warning") #这里不能用error，前端会直接中断
                else:
                    # 计算耗时
                    end_time = time.time()
                    duration = end_time - start_time
                    
                    generate_id = generate_result["generate_id"]
                    role_prompt = generate_result['image_prompt']
                    role_image_url = generate_result['image_url']
                    model_name = image_model.get_model_name()
                    logging.info(f"Success to generate image for role {role_name} in project {project_id}, image_model: {model_name}, duration: {duration:.2f} seconds")
                
            except Exception as e:
                logging.error(f"Error in generate_character_image: {e}",exc_info=True)
                                            
            # 更新角色资源
            new_role_resource["resource_url"] = role_image_url
            new_role_resource["resource_prompt"] = role_prompt
            new_role_resource["image_model_name"] = image_model_name
            new_role_resource["generate_seed"] = generate_seed
            new_role_resource["generate_id"] = generate_id
            new_role_resource["generate_status"] = "done"
            new_role_resource["image_size"] = image_size
                                
            # 保存角色资源到数据库
            await mongo_instance.insert_one("role_resources", new_role_resource)
            
            # 创建角色
            new_role = {
                "_id": new_role_id,
                "user_id": user_id,
                "project_id": project_id,
                "status": "active",
                "role_name": role_name,
                "selected_role_resource_id":new_role_resource_id, #当前选中角色资源ID
                "role_resource_ids": [new_role_resource_id],
                "last_updated_at": current_time,
                "created_at": current_time,
                "created_at_str": beijing_formatted_time
            }
            
            # 保存角色到数据库
            await mongo_instance.insert_one("roles", new_role)
            
            # logging.info(f"Successfully generated image for role {role_name} in project {project_id}")
            
            # 给前端发送当前完成的角色信息
            role_info = {
                "figureName": role_name,
                "url": role_image_url,
                "id": str(new_role_id),
                "figureDesc": new_role_resource.get("description", ""),
            }
            yield encode_sse_data(role_info)
    
            processed_roles += 1
            progress = int((processed_roles / total_roles) * 100)
            yield encode_sse_data(get_translation("processed_roles_progress").format(role_name=role_name,progress=progress), event="progress")
             
        # 第二阶段：生成分镜详细信息和图像
        yield encode_sse_data(get_translation("creating_shots_base_info"), event="progress")
        
        shot_ids = []
        
        for idx, shot in enumerate(shots):
            # 创建镜头ID
            new_shot_id = mongo_instance.generate_object_id()
            shot_ids.append(new_shot_id)
            
            default_selected_roles = shot.get("selected_roles", [])
            
            # logging.info(f"Selected_roles in shot {idx} with project {project_id} is {default_selected_roles}")
            
            # 处理角色信息
            selected_roles = []
            for role_info in default_selected_roles:
                role_name = role_info.get("role_name", "")
                if role_name in role_id_map:
                    role_id = role_id_map[role_name]
                    
                    # 获取动作和情绪描述
                    action_and_emotion = role_info.get("action_and_emotion", "")
                    
                    # 翻译动作和情绪描述
                    translate_result = await translator_model.translate(action_and_emotion, "en")
                    if translate_result['code'] == 0:
                        action_and_emotion_en = translate_result["data"]
                    else:
                        action_and_emotion_en = action_and_emotion
                    
                    # 简化：检查动作和情绪描述是否以角色名称开头
                    if action_and_emotion.startswith(role_name):
                        action_and_emotion = action_and_emotion[len(role_name):]
                    
                    selected_roles.append({
                        "role_id": role_id,
                        "action_and_emotion": action_and_emotion,
                        "action_and_emotion_en": action_and_emotion_en,
                    })
                    
                    #每个镜头最多三个主角
                    if len(selected_roles) >= 3:
                        break
                    
            if not selected_roles:
                logging.info(f"There are no characters in shot {idx} with project {project_id}")
                
            # 获取台词信息
            dialogues = []
            for dialogue in shot.get("dialogues", []):
                dialogue_role_name = dialogue.get("role_name", "")
                dialogue_content = dialogue.get("content", "")
                
                # 处理旁白
                if dialogue_role_name == "voiceover":
                    dialogues.append({
                        "role_id": "voiceover",
                        "content": dialogue_content
                    })
                    continue
                
                # 尝试通过role_name找到对应角色ID
                matched_role_id = None
                
                # 直接匹配
                if dialogue_role_name in role_id_map:
                    matched_role_id = role_id_map[dialogue_role_name]
                
                if matched_role_id:
                    dialogues.append({
                        "role_id": str(matched_role_id),
                        "content": dialogue_content
                    })
                else:
                    logging.warning(f"Cannot find role_id for dialogue with role_name: {dialogue_role_name}")
                    
            #如果dialogues里面没有voiceover，就添加一个。并且加到第一个位置
            if not any(dialogue.get("role_id", "") == "voiceover" for dialogue in dialogues):
                dialogues.insert(0, {
                    "role_id": "voiceover",
                    "content": ""
                })

            # 确保旁白始终位于台词列表的第一位
            voiceover_index = next((i for i, d in enumerate(dialogues) if d.get("role_id") == "voiceover"), -1)
            if voiceover_index > 0:  # 如果旁白存在但不在第一位
                voiceover_dialogue = dialogues.pop(voiceover_index)
                dialogues.insert(0, voiceover_dialogue)
                
            # 获取镜头参数
            shot_size = int(shot.get("shot_size", 1))
            camera_angle = int(shot.get("camera_angle", 0))
            shot_type = int(shot.get("shot_type", 0))
            shot_time = int(shot.get("shot_time", 3))
            
            background = shot.get("background", "")
            
            # 翻译背景
            translate_result = await translator_model.translate(background, "en")
            if translate_result['code'] == 0:
                background_en = translate_result["data"]
            else:
                background_en = background
                    
            # 创建镜头
            new_shot = {
                "_id": new_shot_id,
                "user_id": user_id,
                "project_id": project_id,
                "status": "active",
                "background": background,
                "background_en": background_en,
                "selected_roles": selected_roles,
                "dialogues": dialogues,  
                "selected_shot_resource_id": None,
                "shot_size": shot_size,  # 默认全景
                "camera_angle": camera_angle,  # 默认视平
                "shot_type": shot_type,  # 默认固定镜头
                "shot_time": shot_time,  # 默认3秒
                "shot_resource_ids": [],
                "other_info": [],
                "last_updated_at": current_time,
                "created_at": current_time,
                "created_at_str": beijing_formatted_time
            }
            
            # 保存镜头到数据库
            await mongo_instance.insert_one("shots", new_shot)
        
    
        # 更新项目信息
        await mongo_instance.update_one(
            "projects",
            {"_id": project_id},
            {"$set": {
                "project_language": language,
                "times_and_culture": times_and_culture,
                "times_and_culture_en": times_and_culture_en,
                "has_role": True,  # 已经生成了角色图像
                "has_shot": False,
                "has_storyboard": True,
                "role_ids": role_ids,
                "shot_ids": shot_ids,
                "last_updated_at": current_time
            }}
        )
        
        logging.info(f"Successfully generated storyboard and role images for project {project_id}")
        yield encode_sse_data(get_translation("roles_and_shots_base_info_created_completed"), event="progress")
        yield encode_sse_data("Complete")
        
    except Exception as e:
        logging.error(f"Error in generate_roles: {e}", exc_info=True)
        yield encode_sse_data(get_translation("server_error"), event="error") 
        yield encode_sse_data("Complete")

@role_router.get('/role')
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
            
    logging.info(f"Starting complete storyboard generation for project {project_id}")
    return StreamingResponse(
        generate_complete_storyboard(user_id, project_id),
        media_type='text/event-stream; charset=utf-8',
        headers={
            'Cache-Control': 'no-cache',
            'Connection': 'keep-alive',
        }
    )