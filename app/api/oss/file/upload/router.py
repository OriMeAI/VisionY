from fastapi import APIRouter
from fastapi.responses import JSONResponse

#叶子节点的blueprint不加url_prefix
upload_router = APIRouter()

@upload_router.post('/upload')
async def operator():
    return JSONResponse(content={
        "code": 0,
        "data": "https://static.chuangyi-keji.com/2025/02/16/assets/png/aa4d2bad-35ac-4c2a-ab4c-965eb67a1fea.png",
        "msg": "",
    })