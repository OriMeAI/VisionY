from fastapi import APIRouter
from fastapi.responses import JSONResponse

#叶子节点的blueprint不加url_prefix
purchase_router = APIRouter()

@purchase_router.post('/purchase')
async def operator():
    return JSONResponse(
        content={
            "code": 0,
            "data": None,
            "msg": ""
        }
    )