# VisionY  部署指南

## 1. 修改环境配置文件
### 本地需要安装mongodb和redis，并且启动服务

### 后端配置
- 将 `/app/.env.example` 复制为 `/app/.env`
- 填写你自己的配置参数

### 前端配置
- 将 `/web/.env.example` 复制为 `/web/.env`
- 填写你自己的配置参数

## 2. 开发模式

### 启动后端服务
```bash
cd /app
python main.py
```
- 服务器运行在 `localhost:3000`

### 启动前端服务
```bash
cd /web
npm run start
```
- 前端运行在 `localhost:8080`

## 3. Docker 部署

### 前端打包
1. **修改配置**
   - 修改 `/web/.env` 中的 `API_URL` 为你的后端API地址

2. **执行打包**
   ```bash
   cd /web
   npm run build:prod
   ```
   - 打包后的文件在 `/web/dist` 目录
   - `/web/dist` 是前端静态资源文件夹，需要部署到 nginx 目录下的 `html` 文件夹下

### Nginx 配置
1. **创建 nginx 文件夹**
   - 参考 `nginx_example` 文件夹下的文件
   - 创建 `nginx` 文件夹

2. **配置文件**
   - 在 `nginx` 文件夹下创建 `nginx.conf` 文件
   - 在 `nginx` 文件夹下创建 `cert` 文件夹，存放证书文件

### 服务器部署
**必须上传的文件：**
- `/app/.env` 文件
- `/nginx` 文件夹（包含配置和证书）

### 测试模式登录
- 固定邮箱地址：`test@example.com`
- 密码随便写，但是不能为空
        