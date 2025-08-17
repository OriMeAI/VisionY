from fastapi import APIRouter
from fastapi.responses import JSONResponse

#叶子节点的blueprint不加url_prefix
credit_router = APIRouter()

@credit_router.get('/credit')
async def operator():
    return JSONResponse(content={
        "code": 0,
        "data": {
            "id": 5,
            "name": "生图次数",
            "icon": None,
            "price": "1",
            "cycle": None,
            "addonValue": 20,
            "features": None,
            "addonFeatures": '{"discount": 20}',
            "description": "文生图20次"
        },
        "msg": ""
    })