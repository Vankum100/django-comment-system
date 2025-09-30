#!/bin/bash

# Start Django Comment System Locally
echo "🚀 Starting Django Comment System Locally"
echo "========================================="

# Check if Docker is running
if ! docker info > /dev/null 2>&1; then
    echo "❌ Docker is not running. Please start Docker first."
    exit 1
fi

echo "📦 Starting Docker Compose services..."
docker-compose -f deploy/docker-compose.yml up --build

echo ""
echo "✅ Services are running locally:"
echo "   Frontend: http://localhost:8000"
echo "   Users API: http://localhost:8001"
echo "   Comments API: http://localhost:8002"
echo ""
echo "💡 To expose publicly, use one of these options:"
echo "   1. ngrok: ngrok http 8000"
echo "   2. cloudflared: cloudflared tunnel --url http://localhost:8000"
echo "   3. localtunnel: lt --port 8000"
