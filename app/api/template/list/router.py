from fastapi import APIRouter, Request, HTTPException
from fastapi.responses import JSONResponse
from app.locales.translations import get_project_template_item

list_router = APIRouter()

@list_router.get('/list')
async def operator():
    item =  get_project_template_item()
    return JSONResponse(content={
        "code": 0,
        "data": item,
        "msg": ""
    })