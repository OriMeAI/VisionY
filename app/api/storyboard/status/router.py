from fastapi import APIRouter
from fastapi.responses import JSONResponse

status_router = APIRouter()

@status_router.post('/status')
async def operator():
    return JSONResponse(content={
      "code": 0,
      "data": {
        "projectId": "66699bde3ec82564807be2236059e891",
        "storyboardId": "1883085092151447553",
        "status": "done",
        "resultUrl":"https://static.chuangyi-keji.com/generate_figure_images/69cc9a3269148463/5d8f9a56589cf507/d95c573102bf56998c48f0afa8693f2e.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,size_18,text_b25lc3RvcnkuYXJ0IEFJ55Sf5oiQ,color_FFFFFF,shadow_50,t_100,g_se,x_10,y_10",
        "queuePosition": None,
      },
      "msg": "",
    })

# export async function POST(request: Request) {
#   const res = await request.json();
#   return Response.json({
#     code: 0,
#     data: {
#       projectId: "66699bde3ec82564807be2236059e891",
#       storyboardId: "1883085092151447553",
#       status: "done",
#       resultUrl:
#         "https://static.chuangyi-keji.com/generate_figure_images/69cc9a3269148463/5d8f9a56589cf507/d95c573102bf56998c48f0afa8693f2e.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,size_18,text_b25lc3RvcnkuYXJ0IEFJ55Sf5oiQ,color_FFFFFF,shadow_50,t_100,g_se,x_10,y_10",
#       queuePosition: null,
#     },
#     msg: "",
#   });
# }
