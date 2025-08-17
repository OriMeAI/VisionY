from fastapi import APIRouter, Body
from fastapi.responses import JSONResponse,StreamingResponse
from app.models.model_factory import create_image_model
from app.utils.mongo import mongo_instance
from app.utils.core import get_user_id,encode_sse_data
from app.locales.translations import get_translation
import logging, random,asyncio,time
from app.models.prompts.hd_resolution_image import get_hd_resolution_prompt
from typing import AsyncGenerator


hd_resolution_router = APIRouter()

async def generate_HD_image(user_id, project_id, shot_id) -> AsyncGenerator[bytes, None]: 
        
    """生成分镜高清图的流式响应"""
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
    
    #获取原始图片URL
    selected_shot_resource_id = shot.get("selected_shot_resource_id")

    shot_resource = await mongo_instance.find_one(
        "shot_resources",
        {
            "_id": selected_shot_resource_id,
            "project_id": project_id,
            "user_id": user_id,
            "shot_id": shot_id,
        }
    )
    
    resource_url = shot_resource.get("resource_url", "")
        
    image_model_name = project["image_model_name"]
    image_model = create_image_model(image_model_name)
    
    style_type = project["style_type"]
    image_size = project["image_size"]
    
    # 开始计时
    start_time = time.time()
    
    used_type = "hd_shot_image"
        
    # 生成随机种子
    generate_seed = random.randint(100000, 999999)
    
    prompt = get_hd_resolution_prompt()
            
    #设置默认值
    generate_id, image_url, shot_prompt =  "", "", ""
    
    try:
        # 创建生图调用任务
        image_task = asyncio.create_task(
           image_model.hd_resolution(used_type,seed = generate_seed,style_type= style_type,prompt = prompt,image_url = resource_url)
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
            warning_msg = f"Failed to generate HD image for shot"
                    
            if generate_code == 2: # 积分不足
                error_msg = get_translation("credits_not_enough")
                warning_msg = error_msg
            
            elif generate_code == 7: # 提示词或者图片非法
                error_msg = get_translation("prompt_or_image_illegal")
                warning_msg = error_msg
            
            #不特殊处理其他类型                 
            logging.error(f"Failed to generate HD image for shot {shot_id} in project {project_id}, reason is: {error_msg}")
            yield encode_sse_data(warning_msg, event="error")
            return
        else:
            # 计算耗时
            end_time = time.time()
            duration = end_time - start_time
            
            generate_id = generate_result["generate_id"]
            shot_prompt = generate_result['image_prompt']
            image_url = generate_result['image_url']
            logging.info(f"Success to hd_resolution image for shot {shot_id} in project {project_id}, image_model: {image_model_name}, duration: {duration:.2f} seconds")
        
    except Exception as e:
        logging.error(f"Error in hd_resolution: {e}",exc_info=True)
        warning_msg = f"Failed to generate HD image for shot {shot_id}"
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
        "resource_prompt": shot_prompt,
        "is_HD": True,
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
                "selected_shot_resource_id": new_resource_id,
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
    
    response_data = {
        "shot_resource_id": str(new_resource_id),
        "is_HD": True,
        "shot_resource_url": image_url
    }
    
    #发送数据
    yield encode_sse_data(response_data)
    
    #发送成功标志
    yield encode_sse_data(get_translation("generate_HD_success"), event="progress")
    #发送结束标志
    yield encode_sse_data("Complete")
        
@hd_resolution_router.get('/hd_resolution')
async def operator( projectId: str, storyboardId: str):
    """生成分镜高清图像
    
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
        
    #获取原始图片URL
    selected_shot_resource_id = shot.get("selected_shot_resource_id")

    shot_resource = await mongo_instance.find_one(
        "shot_resources",
        {
            "_id": selected_shot_resource_id,
            "project_id": project_id,
            "user_id": user_id,
            "shot_id": shot_id,
        }
    )
        
    if not shot_resource:
        return JSONResponse(content={
            "code": 1,
            "data": None,
            "msg": get_translation("shot_resource_not_found_or_no_right"),
        })
        
    is_HD = shot_resource.get("is_HD", False)
    resource_url = shot_resource.get("resource_url", "")
    
    if is_HD:
        response_data = {
            "shot_resource_id": str(selected_shot_resource_id),
            "is_HD": True,
            "shot_resource_url": resource_url
        }
        return JSONResponse(content={
            "code": 0,
            "data": response_data,
            "msg": get_translation("shot_resource_is_HD"),
        })
        
    return StreamingResponse(
        generate_HD_image(user_id, project_id, shot_id),
        media_type='text/event-stream; charset=utf-8',
        headers={
            'Cache-Control': 'no-cache',
            'Connection': 'keep-alive',
        }
    )