# Railway Deployment Guide

## Your Docker Images (Already Published)
- Frontend: `kumovish/comment-frontend:latest`
- Users: `kumovish/comment-users:latest`
- Comments: `kumovish/comment-comments:latest`

## Environment Variables Needed
- TELEGRAM_BOT_TOKEN=7980916672:AAEMdiiYgw8C-oddPoyMV0VvkZfH5Xwh2l4
- TELEGRAM_CHAT_ID=5654581485

## Deployment Steps

### 1. Go to Railway
- Visit: https://railway.app
- Sign up with GitHub
- Click "New Project"

### 2. Deploy Comments Service First
- Click "Deploy from Docker Hub"
- Image: `kumovish/comment-comments:latest`
- Service Name: `comments`
- Port: 8002
- Environment Variables: None needed

### 3. Deploy Users Service
- Click "Deploy from Docker Hub" 
- Image: `kumovish/comment-users:latest`
- Service Name: `users`
- Port: 8001
- Environment Variables: None needed

### 4. Deploy Frontend Service
- Click "Deploy from Docker Hub"
- Image: `kumovish/comment-frontend:latest`
- Service Name: `frontend`
- Port: 8000
- Environment Variables:
  - COMMENTS_BASE_URL=https://comments-production.up.railway.app
  - TELEGRAM_BOT_TOKEN=7980916672:AAEMdiiYgw8C-oddPoyMV0VvkZfH5Xwh2l4
  - TELEGRAM_CHAT_ID=5654581485

### 5. Get Service URLs
After deployment, Railway will give you URLs like:
- Frontend: https://frontend-production.up.railway.app
- Users: https://users-production.up.railway.app  
- Comments: https://comments-production.up.railway.app

### 6. Update Frontend Environment
Once you have the comments URL, update the frontend's COMMENTS_BASE_URL to the actual Railway URL.

## Alternative: Single Project with Multiple Services
1. Create one Railway project
2. Add 3 services to the same project
3. Railway will handle internal networking automatically
4. Use service names for internal communication: `http://comments:8002`
