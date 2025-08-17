from fastapi import APIRouter
from fastapi.responses import JSONResponse,StreamingResponse
from app.utils.core import get_user_id,encode_sse_data
from app.utils.mongo import mongo_instance
from app.models.model_factory import create_image_model,create_translator_model,create_llm_model
from app.models.prompts.generate_image import get_shot_image_prompt
from app.locales.translations import get_translation

import logging, random,asyncio,time
from typing import AsyncGenerator

regenerate_router = APIRouter()

async def regenerate_shot_image(user_id, project_id, shot_id) -> AsyncGenerator[bytes, None]: 
    """生成分镜内容的流式响应"""
    yield encode_sse_data("Connection successful")

    # 查询项目信息
    project = await mongo_instance.find_one(
        "projects",
        {
            "_id": project_id,
            "user_id": user_id,
            "status": "active"
        }
    )
    
    # 查询分镜信息
    shot = await mongo_instance.find_one(
        "shots", 
        {
            "_id": shot_id,
            "user_id": user_id,
            "status": "active"
        }
    )
     
    #语言模型
    llm_model = create_llm_model()
        
    # 创建图像模型
    image_model_name = project.get("image_model_name")
    image_model = create_image_model(image_model_name)
    
    #翻译模型
    translator_model = create_translator_model()
    
    # 获取当前时间
    current_time, beijing_formatted_time, _ = mongo_instance.get_current_time()
    
    # 获取项目风格
    style_type = project.get("style_type", 0)
    style_type_desc = project.get("style_type_desc", "")
    times_and_culture = project.get("times_and_culture_en", "")
    
    # 创建不包含ID的角色列表
    image_roles = []
    selected_roles = shot.get("selected_roles", [])
    
    # 获取角色信息
    role_id_map = {}
    for role in selected_roles:
        role_id = str(role.get("role_id", ""))
        role_info = await mongo_instance.find_one("roles", {"_id": role.get("role_id")})
        if role_info:
            role_name = role_info.get("role_name", "")
            role_id_map[role_id] = {"name": role_name}
            
            selected_role_resource_id = role_info.get("selected_role_resource_id", "")
            
            role_resource_info = await mongo_instance.find_one("role_resources", {"_id": selected_role_resource_id})
            
            if role_resource_info:
                description_en = role_resource_info.get("description_en", "")
                resource_url = role_resource_info.get("resource_url", "")
            else:
                description_en = ""
                resource_url = ""
            
            #需要将原始内容的action_and_emotion翻译为英文。因为用户可能修改过，所以需要重新翻译
            action_and_emotion = role.get("action_and_emotion", "")
            
            translate_result = await translator_model.translate(action_and_emotion)
            
            if translate_result['code'] != 0:
                action_and_emotion_en = action_and_emotion
            else:
                action_and_emotion_en = translate_result["data"]
            
            image_role = {
                "role_name": role_name,
                "description_en": description_en,
                "resource_url": resource_url,
                "action_and_emotion_en": action_and_emotion_en
            }
            image_roles.append(image_role)
            
            
    #翻译背景信息
    background = shot.get("background", "")
    translate_result = await translator_model.translate(background)

    if translate_result['code']!= 0:
        background_en = background
    else:
        background_en = translate_result["data"]
    
    # 准备分镜数据
    shot_data = {
        "shot_size": get_translation("size_values", "en")[shot.get("shot_size", 1)],
        "camera_angle": get_translation("angle_values", "en")[shot.get("camera_angle", 0)],
        "shot_type": get_translation("type_values", "en")[shot.get("shot_type", 0)],
        "shot_time": f"{shot.get('shot_time', 3)} seconds",
        "background_en": background_en,
        "selected_roles": image_roles,
    }
    
    # 生成随机种子
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
        #shot_prompt = await llm_model.generate_content(messages, is_json=False, used_type = "generate_shot_prompt")
        # logging.info(f"regenerate_shot_image llm_shot_prompt: {shot_prompt}")
        
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
        
    except Exception as e:
        logging.error(f"Error in regenerate_shot_image generate_shot_prompt: {e}",exc_info=True)
        
    end_time = time.time()
    duration = end_time - start_time
    logging.info(f"regenerate_shot_prompt duration: {duration:.2f} seconds")
    
    # 开始计时
    start_time = time.time()
    
    #使用类型
    used_type = "regenerate_shot_image"
    
    # 生成图像
    # generate_result = await image_model.generate_shot_image_with_no_character(shot_prompt, style_type, size=image_size, seed=generate_seed)
    
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
            warning_msg = f"Failed to generate image for shot"
                    
            if generate_code == 2: # 积分不足
                error_msg = get_translation("credits_not_enough")
                warning_msg = error_msg
                
            elif generate_code == 7: # 提示词或者图片非法
                error_msg = get_translation("prompt_or_image_illegal")
                warning_msg = error_msg
            
            #不特殊处理其他类型                 
            logging.error(f"Failed to generate image for shot {shot_id} in project {project_id}, reason is: {error_msg}")
            yield encode_sse_data(warning_msg, event="error")
            return
        else:
            # 计算耗时
            end_time = time.time()
            duration = end_time - start_time
            
            generate_id = generate_result["generate_id"]
            image_prompt = generate_result['image_prompt']
            shot_image_url = generate_result['image_url']
            logging.info(f"Success to generate image for shot {shot_id} in project {project_id}, image_model: {image_model_name}, duration: {duration:.2f} seconds")
        
    except Exception as e:
        logging.error(f"Error in generate_shot_image_with_characters: {e}",exc_info=True)
        warning_msg = f"Failed to generate image for shot {shot_id}"
        yield encode_sse_data(warning_msg, event="error")
        return
                       
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
        "image_size": image_size,
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
    
    # 更新分镜的资源ID列表
    shot_resource_ids = shot.get("shot_resource_ids", [])
    shot_resource_ids.insert(0, shot_resource_id)  # 将新资源ID添加到列表前面
    
    # 更新分镜信息
    await mongo_instance.update_one(
        "shots",
        {"_id": shot_id},
        {
            "$set": {
                "selected_shot_resource_id": shot_resource_id,
                "shot_resource_ids": shot_resource_ids,
                "last_updated_at": current_time
            }
        }
    )
    
    # 更新项目
    project_cover = project.get("cover", "")
    if not project_cover:
        await mongo_instance.update_one(
            "projects",
            {"_id": project_id},
            {
                "$set": {
                    "cover": shot_image_url,
                    "last_updated_at": current_time
                }
            }
        )
    else: 
        await mongo_instance.update_one(
            "projects",
            {"_id": project_id},
            {
                "$set": {
                    "last_updated_at": current_time
                }
            }
        )
    
    # 构建返回数据
    response_data = {
        "shot_resource_id": str(shot_resource_id),
        "is_HD": False,
        "shot_resource_url": shot_image_url
    }
    
    #发送数据
    yield encode_sse_data(response_data)
    #发送成功标志
    yield encode_sse_data(get_translation("regenerate_image_success"), event="progress")
    #发送结束标志
    yield encode_sse_data("Complete")
    
@regenerate_router.get('/regenerate')
async def operator( projectId: str, storyboardId: str):
    """重新生成分镜图像
    
    Args:
        shotId: 分镜ID
        
    Returns:
        JSONResponse: 重新生成的分镜信息
    """
        
    # 获取当前用户ID
    user_id = get_user_id()
    
    # 转换为ObjectId
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
            "code": 1,
            "data": None,
            "msg": get_translation("project_not_found"),
        })
    
    shot_id = mongo_instance.generate_object_id(storyboardId)
    
    # 查询分镜信息
    shot = await mongo_instance.find_one(
        "shots", 
        {
            "_id": shot_id,
            "user_id": user_id,
            "status": "active"
        }
    )
    
    if not shot:
        return JSONResponse(content={
            "code": 1,
            "data": None,
            "msg": get_translation("shot_not_found_or_no_right"),
        })
        
    return StreamingResponse(
        regenerate_shot_image(user_id, project_id, shot_id),
        media_type='text/event-stream; charset=utf-8',
        headers={
            'Cache-Control': 'no-cache',
            'Connection': 'keep-alive',
        }
    )