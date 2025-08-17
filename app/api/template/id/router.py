from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse
from app.utils.mongo import mongo_instance
from app.locales.translations import get_translation,get_project_description_item
import logging

id_router = APIRouter()

@id_router.get('/{id}')
async def operator(id: str):    
    # 先从数据库获取项目信息
    project = await mongo_instance.find_one(
        "projects", 
        {
            "_id": mongo_instance.generate_object_id(id),
            "status": "active"
        }
    )
    
    if project:
        # 如果在数据库中找到项目，返回项目信息
        project_data = {
            "id": str(project["_id"]),
            "name": project.get("project_name", ""),
            "type": project.get("proect_type", 0),
            "storyBoardType": project.get("story_board_type", 1),
            "storyBoardTypeDesc": project.get("story_board_type_desc", ""),
            "pictureSize": project.get("picture_size", "16:9"),
            "cover": project.get("cover", ""),
            "scriptType": project.get("script_type", 1),
            "content": project.get("script_content", ""),
        }
                
        return JSONResponse(content={
            "code": 0,
            "data": project_data,
            "msg": ""
        })
    else:
        # 如果数据库中没有，从模板获取
        item = get_project_description_item(id)
        
        if item is not None:
            return JSONResponse(content={
                "code": 0,
                "data": item,
                "msg": ""
            })
        else:
            # 如果模板中也没有，返回错误信息
            logging.error(f"Project template with id {id} not found")
            return JSONResponse(content={
                "code": 404,
                "data": {},
                "msg": get_translation("project_template_not_found")
            })