from fastapi import APIRouter, Body
from fastapi.responses import JSONResponse
from app.models.model_factory import create_cdn_instance
import logging, random
from app.locales.translations import get_translation
from app.utils.mongo import mongo_instance
from app.utils.core import get_user_id
from datetime import datetime

pic_upload_router = APIRouter()

@pic_upload_router.post('/pic_upload')
async def operator(
    shotId: str = Body(...),
    projectId: str = Body(...),
    fileData: str = Body(...),
    fileName: str = Body(...),
):
    """
    上传镜头图片
    
    接收前端发送的base64编码图像数据，并上传到Cloudflare，然后更新镜头资源
    
    Args:
        shotId: 镜头ID
        projectId: 项目ID
        fileData: base64编码的图片数据
        fileName: 文件名
    
    Returns:
        JSONResponse: 上传结果，包含资源URL
    """
    
    # 获取当前用户ID
    user_id = get_user_id()
    
    # 转换为ObjectId
    project_id = mongo_instance.generate_object_id(projectId)
    shot_id = mongo_instance.generate_object_id(shotId)
    
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
    
    # 验证项目和镜头存在且用户有权限
    shot = await mongo_instance.find_one(
        "shots",
        {
            "_id": shot_id,
            "project_id": project_id,
            "status": "active"
        }
    )
    
    if not shot: 
        return JSONResponse(content={
            "code": 1,
            "data": None,
            "msg": get_translation("shot_not_found_or_no_right"),
        })
        
    cdn_instance = create_cdn_instance()
    
    # 调用cloudflare的upload_base64方法上传文件
    result = await cdn_instance.upload_base64(fileData, fileName)
    
    if result["status"] == "success":
        # 获取上传成功的图片URL
        resource_url = result.get("resource_url", "")
        
        generate_seed = random.randint(100000, 999999) #生成种子,用户生成图片或者视频
        
        new_resource_id = mongo_instance.generate_object_id()
        
        # 获取当前时间
        current_time, beijing_formatted_time, _ = mongo_instance.get_current_time()
        
        # 创建新的镜头资源记录
        new_resource = {
            "_id": new_resource_id,
            "user_id": user_id,
            "project_id": project_id,
            "shot_id": shot_id,
            "image_model_name": project.get("image_model_name", ""),
            "style_type": project.get("style_type", 0),
            "style_type_desc": project.get("style_type_desc", ""),
            "image_size": project.get("image_size", ""),
            "generate_seed": project.get("generate_seed", generate_seed),
            "generate_id": "",
            "generate_status": "done",
            "resource_type": 1,  # 1表示图片
            "resource_url": resource_url,
            "resource_prompt": "",
            "is_HD": False,
            "last_updated_at": current_time,
            "created_at": current_time,
            "created_at_str": beijing_formatted_time
        }
        
        # 插入新的资源记录
        await mongo_instance.insert_one("shot_resources", new_resource)
                
        # 更新镜头的资源ID列表和当前选中的资源ID
        shot_resource_ids = shot.get("shot_resource_ids", [])
        # 将新资源ID添加到列表前面，而不是末尾
        shot_resource_ids.insert(0, new_resource_id)
        
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
        
        return JSONResponse(content={
            "code": 0,
            "data": {
                    "shot_resource_id": str(new_resource_id),
                    "is_HD": False, 
                    "shot_resource_url": resource_url,
                },
            "msg": get_translation("upload_success"),
        })
    else:
        logging.error(f"上传文件失败: {result}")
        return JSONResponse(content={
            "code": 1,
            "data": None,
            "msg": get_translation("server_error"),
        })