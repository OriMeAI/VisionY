from fastapi import APIRouter
from fastapi.responses import JSONResponse

video_router = APIRouter()

@video_router.post('/video')
async def operator():
    return JSONResponse(content={
        "code": 10506,
        "data": None,
        "msg": "操作失败",
    })