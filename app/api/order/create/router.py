from fastapi import APIRouter
from fastapi.responses import JSONResponse

#叶子节点的blueprint不加url_prefix
create_router = APIRouter()

@create_router.post('/create')
async def operator():
    return JSONResponse(content={
        "code": 0,
        "data": {
            "planId": None,
            "orderNo": "732604612766334976"
        },
        "msg": ""
    })