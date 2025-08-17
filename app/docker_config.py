import multiprocessing

# 通用配置
bind = '0.0.0.0:3000'
workers = multiprocessing.cpu_count() * 2 + 1
worker_class = 'uvicorn.workers.UvicornWorker'

# 生产环境配置
reload = False
daemon = False
pidfile = 'gunicorn.pid'
# 对于 SSE 应用的优化配置
timeout = 300  # 增加到 5 分钟，适合长时间的 SSE 连接
keepalive = 2  # 保持不变，对 SSE 影响不大

# 可以添加的其他配置
worker_connections = 1000  # 增加每个 worker 的连接数
max_requests = 0  # 禁用请求数限制，避免 SSE 连接被意外重启

# 日志配置
# accesslog = None  # 使用自定义的日志配置
# errorlog = None   # 使用自定义的日志配置