from fastapi import APIRouter
from fastapi.responses import JSONResponse

script_to_shot_router = APIRouter()

@script_to_shot_router.post('/script_to_shot')
async def operator():
    return JSONResponse(content={
        "code": 0,
        "data": None,
        "msg": "",
    })

# // 确认生成分镜
# export async function POST(request: Request) {
#   const res = await request.json();
#   console.log(res);
#   return Response.json({
#     code: 0,
#     data: null,
#     msg: "",
#   });
# }
