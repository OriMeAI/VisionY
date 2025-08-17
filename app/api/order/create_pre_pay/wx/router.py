from fastapi import APIRouter
from fastapi.responses import JSONResponse

wx_router = APIRouter()

@wx_router.get('/wx')
async def operator():
    return JSONResponse(content={
        "code": 0,
        "data": {
            "tradeStatus": "NOTPAY",
            "tradeNo": None,
            "outTradeNo": "732604612766334976",
            "sellId": "1676109379",
            "payType": "WECHAT",
        },
        "msg": "",
    })