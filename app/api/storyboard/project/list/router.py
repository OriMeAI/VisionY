from fastapi import APIRouter, Request, Query
from fastapi.responses import JSONResponse
from app.utils.mongo import mongo_instance
from datetime import datetime
from app.utils.core import get_user_id

list_router = APIRouter()

@list_router.get('/list')
async def operator(
    page_size: int = Query(default=20, alias="pageSize"),
    page_num: int = Query(default=1, alias="pageNum")
):
    user_id = get_user_id()
    
    query = {
        "user_id": user_id,
        "status": "active"
    }
    
    total = await mongo_instance.count("projects", query)
    pages = (total + page_size - 1) // page_size
    skip = (page_num - 1) * page_size
    
    projects = await mongo_instance.find_many(
        "projects", 
        query, 
        sort=[("last_updated_at", -1)],
        skip=skip,
        limit=page_size
    )
    
    records = []
    for project in projects:
        last_updated = project.get("last_updated_at")
        if isinstance(last_updated, (int, float)):
            update_time = datetime.fromtimestamp(last_updated).strftime("%Y-%m-%dT%H:%M:%S")
        else:
            update_time = mongo_instance.get_local_formatted_time(last_updated) if last_updated else ""
        
        records.append({
            "id": str(project.get("_id")),
            "name": project.get("project_name"),
            "type": project.get("project_type"),
            "storyBoardType": project.get("style_type"),
            "storyBoardTypeDesc": project.get("style_type_desc"),
            "pictureSize": project.get("picture_size"),
            "cover": project.get("cover"),
            # "hasRole": project.get("has_role"),
            # "hasShot": project.get("has_shot"),
            # "hasStoryboard": project.get("has_storyboard"),
            "updateTime": update_time
        })
    
    return JSONResponse(content={
        "code": 0,
        "data": {
            "records": records,
            "total": total,
            "pages": pages,
            "pageNum": page_num,
            "pageSize": page_size
        },
        "msg": ""
    })
