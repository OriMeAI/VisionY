from fastapi import APIRouter
from fastapi.responses import JSONResponse

statistics_router = APIRouter()

@statistics_router.get('/statistics')
async def operator():
    return JSONResponse(
        content={
            "code": 0,
            "data": {
                "total": 100,
                "today": 10
            },
            "msg": ""
        }
    )