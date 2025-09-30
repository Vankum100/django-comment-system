# Render Deployment Guide

This guide will help you deploy your Django comment system to Render using Docker.

## Prerequisites

1. A Render account (sign up at https://render.com)
2. Your code pushed to GitHub (already done)
3. Docker Hub account (optional, for custom images)

## Deployment Steps

### 1. Create a New Blueprint on Render

1. Go to your Render dashboard
2. Click "New +" and select "Blueprint"
3. Connect your GitHub repository: `Vankum100/django-comment-system`
4. Select the `render.yaml` file from the root directory
5. Click "Apply"

### 2. Environment Variables

After the services are created, you'll need to set these environment variables:

#### Frontend Service (comment-frontend)
- `TELEGRAM_BOT_TOKEN`: Your Telegram bot token (if using Telegram integration)
- `TELEGRAM_CHAT_ID`: Your Telegram chat ID (if using Telegram integration)

#### Users Service (comment-users)
- No additional environment variables needed

#### Comments Service (comment-comments)
- No additional environment variables needed

### 3. Database Setup

The PostgreSQL database (`comment-db`) will be automatically created and configured. The `DATABASE_URL` environment variable will be automatically set for the users and comments services.

### 4. Service URLs

After deployment, your services will be available at:
- Frontend: `https://comment-frontend.onrender.com`
- Users API: `https://comment-users.onrender.com`
- Comments API: `https://comment-comments.onrender.com`

### 5. Manual Deployment (Alternative)

If you prefer to deploy services individually:

#### Deploy Frontend Service
1. Go to Render dashboard
2. Click "New +" → "Web Service"
3. Connect your GitHub repository
4. Configure:
   - **Name**: comment-frontend
   - **Environment**: Docker
   - **Dockerfile Path**: `./services/frontend/Dockerfile`
   - **Docker Context**: `./services/frontend`
   - **Plan**: Starter (Free)
   - **Region**: Oregon

#### Deploy Users Service
1. Click "New +" → "Web Service"
2. Connect your GitHub repository
3. Configure:
   - **Name**: comment-users
   - **Environment**: Docker
   - **Dockerfile Path**: `./services/users/Dockerfile`
   - **Docker Context**: `./services/users`
   - **Plan**: Starter (Free)
   - **Region**: Oregon

#### Deploy Comments Service
1. Click "New +" → "Web Service"
2. Connect your GitHub repository
3. Configure:
   - **Name**: comment-comments
   - **Environment**: Docker
   - **Dockerfile Path**: `./services/comments/Dockerfile`
   - **Docker Context**: `./services/comments`
   - **Plan**: Starter (Free)
   - **Region**: Oregon

#### Create Database
1. Click "New +" → "PostgreSQL"
2. Configure:
   - **Name**: comment-db
   - **Plan**: Starter (Free)
   - **Region**: Oregon
3. Connect the database to your users and comments services

### 6. Post-Deployment

1. **Run Migrations**: The services will automatically run migrations on startup
2. **Test the Application**: Visit your frontend URL to test the application
3. **Monitor Logs**: Check the Render dashboard for any deployment issues

### 7. Troubleshooting

#### Common Issues:
1. **Build Failures**: Check the build logs in Render dashboard
2. **Database Connection**: Ensure `DATABASE_URL` is properly set
3. **Static Files**: The Dockerfiles include `collectstatic` command
4. **CORS Issues**: Update `ALLOWED_HOSTS` in settings if needed

#### Logs:
- Check service logs in the Render dashboard
- Look for Django error messages
- Verify environment variables are set correctly

### 8. Custom Domain (Optional)

1. Go to your service settings
2. Click "Custom Domains"
3. Add your domain and configure DNS

## File Structure

```
/
├── render.yaml                 # Render Blueprint configuration
├── services/
│   ├── frontend/
│   │   ├── Dockerfile
│   │   ├── requirements.txt
│   │   └── frontend/settings.py
│   ├── users/
│   │   ├── Dockerfile
│   │   ├── requirements.txt
│   │   └── users_service/settings.py
│   └── comments/
│       ├── Dockerfile
│       ├── requirements.txt
│       └── comments_service/settings.py
└── deploy/
    └── render-deploy.md       # This file
```

## Environment Variables Reference

| Variable | Service | Description | Required |
|----------|---------|-------------|----------|
| `SECRET_KEY` | All | Django secret key | Auto-generated |
| `DEBUG` | All | Debug mode | No (default: False) |
| `ALLOWED_HOSTS` | All | Allowed hostnames | No (auto-set) |
| `DATABASE_URL` | Users, Comments | PostgreSQL connection | Auto-set |
| `TELEGRAM_BOT_TOKEN` | Frontend | Telegram bot token | No |
| `TELEGRAM_CHAT_ID` | Frontend | Telegram chat ID | No |

## Next Steps

1. Deploy using the Blueprint method (recommended)
2. Set up your Telegram bot credentials if using Telegram integration
3. Test all functionality
4. Set up monitoring and alerts
5. Consider upgrading to paid plans for production use
