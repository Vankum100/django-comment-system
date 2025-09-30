# Railway Manual Deployment Guide (No Credit Card Required)

Since the CLI approach had some issues, here's a step-by-step guide to deploy through Railway's web interface.

## Step 1: Access Your Railway Project

1. Go to https://railway.app
2. Click on your project "dynago" (or create a new one)
3. You should see your project dashboard

## Step 2: Deploy Frontend Service

### 2.1 Create Frontend Service
1. Click "New Service" → "GitHub Repo"
2. Select your repository: `Vankum100/django-comment-system`
3. Railway will ask for configuration:
   - **Root Directory**: `services/frontend`
   - **Build Command**: Leave empty (uses Dockerfile)
   - **Start Command**: `gunicorn --bind 0.0.0.0:$PORT frontend.wsgi:application`
   - **Dockerfile Path**: `Dockerfile` (should auto-detect)

### 2.2 Configure Environment Variables
In the frontend service settings, add these variables:
```
DJANGO_SETTINGS_MODULE=frontend.settings
DEBUG=False
SECRET_KEY=your-secret-key-here
COMMENTS_BASE_URL=https://your-comments-service.railway.app
USERS_BASE_URL=https://your-users-service.railway.app
```

## Step 3: Deploy Users Service

### 3.1 Create Users Service
1. Click "New Service" → "GitHub Repo"
2. Select your repository: `Vankum100/django-comment-system`
3. Configuration:
   - **Root Directory**: `services/users`
   - **Build Command**: Leave empty
   - **Start Command**: `gunicorn --bind 0.0.0.0:$PORT users_service.wsgi:application`

### 3.2 Configure Environment Variables
```
DJANGO_SETTINGS_MODULE=users_service.settings
DEBUG=False
SECRET_KEY=your-secret-key-here
DATABASE_URL=${{PostgreSQL.DATABASE_URL}}
```

## Step 4: Deploy Comments Service

### 4.1 Create Comments Service
1. Click "New Service" → "GitHub Repo"
2. Select your repository: `Vankum100/django-comment-system`
3. Configuration:
   - **Root Directory**: `services/comments`
   - **Build Command**: Leave empty
   - **Start Command**: `gunicorn --bind 0.0.0.0:$PORT comments_service.wsgi:application`

### 4.2 Configure Environment Variables
```
DJANGO_SETTINGS_MODULE=comments_service.settings
DEBUG=False
SECRET_KEY=your-secret-key-here
DATABASE_URL=${{PostgreSQL.DATABASE_URL}}
```

## Step 5: Create PostgreSQL Database

### 5.1 Add Database
1. Click "New Service" → "Database" → "PostgreSQL"
2. Railway will create a PostgreSQL instance
3. Note the database name (e.g., "PostgreSQL")

### 5.2 Connect Database to Services
1. Go to Users service settings
2. Add variable: `DATABASE_URL=${{PostgreSQL.DATABASE_URL}}`
3. Go to Comments service settings
4. Add variable: `DATABASE_URL=${{PostgreSQL.DATABASE_URL}}`

## Step 6: Update Service URLs

After all services are deployed, update the URLs:

### 6.1 Get Service URLs
1. Each service will have a Railway-generated URL
2. Note down the URLs for each service

### 6.2 Update Frontend Service
Update the frontend service variables:
```
COMMENTS_BASE_URL=https://your-actual-comments-url.railway.app
USERS_BASE_URL=https://your-actual-users-url.railway.app
```

## Step 7: Deploy and Test

### 7.1 Deploy All Services
1. Railway will automatically deploy when you save changes
2. Check the deployment logs for any errors
3. Wait for all services to be "Ready"

### 7.2 Test Your Application
1. Visit your frontend URL
2. Test the comment functionality
3. Check that all services are communicating

## Troubleshooting

### Common Issues:

1. **Build Failures - "requirements.txt not found"**:
   - **Problem**: Railway can't find requirements.txt
   - **Solution**: Make sure "Root Directory" is set to `services/frontend`
   - **Check**: The Dockerfile should be in the same directory as requirements.txt
   - **Verify**: In Railway dashboard, go to Settings → Build & Deploy → Root Directory

2. **Build Failures - General**:
   - Check that the root directory is correct
   - Verify Dockerfile exists in the specified directory
   - Check build logs for specific errors

2. **Database Connection Issues**:
   - Ensure `DATABASE_URL` is set correctly
   - Use the format: `${{PostgreSQL.DATABASE_URL}}`
   - Check that the database service is running

3. **Service Communication Issues**:
   - Verify URLs are correct and accessible
   - Check that services are using HTTPS URLs
   - Ensure CORS settings allow cross-origin requests

4. **Environment Variable Issues**:
   - Double-check variable names and values
   - Ensure no extra spaces or quotes
   - Restart services after changing variables

### Useful Commands (if using CLI):
```bash
# Check service status
railway status

# View logs
railway logs

# Open service in browser
railway open

# Set variables
railway variables --set "KEY=value"
```

## Expected URLs

After successful deployment, you'll have:
- **Frontend**: `https://frontend-production-xxxx.up.railway.app`
- **Users**: `https://users-production-xxxx.up.railway.app`
- **Comments**: `https://comments-production-xxxx.up.railway.app`

## Next Steps

1. **Custom Domain** (optional):
   - Go to service settings
   - Click "Custom Domains"
   - Add your domain

2. **Monitoring**:
   - Check Railway dashboard for metrics
   - Set up alerts for downtime

3. **Scaling**:
   - Upgrade to paid plans for more resources
   - Configure auto-scaling

## Cost

- **Free Tier**: $5 monthly credit
- **Usage**: Each service uses minimal credits
- **Database**: Included in free tier
- **No credit card required** for free tier

This manual approach is often more reliable than CLI for initial deployments!
