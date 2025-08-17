# VisionY Project Introduction

As an experienced system architect, I'll provide you with a detailed introduction to the VisionY project. From the code structure and functional modules, this is quite an ambitious AI-driven storyboard generation platform.

## Project Overview

VisionY is a professional AI-based storyboard generation platform with the core philosophy of "AI Makes Creativity Visible". The platform can convert scripts into professional storyboards with one click, unleashing creators' creative potential.

## Core Features

### 1. Intelligent Script Analysis & Storyboard Generation
- **One-Click Conversion**: Supports multiple text format inputs or direct pasting, easily importing your creative blueprint
- **AI Engine Analysis**: Powerful AI engine quickly analyzes, breaks down, and generates initial storyboards with detailed parameters
- **Professional Annotation**: Automatically annotates each storyboard with shot type, camera angle, movement, and duration suggestions, meeting professional standards

### 2. Visual Editing Mode
- **WYSIWYG Interface**: Brand-new visual mode offers an unprecedented storyboard browsing and editing experience
- **Precise Adjustment**: Easily tweak AI-generated image descriptions and shot parameters
- **Multi-Format Export**: Supports multiple common format exports, seamlessly integrating into your workflow
        

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