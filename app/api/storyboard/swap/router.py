from fastapi import APIRouter
from fastapi.responses import JSONResponse

swap_router = APIRouter()

@swap_router.post('/swap')
async def operator():
    return JSONResponse(content={
        "code": 0,
        "data": None,
        "msg": "",
    })

# export async function POST(request: Request) {
#   const res = await request.json();
#   console.log(res);
#   return Response.json({
#     code: 0,
#     data: null,
#     msg: "",
#   });
# }
