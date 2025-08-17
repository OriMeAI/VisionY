from fastapi import APIRouter
from fastapi.responses import JSONResponse
from app.locales.translations import get_stories_list

#叶子节点的blueprint不加url_prefix
stories_router = APIRouter()

@stories_router.get('/stories')
async def operator():
    stories_slit = get_stories_list()
    
    return JSONResponse(content={
        "code": 0,
        "data": stories_slit,
        "msg": "",
    })
