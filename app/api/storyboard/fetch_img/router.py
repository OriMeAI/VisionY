from fastapi import APIRouter
from fastapi.responses import JSONResponse

fetch_img_router = APIRouter()

@fetch_img_router.post('/fetch_img')
async def operator():
    return JSONResponse(content={
        "code": 0,
        "data": [
            {
                "storyboardId": "1891621816154787842",
                "storyHeadId": 3,
                "cellValue": '{"image":"https://static.chuangyi-keji.com/generate_figure_images/69cc9a3269148463/c26472b272342af7/aa5218e71f41d748c60bfa7fddf24943.png","isHd": false}',
            },
            {
                "storyboardId": "1891621829446303746",
                "storyHeadId": 3,
                "cellValue": '{"image":"https://static.chuangyi-keji.com/generate_figure_images/69cc9a3269148463/c26472b272342af7/dc8783c6b1260c93f987d4ddd3ee62a6.png","isHd": false}',
            },
            {
                "storyboardId": "1891621841823928322",
                "storyHeadId": 3,
                "cellValue": '{"image":"https://static.chuangyi-keji.com/generate_figure_images/69cc9a3269148463/c26472b272342af7/6168df6ab3a6a2bb38715244e9721699.png","isHd": false}',
            },
            {
                "storyboardId": "1891621854557601793",
                "storyHeadId": 3,
                "cellValue": '{"image":"https://static.chuangyi-keji.com/generate_figure_images/69cc9a3269148463/c26472b272342af7/fdf0b73d5e3e03a1a4f395245f4a08c3.png","isHd": false}',
            },
            {
                "storyboardId": "1891621867136552962",
                "storyHeadId": 3,
                "cellValue": '{"image":"https://static.chuangyi-keji.com/generate_figure_images/69cc9a3269148463/c26472b272342af7/9d32f7a6254847ea19c4d4c28561fc94.png","isHd": false}',
            },
            {
                "storyboardId": "1891621879685677057",
                "storyHeadId": 3,
                "cellValue": '{"image":"https://static.chuangyi-keji.com/generate_figure_images/69cc9a3269148463/c26472b272342af7/cf56c3d38d596126714d71b6b83cb04b.png","isHd": false}',
            },
            {
                "storyboardId": "1891621903488585729",
                "storyHeadId": 3,
                "cellValue": '{"image":"https://static.chuangyi-keji.com/generate_figure_images/69cc9a3269148463/c26472b272342af7/d87306ec173d69b54df9ecf478322a5a.png","isHd": false}',
            },
            {
                "storyboardId": "1891621909087748097",
                "storyHeadId": 3,
                "cellValue": '{"image":"https://static.chuangyi-keji.com/generate_figure_images/69cc9a3269148463/c26472b272342af7/4fbabae2cecfba9a9599ae2afac79685.png","isHd": false}',
            },
            {
                "storyboardId": "1891621922346176513",
                "storyHeadId": 3,
                "cellValue": '{"image":"https://static.chuangyi-keji.com/generate_figure_images/69cc9a3269148463/c26472b272342af7/4fbabae2cecfba9a9599ae2afac79685.png","isHd": false}',
            },
            {
                "storyboardId": "1891621933569900545",
                "storyHeadId": 3,
                "cellValue": '{"image":"https://static.chuangyi-keji.com/generate_figure_images/69cc9a3269148463/c26472b272342af7/4fbabae2cecfba9a9599ae2afac79685.png","isHd": false}',
            },
        ],
        "msg": "",
    })