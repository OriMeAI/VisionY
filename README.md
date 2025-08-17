# VisionY Deployment Guide

## 1. Modify Environment Configuration Files
### MongoDB and Redis need to be installed locally and services started
        
### Backend Configuration
- Copy `/app/.env.example` to `/app/.env`
- Fill in your own configuration parameters

### Frontend Configuration
- Copy `/web/.env.example` to `/web/.env`
- Fill in your own configuration parameters

## 2. Development Mode

### Start Backend Service
```bash
cd /app
python main.py
```
- Server runs on `localhost:3000`

### Start Frontend Service
```bash
cd /web
npm run start
```
- Frontend runs on `localhost:8080`

## 3. Docker Deployment

### Frontend Build
1. **Modify Configuration**
   - Modify `API_URL` in `/web/.env` to your backend API address

2. **Execute Build**
   ```bash
   cd /web
   npm run build:prod
   ```
   - Built files are in `/web/dist` directory     
   - `/web/dist` is the frontend static resource folder that needs to be deployed to the `html` folder under the nginx directory

### Nginx Configuration
1. **Create nginx folder**
   - Refer to files in `nginx_example` folder
   - Create `nginx` folder

2. **Configuration Files**
   - Create `nginx.conf` file in `nginx` folder
   - Create `cert` folder in `nginx` folder to store certificate files

### Server Deployment
**Required files to upload:**
- `/app/.env` file
- `/nginx` folder (including configuration and certificates)

### Test Mode Login
- Fixed email address: `test@example.com`
- Password can be any non-empty string

## License

This repository is licensed under the [VisionY Open Source License](LICENSE), based on Apache 2.0 with additional conditions.