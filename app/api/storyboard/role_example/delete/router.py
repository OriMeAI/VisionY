from fastapi import APIRouter
from fastapi.responses import JSONResponse

delete_router = APIRouter()

@delete_router.post('/delete')
async def operator():
    return JSONResponse(content={
        "code": 0,
        "data": None,
        "msg": "",
    })

# // 删除上传人脸参考图
# // export async function POST(request: Request) {
# //   const res = await request.json();
# //   console.log(res);
# //   return Response.json({
# //     code: 0,
# //     data: null,
# //     msg: "",
# //   });
# // }
