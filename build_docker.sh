#!/bin/bash

# Ubuntu deployment script for VisionY Server
# This script stops docker-compose.ai, pulls latest code, and restarts the service

set -e  # Exit on any error

echo "🚨 WARNING: This will stop all running services and rebuild containers!"
echo "📋 This script will:"
echo "   1. Stop all docker-compose services"
echo "   2. Pull latest code from git"
echo "   3. Rebuild and restart all services"
echo ""
echo "⚠️  Current running services:"
docker-compose ps 2>/dev/null || echo "   No services currently running"
echo ""
echo "📊 Active connections (if any):"
netstat -an 2>/dev/null | grep :80 | grep ESTABLISHED | wc -l | xargs echo "   HTTP connections:" || echo "   Connection info unavailable"
netstat -an 2>/dev/null | grep :443 | grep ESTABLISHED | wc -l | xargs echo "   HTTPS connections:" || echo "   Connection info unavailable"
echo ""
echo "🚨 WARNING: This will immediately disconnect all users!"

# 严格的确认逻辑 - 只接受完整的 yes 或 no
while true; do
    read -p "❓ Are you sure you want to continue? (type 'yes' or 'no'): " confirm
    case "$confirm" in
        "yes")
            echo "✅ Confirmed. Starting build process..."
            break
            ;;
        "no")
            echo "❌ Operation cancelled by user."
            exit 0
            ;;
        *)
            echo "⚠️  Please type exactly 'yes' or 'no' (without quotes)"
            ;;
    esac
done


echo "Starting build process..."

# Step 0: Environment validation
echo "Validating environment..."

# Check backend .env file
if [ ! -f "app/.env" ]; then
    echo "❌ Error: app/.env file not found!"
    echo "📝 Please copy app/.env.example to app/.env and configure it:"
    echo "   cp app/.env.example app/.env"
    echo "   # Then edit app/.env with your settings"
    exit 1
fi

# Check and create nginx html directory structure
echo "Validating nginx configuration..."
if [ ! -f "nginx/nginx.conf" ]; then
    echo "❌ Error: nginx/nginx.conf not found!"
    exit 1
fi

if [ ! -d "nginx/html" ]; then
    echo "📁 Creating missing html directory: nginx/html"
    exit 1
fi

echo "✅ Environment validation passed"

# Step 1: Stop docker-compose service
echo "Stopping docker-compose service..."
if [ -f "docker-compose.yml" ]; then
    docker-compose down
    echo "docker-compose service stopped successfully"
else
    echo "Warning: docker-compose.yml not found"
    exit 1
fi

# Step 2: Pull latest code from git
echo "Pulling latest code from git..."
git pull
echo "Git pull completed successfully"

# Step 3: Start docker-compose service
echo "Starting docker-compose service..."
if [ -f "docker-compose.yml" ]; then
    docker-compose up -d --build
    echo "docker-compose service started successfully"
else
    echo "Error: docker-compose.yml not found"
    exit 1
fi

docker-compose ps
echo "Build completed successfully!"
echo "You can check the service status with: docker-compose logs"
