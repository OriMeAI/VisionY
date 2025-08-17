from fastapi import APIRouter
from fastapi.responses import JSONResponse

#叶子节点的blueprint不加url_prefix
list_router = APIRouter()

@list_router.get('/list')
async def operator():
    return JSONResponse(content={
        "code": 0,
        "data": [
            {
                "planId": 1,
                "monthly": {
                    "price": "0",
                    "name": "免费用户",
                    "desc": "试用"
                },
                "annual": {
                    "price": "0",
                    "name": "免费用户",
                    "desc": "试用"
                },
                "benefit": {
                    "project_count": 10,
                    "face_swap_count": 2,
                    "image_generation_count": 120,
                    "project_content_length": 3000
                },
                "featuresExt": [
                    {
                        "title": "每月赠送生图次数",
                        "desc": "每个自然月赠送120次免费生图次数，未使用完不会结转至次月"
                    },
                    {
                        "title": "参考图片试用2次",
                        "desc": "使用角色库上传参考图片功能生成2张角色图片"
                    },
                    {
                        "title": "最大项目数10个",
                        "desc": "项目库的最大项目数量为10个"
                    },
                    {
                        "title": "文本长度3000字",
                        "desc": "单个项目的最大文本字符总数为3000字"
                    }
                ]
            },
            {
                "planId": 2,
                "monthly": {
                    "price": "29",
                    "name": "普通会员",
                    "desc": "每人/每月"
                },
                "annual": {
                    "price": "299",
                    "name": "普通会员",
                    "desc": "每人/每年"
                },
                "benefit": {
                    "project_count": 100,
                    "face_swap_count": -1,
                    "image_generation_count": 600,
                    "project_content_length": 8000
                },
                "featuresExt": [
                    {
                        "title": "每月赠送生图次数",
                        "desc": "每个自然月赠送120次免费生图次数，未使用完不会结转至次月"
                    },
                    {
                        "title": "参考图片上传",
                        "desc": "无限制使用角色库的上传参考图片功能"
                    },
                    {
                        "title": "最大项目数100个",
                        "desc": "项目库的最大项目数量为100个"
                    },
                    {
                        "title": "订阅赠送生图次数",
                        "desc": "普通会员订阅生效后，可获得生图次数600次/月，订阅有效期结束后清零。"
                    },
                    {
                        "title": "文本长度8000字",
                        "desc": "单个项目的最大文本字符总数为8000字"
                    }
                ]
            },
            {
                "planId": 3,
                "monthly": {
                    "price": "49",
                    "name": "高级会员",
                    "desc": "每人/每月"
                },
                "annual": {
                    "price": "499",
                    "name": "高级会员",
                    "desc": "每人/每年"
                },
                "benefit": {
                    "project_count": 500,
                    "face_swap_count": -1,
                    "image_generation_count": 2000,
                    "project_content_length": 15000
                },
                "featuresExt": [
                    {
                        "title": "每月赠送生图次数",
                        "desc": "每个自然月赠送120次免费生图次数，未使用完不会结转至次月"
                    },
                    {
                        "title": "参考图片上传",
                        "desc": "无限制使用角色库的上传参考图片功能"
                    },
                    {
                        "title": "最大项目数500个",
                        "desc": "项目库的最大项目数量为500个"
                    },
                    {
                        "title": "订阅赠送生图次数",
                        "desc": "高级会员订阅生效后，可获得生图次数2000次/月，订阅有效期结束后清零。"
                    },
                    {
                        "title": "文本长度15000字",
                        "desc": "单个项目的最大文本字符总数为15000字"
                    }
                ]
            },
            {
                "planId": 4,
                "monthly": {
                    "price": None,
                    "name": "团队会员",
                    "desc": "定制"
                },
                "annual": {
                    "price": None,
                    "name": "团队会员",
                    "desc": "定制"
                },
                "benefit": {
                    "project_count": None,
                    "face_swap_count": None,
                    "image_generation_count": None,
                    "project_content_length": None
                },
                "featuresExt": None
            }
        ],
        "msg": ""
    })