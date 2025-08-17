from fastapi import APIRouter, Query
from fastapi import APIRouter, Query
from fastapi.responses import JSONResponse
from app.utils.mongo import mongo_instance
from app.utils.core import get_user_id
from app.locales.translations import get_translation

info_router = APIRouter()

@info_router.get('/info')
async def operator(id: str = Query(...)):
    user_id = get_user_id()
    project_id = id
    
    # 查询项目信息
    project = await mongo_instance.find_one(
        "projects",
        {
            "_id": mongo_instance.generate_object_id(project_id),
            "user_id": user_id,
            "status": "active"
        }
    )
    
    if not project:
        return JSONResponse(content={
            "code": 801,
            "data": None,
            "msg": get_translation("project_not_found"),
        })
    
    # 转换数据格式
    response_data = {
        "id": project_id,
        "name": project.get("project_name", ""),
        "type": project.get("project_type", 2),
        "storyBoardType": project.get("style_type", 2),
        "storyBoardTypeDesc": project.get("style_type_desc"),
        "pictureSize": project.get("picture_size", "16:9"),
        "cover": project.get("cover"),
        "scriptType": project.get("script_type", 2),
        "hasShot": project.get("has_shot", False),
        "hasRole": project.get("has_role", False),
        "hasStoryboard": project.get("has_storyboard", False),
        "updateTime": mongo_instance.get_local_formatted_time(project.get("last_updated_at")) if project.get("last_updated_at") else None,
        "content": project.get("script_content", ""),
        "hasAuth": True,
        # 默认图片尺寸，可以根据实际需求调整
        # "imgWidth": 1344,
        # "imgHeight": 768
    }
    
    return JSONResponse(content={
        "code": 0,
        "data": response_data,
        "msg": "",
    })
