from fastapi import APIRouter, Request, Depends
from fastapi.responses import JSONResponse
from app.utils.mongo import mongo_instance
from app.utils.core import get_user_id

benefit_router = APIRouter()

@benefit_router.get('/benefit')
async def operator():
    user_id = get_user_id()
    
    user = await mongo_instance.find_one("users", {"_id": user_id})
    total_count = user.get("project_count_limit", 0)
    
    used_count = await mongo_instance.count("projects", {
        "user_id": user_id,
        "status": "active"
    })
    
    return JSONResponse(content={
        "code": 0,
        "data": {
            "totalCount": total_count,
            "usedCount": used_count,
        },
        "msg": "",
    })
