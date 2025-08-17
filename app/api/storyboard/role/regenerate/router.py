from fastapi import APIRouter
from fastapi.responses import JSONResponse,StreamingResponse
import random,logging,asyncio
from app.utils.mongo import mongo_instance
from app.utils.core import get_user_id,encode_sse_data
from app.models.model_factory import create_image_model
from app.models.prompts.generate_image import get_role_image_prompt
from app.models.model_factory import create_translator_model,create_llm_model
from app.locales.translations import get_translation
import time,json

from typing import AsyncGenerator

regenerate_router = APIRouter()

MAX_RETRIES = 3
    
async def regenerate_role_image(user_id, project_id,role_id, role_name,role_desc) -> AsyncGenerator[bytes, None]:
    """生成分镜内容的流式响应"""
    yield encode_sse_data("Connection successful")

    project = await mongo_instance.find_one(
        "projects",
        {
            "_id": project_id,
            "user_id": user_id,
            "status": "active"
        }
    )
                
    role = await mongo_instance.find_one(
        "roles",
        {
            "_id": role_id,
            "project_id": project_id,
            "user_id": user_id
        }
    )
            
    image_model_name = project["image_model_name"]
        
    translator_model = create_translator_model()
    
    translate_result = await translator_model.translate(role_desc, "en")
    
    if translate_result['code'] != 0:
        description_en = role_desc
    else:
        description_en = translate_result["data"]

    # 获取当前时间
    current_time, beijing_formatted_time, _ = mongo_instance.get_current_time()
    
    llm_model = create_llm_model()
    
    image_model = create_image_model(image_model_name)
    generate_seed = random.randint(100000, 999999)
    image_size = image_model.get_role_image_size()
                                                            
    # 获取角色当前选中的资源
    selected_role_resource_id = role.get("selected_role_resource_id")
    existing_resource = None
    
    if selected_role_resource_id:
        existing_resource = await mongo_instance.find_one(
            "role_resources",
            {
                "_id": selected_role_resource_id,
                "role_id": role_id,
                "user_id": user_id
            }
        )
    
    # 如果存在已选资源且没有URL，则复用该资源
    if existing_resource and not existing_resource.get("resource_url"):
        new_role_resource_id = selected_role_resource_id
        new_role_resource = {}
        new_role_resource["description"] = role_desc
        new_role_resource["description_en"] = description_en
        new_role_resource["style_type"] = project["style_type"]
        new_role_resource["style_type_desc"] = project["style_type_desc"]
    else:
        # 创建新资源
        new_role_resource_id = mongo_instance.generate_object_id()
                                                               
        new_role_resource = {
            "_id": new_role_resource_id,
            "user_id": user_id,
            "project_id": project_id,
            "role_id": role_id,
            "description": role_desc,
            "description_en": description_en,
            "style_type": project["style_type"],
            "style_type_desc": project["style_type_desc"],
            "voice_model_name": "",
            "face_image": "",
            "projection_image": []
        }
            
    # 根据角色描述生成提示词
    image_style = image_model.get_model_image_style(new_role_resource.get("style_type"))
    times_and_culture = project["times_and_culture_en"]
    role_system_prompt, role_prompt = get_role_image_prompt(new_role_resource["description_en"],image_style,times_and_culture)
    
    # logging.info(f"role_prompt: {role_prompt}")
    
    # 初始化变量，避免UnboundLocalError
    optimized_prompt = role_prompt
    height_percentage = 85
    image_size = None
    
    # 开始计时
    start_time = time.time()
    
    for attempt in range(MAX_RETRIES):  
        try:        
            # 提取角色和场景信息        
            messages = [
                {"role": "system", "content": role_system_prompt},
                {"role": "user", "content": role_prompt}
            ]
            
            #response = await llm_model.generate_content(messages, is_json=True, used_type = "generate_role_prompt")
            # logging.info(f"regenerate_role_image llm_role_prompt: {response}")
            
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
            logging.warning(f"Error in regenerate_role_image generate_role_prompt: {e}",exc_info=True)
            
        if attempt == MAX_RETRIES - 1:  # 最后一次重试
            logging.warning(f"Failed in regenerate_role_image generate_role_prompt after {MAX_RETRIES} attempts")
            optimized_prompt = role_prompt
            height_percentage = 85
            image_size = image_model.get_role_image_size_by_height_percentage(height_percentage) 
        else:
            logging.warning(f"Failed in regenerate_role_image generate_role_prompt after {attempt + 1} attempts, retrying...")
            await asyncio.sleep(2 ** attempt)  # 指数退避
            yield encode_sse_data("", event="heartbeat")
            
    end_time = time.time()
    duration = end_time - start_time
    logging.info(f"regenerate_role_prompt duration: {duration:.2f} seconds")
    
    # 开始计时
    start_time = time.time()
        
    #使用类型
    used_type = "regenerate_role_image"
                                       
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
                
            logging.error(f"Failed to regenerate image for role {role_name} in project {project_id}, reason is: {error_msg}")
            
            yield encode_sse_data(warning_msg, event="error")
            return
        else:
            # 计算耗时
            end_time = time.time()
            duration = end_time - start_time
            
            generate_id = generate_result["generate_id"]
            role_prompt = generate_result['image_prompt']
            role_image_url = generate_result['image_url']
            logging.info(f"Success to regenerate image for role {role_name} in project {project_id}, image_model: {image_model_name}, duration: {duration:.2f} seconds")
        
    except Exception as e:
        logging.error(f"Error in generate_character_image: {e}",exc_info=True)
        warning_msg = get_translation("failed_to_generate_image_for_role").format(role_name=role_name)
        yield encode_sse_data(warning_msg, event="error")
        return
  
    if role_image_url:
        # 更新角色资源
        new_role_resource["resource_url"] = role_image_url
        new_role_resource["resource_prompt"] = role_prompt
        new_role_resource["image_model_name"] = image_model_name
        new_role_resource["generate_seed"] = generate_seed
        new_role_resource["generate_id"] = generate_id
        new_role_resource["generate_status"] = "done"
        new_role_resource["image_size"] = image_size
        new_role_resource["last_updated_at"] = current_time
    
        # 如果是复用现有资源，则更新资源
        if existing_resource and not existing_resource.get("resource_url"):
            await mongo_instance.update_one(
                "role_resources",
                {"_id": new_role_resource_id},
                {"$set": new_role_resource}
            )
        else:
            # 否则插入新资源
            new_role_resource["created_at"] = current_time
            new_role_resource["created_at_str"] = beijing_formatted_time
            await mongo_instance.insert_one("role_resources", new_role_resource)
            
            # 更新角色信息，添加新资源ID到资源列表
            await mongo_instance.update_one(
                "roles",
                {
                    "_id": role_id,
                    "project_id": project_id,
                    "user_id": user_id
                },
                {
                    "$set": { 
                        "selected_role_resource_id": new_role_resource_id,
                        "last_updated_at": current_time,
                    },
                    "$push": { 
                        "role_resource_ids": {
                            "$each": [new_role_resource_id],
                            "$position": 0  # 将新ID插入到数组的开头位置
                        }
                    }
                }
            )
        
        #更新工程信息
        await mongo_instance.update_one(
            "projects",
            {
                "_id": project_id,
                "user_id": user_id
            },
            {
                "$set": {
                    "last_updated_at": current_time,
                }
            }
        )
        
        response_data = {
                "figureDesc": role_desc,
                "figureName": role_name,
                "url": role_image_url,
            }   
        
        #发送数据
        yield encode_sse_data(response_data)
        #发送成功标志
        yield encode_sse_data(get_translation("role_generate_success"), event="progress")
        #发送结束标志
        yield encode_sse_data("Complete")
        
    else:
        yield encode_sse_data(get_translation("role_generate_fail"), event="error")
        
@regenerate_router.get('/regenerate')
async def operator(projectId: str,roleId: str,figureName: str,figureDesc: str,figureExampleUrl: str):
    """重新生成角色形象
    
    Args:
        projectId: 项目ID
        roleId: 角色ID
        figureName: 角色名称
        figureDesc: 角色描述
        figureExampleUrl: 角色示例URL
        
    Returns:
        JSONResponse: 重新生成的角色信息
    """    

    # 获取当前用户ID
    user_id = get_user_id()
    
    # 转换为ObjectId
    project_id = mongo_instance.generate_object_id(projectId)
    
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
            
    role_id = mongo_instance.generate_object_id(roleId)
    
    role = await mongo_instance.find_one(
        "roles",
        {
            "_id": role_id,
            "project_id": project_id,
            "user_id": user_id
        }
    )
    
    if not role:
        return JSONResponse(content={
            "code": 1,
            "data": None,
            "msg": get_translation("role_not_exist_or_no_right"),
        })
        
    return StreamingResponse(
        regenerate_role_image(user_id, project_id, role_id,figureName,figureDesc),
        media_type='text/event-stream; charset=utf-8',
        headers={
            'Cache-Control': 'no-cache',
            'Connection': 'keep-alive',
        }
    )