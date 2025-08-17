from fastapi import APIRouter
from fastapi.responses import JSONResponse
from app.models.model_factory import create_image_model

#叶子节点的blueprint不加url_prefix
style_router = APIRouter()

@style_router.get('/style')
async def operator():
    image_model = create_image_model()
    style_list = image_model.get_style_list()
    image_size_list = image_model.get_image_size_list()
    return JSONResponse(content={
        "code": 0,
        "data": {
            "styleDataList":style_list,
            "pictureSizeList":image_size_list
            },
        "msg": "",
    })
