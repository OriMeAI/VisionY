from fastapi import APIRouter, Request, Body
from pydantic import BaseModel
from fastapi.responses import JSONResponse
from app.utils.mongo import mongo_instance
from datetime import datetime
import random  # 添加random模块导入
import logging

from app.collections.user import is_project_count_exceeded
from app.utils.core import get_user_id

from app.models.model_factory import create_image_model
from app.locales.translations import get_translation

project_router = APIRouter()

# 新增请求模型
class ProjectCreateRequest(BaseModel):
    name: str
    storyBoardType: int
    content: str  # 文件内容文本
    scriptType: int  # 剧本类型（需要与前端枚举值对应）
    aspectRatio: str

@project_router.post('/project')
async def operator(request: ProjectCreateRequest = Body(...)):
    # 获取用户ID
    user_id = get_user_id()   
    
    if await is_project_count_exceeded(user_id):
        return JSONResponse(content={
            "code": 400,
            "msg": get_translation("need_upgrade_membership_level"),
            "data": {}
        })
        
     
    # 获取当前时间
    current_time, beijing_formatted_time, _ = mongo_instance.get_current_time()
    
    # 创建新项目ID
    project_id = mongo_instance.generate_object_id()
    
    # 获取风格描述
    image_model = create_image_model()
    image_model_name = image_model.get_model_name()
    style_list = image_model.get_style_list()
    
    #获取风格名称
    style_type_desc = ""
    for style in style_list:
        if style.get("type") == request.storyBoardType:
            style_type_desc = style.get("name", "")
            break
        
    #获取图片尺寸
    image_size = image_model.get_image_size_by_aspect_ratio(request.aspectRatio)
            
    # 创建项目基本信息
    new_project = {
        "_id": project_id,
        "user_id": user_id,
        "status": "active",
        "project_language": "",  # 默认使用中文
        "project_name": request.name,
        "project_type": 0,  # 0表示新建项目
        "image_model_name": image_model_name   ,  # 初始为空
        "style_type": request.storyBoardType,
        "style_type_desc": style_type_desc,
        "picture_size": request.aspectRatio,
        "image_size": image_size,
        "cover": "",  # 初始为空
        "script_type": request.scriptType,
        "script_content": request.content,
        "times_and_culture": "",  # 添加年代和文化元素
        "times_and_culture_en": "",  # 添加英文版的年代和文化元素
        "has_shot": False,
        "has_role": False,
        "has_storyboard": False,
        "generate_seed": random.randint(100000, 999999), #生成种子,用户生成图片或者视频
        "shot_ids": [],  # 添加镜头ID列表
        "role_ids": [],
        "voiceover_model_name": "",  # 添加旁白音效模型
        "last_updated_at": current_time,
        "created_at": current_time,
        "created_at_str": beijing_formatted_time
    }
    
    # 插入数据库
    await mongo_instance.insert_one("projects", new_project)
    
    logging.info(f"User {user_id} create project {project_id} successfully.")
    
    # 返回成功响应
    return JSONResponse(content={
        "code": 0,
        "data": {
            "id": str(project_id),
        },
        "msg": "Create success",
    })