from fastapi import APIRouter, Query
from fastapi.responses import JSONResponse
from app.utils.mongo import mongo_instance
from app.utils.core import get_user_id
from datetime import datetime
import logging
from app.locales.translations import get_translation

delete_router = APIRouter()

@delete_router.post('/delete')
async def operator(id: str = Query(...)):
    user_id = get_user_id()
    project_id = mongo_instance.generate_object_id(id)
        
    # 更新项目状态为 inactive
    current_time,_,_ = mongo_instance.get_current_time()
    result = await mongo_instance.update_one(
        "projects",
        {"_id": project_id,"user_id": user_id,"status": "active",},
        {
            "$set": {
                "status": "inactive",
                "last_updated_at": current_time
            }
        }
    )
    
    if result and result.modified_count > 0:
        logging.info(f"user {user_id} delete project {project_id} successfully.")
        return JSONResponse(content={
            "code": 0,
            "data": None,
            "msg": get_translation("delete_project_success"),
        })
    else:
        return JSONResponse(content={
            "code": 801,
            "data": None,
            "msg": get_translation("delete_project_failed"),
        })
