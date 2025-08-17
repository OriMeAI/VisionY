import sys
import os
import time
from fastapi import Request
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# from app.utils.core import fast_app
from fastapi import FastAPI, Response # 确保导入 Response
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.sessions import SessionMiddleware
import logging,os
from app.utils.core import is_running_in_docker
from init_env import initialize_environment_variables
import uvicorn

# 初始化环境变量
initialize_environment_variables()

# 是否为开发环境
# is_dev = os.getenv('ENV', 'dev') == 'dev'
is_dev = is_running_in_docker()

# 日志处理
from app.utils.log import register_log_handlers
register_log_handlers()

#定义fastapi
fast_app = FastAPI()

# 配置 CORS
fast_app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["Content-Disposition"]  # 添加这一行
)

# 添加 SessionMiddleware，使用一个安全的随机密钥
fast_app.add_middleware(SessionMiddleware, os.getenv("SESSION_SECRET_KEY", "dev-secret-key")) #secret_key=secrets.token_urlsafe(32)

# 错误处理
from app.utils.exception import register_exception_handlers
register_exception_handlers(fast_app)

# 全局钩子函数
from app.utils.hook import register_hook_handlers
register_hook_handlers(fast_app)

# 在FastAPI中添加中间件监控响应时间
@fast_app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    return response

# 初始化 Mongo 连接
from app.utils.mongo import mongo_instance
if mongo_instance.is_available():
    logging.info("Mongo connection initialized")
else:
    logging.warning("Mongo not available")

# 初始化 Redis 连接
from app.utils.redis_client import redis_instance
if redis_instance.is_available():
    logging.info("Redis connection initialized")
else:
    logging.warning("Redis not available")

#注册auth
from app.utils.auth import auth_instance
auth_instance.register_google_auth()

#注册支付
from app.utils.stripe import stripe_instance
stripe_instance.register_stripe()

# api接口
from app.api.router import api_router
fast_app.include_router(api_router)

# 记录日志
logging.info("System Start Successfully")


if __name__ == "__main__":
    uvicorn.run("main:fast_app", host="0.0.0.0", port=3000, reload=True)