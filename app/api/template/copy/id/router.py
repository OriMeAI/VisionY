from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse
from app.utils.mongo import mongo_instance
from app.collections.project import copy_project_from_template
from app.collections.user import is_project_count_exceeded
from app.utils.core import get_user_id
import logging
from app.locales.translations import get_translation

id_router = APIRouter()

@id_router.post('/{id}')
async def operator(id: str):
    user_id = get_user_id()
    if not user_id:
        return JSONResponse(content={
            "code": 800,
            "data": {},
            "msg": get_translation("user_not_login"),
        })
        
    #检查用户是否超过项目数量限制
    if await is_project_count_exceeded(user_id):
        return JSONResponse(content={
            "code": 400,
            "msg": get_translation("project_count_exceeded"),
            "data": {}
        })
            
    project_id = await copy_project_from_template(user_id, id)
    
    if not project_id:
        return JSONResponse(content={
            "code": 400,
            "data": "",
            "msg": get_translation("copy_project_failed")
        })
    else:
        return JSONResponse(content={
            "code": 0,
            "data": str(project_id),
            "msg": ""
        })