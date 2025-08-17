from fastapi import APIRouter
from fastapi.responses import JSONResponse

verify_router = APIRouter()

@verify_router.post('/verify')
async def operator():
    return JSONResponse(
        content={
            "code": 0,
            "data": "captcha:1_1597983992_1889003138522202112",
            "msg": ""
        }
    )