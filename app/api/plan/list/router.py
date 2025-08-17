from fastapi import APIRouter
from fastapi.responses import JSONResponse
from app.data.membership import get_membership_benefit_item

list_router = APIRouter()

@list_router.get('/list')
async def operator():
    item = get_membership_benefit_item()
    return JSONResponse(content={
        "code": 0,
        "data": item,
        "msg": ""
    })