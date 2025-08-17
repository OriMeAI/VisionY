from fastapi import APIRouter, Body
from fastapi.responses import JSONResponse
from app.models.model_factory import create_cdn_instance
import logging
from typing import Dict, Any
from app.locales.translations import get_translation
from app.utils.mongo import mongo_instance
from app.utils.core import get_user_id

upload_example_figure_router = APIRouter()

@upload_example_figure_router.post('/upload_example_figure')
async def upload_example_figure(
    projectId: str = Body(...),
    fileData: str = Body(...),
    fileName: str = Body(...),
):
    """
    上传示例人物图片
    
    接收前端发送的base64编码图像数据，并上传到Cloudflare
    
    Args:
        data: 包含fileData(base64数据)和fileName的字典
    
    Returns:
        JSONResponse: 上传结果，包含资源URL
    """
    
    # 获取当前用户ID
    user_id = get_user_id()
    
    # 转换为ObjectId
    project_id = mongo_instance.generate_object_id(projectId)
    
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
        
    #获取cdn实例
    cdn_instance = create_cdn_instance()
    
    # 调用cloudflare的upload_base64方法上传文件
    result = await cdn_instance.upload_base64(fileData, fileName)
    
    if result["status"] == "success":
      
        figure_url = result.get("resource_url", "")
        
        #1 验证人脸是否存在且角度正确
      
        return JSONResponse(content={
            "code": 0,
            "data": figure_url,
            "msg": get_translation("upload_success"),
        })
    else:
        logging.error(f"上传文件失败: {result}")
        return JSONResponse(content={
            "code": 1,
            "data": None,
            "msg": get_translation("server_error"),
        })