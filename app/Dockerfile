# 使用官方 Python 镜像
FROM python:3.9.18

# 设置工作目录
WORKDIR /app

# 复制 requirements.txt
COPY requirements.txt .

# 安装 Python 依赖
RUN pip install -r requirements.txt --index-url https://pypi.org/simple