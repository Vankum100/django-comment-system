#!/bin/bash

# Railway Deployment Script
# This script helps deploy your Django comment system to Railway

echo "🚀 Railway Deployment Script"
echo "=============================="

# Check if Railway CLI is installed
if ! command -v railway &> /dev/null; then
    echo "❌ Railway CLI not found. Installing..."
    npm install -g @railway/cli
fi

# Login to Railway
echo "🔐 Logging into Railway..."
railway login

# Create new project
echo "📦 Creating Railway project..."
railway init

# Deploy the project
echo "🚀 Deploying to Railway..."
railway up

echo "✅ Deployment complete!"
echo "🌐 Your app will be available at the Railway-generated URL"
echo "📊 Check the Railway dashboard for logs and monitoring"
