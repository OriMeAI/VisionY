from fastapi import APIRouter
from fastapi.responses import JSONResponse

img_router = APIRouter()

@img_router.post('/img')
async def operator():
    return JSONResponse(content={
        "code": 0,
        "data": None,
        "msg": "",
    })