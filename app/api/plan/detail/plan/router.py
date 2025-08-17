from fastapi import APIRouter
from fastapi.responses import JSONResponse

#叶子节点的blueprint不加url_prefix
plan_router = APIRouter()

@plan_router.get('/plan')
async def operator():
    return JSONResponse(content={
        "code": 0,
        "data": {
            "id": 6,
            "name": "普通会员",
            "icon": "Layers2",
            "price": "299",
            "cycle": "ANNUAL",
            "addonValue": None,
            "features": [
                "角色库上传参考图片解除限制",
                "可使用的项目数为100个",
                "每月可获得120次免费生图次数",
                "每月赠送600次生图次数",
                "单个项目创意字符数8000字"
            ],
            "addonFeatures": None,
            "description": "每人/每年"
        },
        "msg": ""
    })