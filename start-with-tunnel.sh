#!/bin/bash

# Start Django Comment System with Local Tunnel
echo "🚀 Starting Django Comment System with Local Tunnel"
echo "=================================================="

# Check if Docker is running
if ! docker info > /dev/null 2>&1; then
    echo "❌ Docker is not running. Please start Docker first."
    exit 1
fi

# Check if ngrok is installed
if ! command -v ngrok &> /dev/null; then
    echo "❌ ngrok is not installed. Installing..."
    if command -v brew &> /dev/null; then
        brew install ngrok
    else
        echo "Please install ngrok from https://ngrok.com/download"
        exit 1
    fi
fi

echo "📦 Starting Docker Compose services..."
docker-compose -f deploy/docker-compose.yml up --build -d

echo "⏳ Waiting for services to start..."
sleep 10

echo "🌐 Starting ngrok tunnel..."
echo "Your app will be available at the ngrok URL shown below:"
echo ""

# Start ngrok in the background
ngrok http 8000 --log=stdout
