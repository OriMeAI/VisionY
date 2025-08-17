from fastapi import APIRouter
from fastapi.responses import JSONResponse

pdf_router = APIRouter()

@pdf_router.post('/pdf')
async def operator():
    return JSONResponse(content={
        "code": 0,
        "data": None,
        "msg": "",
    })
