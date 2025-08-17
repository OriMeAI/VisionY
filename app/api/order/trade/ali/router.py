from fastapi import APIRouter
from fastapi.responses import JSONResponse

ali_router = APIRouter()

@ali_router.get('/ali')
async def operator():
    return JSONResponse(content={
        "code": 0,
        "data": {
            "tradeStatus": "",
            "tradeNo": None,
            "outTradeNo": "732604612766334976",
            "sellId": None,
            "payType": "ALIPAY",
        },
        "msg": "",
    })