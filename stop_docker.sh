#!/bin/bash

# Ubuntu deployment script for VisionY Server   
# This script stops docker-compose.ai, pulls latest code, and restarts the service

set -e  # Exit on any error

echo "🛑 DANGER: This will stop ALL running services immediately!"
echo "📋 This script will:"
echo "   1. Stop all docker-compose services"
echo "   2. Disconnect all user connections"
echo "   3. Make the website unavailable"
echo ""
echo "⚠️  Current running services:"
docker-compose ps 2>/dev/null || echo "   No services currently running"
echo ""
echo "📊 Active connections (if any):"
netstat -an 2>/dev/null | grep :80 | grep ESTABLISHED | wc -l | xargs echo "   HTTP connections:" || echo "   Connection info unavailable"
netstat -an 2>/dev/null | grep :443 | grep ESTABLISHED | wc -l | xargs echo "   HTTPS connections:" || echo "   Connection info unavailable"
echo ""
echo "🚨 WARNING: This will immediately disconnect all users!"
echo ""

# 严格的确认逻辑 - 只接受完整的 yes 或 no
while true; do
    read -p "❓ Are you sure you want to STOP all services? (type 'yes' or 'no'): " confirm
    case "$confirm" in
        "yes")
            echo "✅ Confirmed. Stopping all services..."
            break
            ;;
        "no")
            echo "❌ Stop operation cancelled by user."
            exit 0
            ;;
        *)
            echo "⚠️  Please type exactly 'yes' or 'no' (without quotes)"
            ;;
    esac
done

echo "Starting deployment process..."

# Step 1: Stop docker-compose service
echo "Stopping docker-compose service..."
if [ -f "docker-compose.yml" ]; then
    docker-compose down
    echo "docker-compose service stopped successfully"
else
    echo "Warning: docker-compose.yml not found"
    exit 1
fi

docker-compose ps
echo "Deployment stopped successfully!"
