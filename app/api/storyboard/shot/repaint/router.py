from fastapi import APIRouter, Body
from fastapi.responses import JSONResponse,StreamingResponse
from app.models.model_factory import create_image_model, create_translator_model
from app.utils.mongo import mongo_instance
from app.utils.core import get_user_id,encode_sse_data
from app.locales.translations import get_translation
import logging, random, asyncio,time
from app.models.prompts.repaint_image import get_repaint_prompt_with_no_mask,get_repaint_prompt_with_mask

repaint_router = APIRouter()

async def repaint_image(
    user_id,project_id,shot_id,
    repaint_prompt,
    mask_data,
    origin_image_url,
    origin_image_width,
    origin_image_height
):
    """重绘分镜图的流式响应"""
    yield encode_sse_data("Connection successful")
    
    project = await mongo_instance.find_one(
        "projects",
        {
            "_id": project_id,
            "user_id": user_id,
            "status": "active"
        }
    )
                
    # 验证项目和镜头存在且用户有权限
    shot = await mongo_instance.find_one(
        "shots",
        {
            "_id": shot_id,
            "project_id": project_id,
            "user_id": user_id,
            "status": "active"
        }
    )
            
    image_model_name = project["image_model_name"]
    image_model = create_image_model(image_model_name)
    
    style_type = project["style_type"]
    image_size = f"{origin_image_width}x{origin_image_height}"
        
    # 获取翻译模型和图像模型
    translator_model = create_translator_model()
    
    # 开始计时
    start_time = time.time()
    
    used_type = "repaint_shot_image"
    
    # 生成随机种子
    generate_seed = random.randint(100000, 999999)

    # 翻译提示词
    translate_result = await translator_model.translate(repaint_prompt)
    
    if translate_result['code'] != 0:
        translated_prompt = repaint_prompt
    else:
        translated_prompt = translate_result["data"]
        
    if mask_data:
        prompt = get_repaint_prompt_with_mask(translated_prompt)
    else:
        prompt = get_repaint_prompt_with_no_mask(translated_prompt) 
                 
    #设置默认值
    generate_id, image_url, shot_repaint_prompt =  "", "", ""
    
    try:
        # 创建生图调用任务
        image_task = asyncio.create_task(
           image_model.repaint_image(used_type,seed = generate_seed,style_type = style_type,size = image_size,prompt = prompt,base_image = origin_image_url,mask_data = mask_data)
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
            warning_msg = f"Failed to repaint image for shot"
                    
            if generate_code == 2: # 积分不足
                error_msg = get_translation("credits_not_enough")
                warning_msg = error_msg
            
            elif generate_code == 7: # 提示词或者图片非法
                error_msg = get_translation("prompt_or_image_illegal")
                warning_msg = error_msg
            
            #不特殊处理其他类型                 
            logging.error(f"Failed to repaint image for shot {shot_id} in project {project_id}, reason is: {error_msg}")
            yield encode_sse_data(warning_msg, event="error")
            return
        else:
            # 计算耗时
            end_time = time.time()
            duration = end_time - start_time
            
            generate_id = generate_result["generate_id"]
            shot_repaint_prompt = generate_result['image_prompt']
            image_url = generate_result['image_url']
            logging.info(f"Success to repaint image for shot {shot_id} in project {project_id}, image_model: {image_model_name}, duration: {duration:.2f} seconds")
        
    except Exception as e:
        logging.error(f"Error in repaint_image: {e}",exc_info=True)
        warning_msg = f"Failed to repaint image for shot {shot_id}"
        yield encode_sse_data(warning_msg, event="error")
        return
        
    # 获取当前时间
    current_time, beijing_formatted_time, _ = mongo_instance.get_current_time()
    
    new_resource_id = mongo_instance.generate_object_id()
        
    # 创建新的镜头资源记录
    new_resource = {
        "_id": new_resource_id,
        "user_id": user_id,
        "project_id": project_id,
        "shot_id": shot_id,
        "image_model_name": image_model_name,
        "style_type": style_type,
        "style_type_desc": project.get("style_type_desc", ""),
        "image_size": image_size,
        "generate_seed": generate_seed,
        "generate_id": generate_id,
        "generate_status": "done",
        "resource_type": 1,  # 1表示图片
        "resource_url": image_url,
        "resource_prompt": shot_repaint_prompt,
        "is_HD": False,
        "last_updated_at": current_time,
        "created_at": current_time,
        "created_at_str": beijing_formatted_time
    }
    
    # 插入新的资源记录
    await mongo_instance.insert_one("shot_resources", new_resource)
    
    # 更新镜头的资源ID列表和当前选中的资源ID
    shot_resource_ids = shot.get("shot_resource_ids", [])
    shot_resource_ids.insert(0, new_resource_id)  # 将新资源ID添加到列表前面
    
    await mongo_instance.update_one(
        "shots",
        {"_id": shot_id},
        {
            "$set": {
                "shot_resource_ids": shot_resource_ids,
                "last_updated_at": current_time
            }
        }
    )
    
    # 更新项目的最后更新时间
    await mongo_instance.update_one(
        "projects",
        {"_id": project_id},
        {
            "$set": {
                "last_updated_at": current_time
            }
        }
    )
    
    #构造返回数据，查询所有镜头资源
    history_resources = []
    
    for resource_id in shot_resource_ids:
        resource = await mongo_instance.find_one(
            "shot_resources",
            {"_id": resource_id}
        )
        
        if resource:
            # 判断是否为当前选中的资源
            is_selected = str(resource_id) == str(new_resource_id)
            
            history_resources.append({
                "id": str(resource_id),
                "projectId": str(project_id),
                "storyboardId": str(shot_id),
                "selected": is_selected,
                "url": resource.get("resource_url", ""),
                "is_HD": resource.get("is_HD", False),
            })
        
    #发送数据
    yield encode_sse_data(history_resources)
    
    #发送成功标志
    yield encode_sse_data(get_translation("repaint_success"), event="progress")
    #发送结束标志
    yield encode_sse_data("Complete")
    
@repaint_router.post('/repaint')
async def operator(  
    projectId: str = Body(...),
    storyboardId: str = Body(...),
    imgPrompts: str = Body(...),
    maskData: str = Body(...),
    originImgUrl: str = Body(...),
    originImgWidth: int = Body(...),
    originImgHeight: int = Body(...)
):
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
        
    shot_id = mongo_instance.generate_object_id(storyboardId)
        
    # 验证项目和镜头存在且用户有权限
    shot = await mongo_instance.find_one(
        "shots",
        {
            "_id": shot_id,
            "project_id": project_id,
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
        repaint_image(user_id, project_id, shot_id,imgPrompts,maskData,originImgUrl,originImgWidth,originImgHeight),
        media_type='text/event-stream; charset=utf-8',
        headers={
            'Cache-Control': 'no-cache',
            'Connection': 'keep-alive',
        }
    )