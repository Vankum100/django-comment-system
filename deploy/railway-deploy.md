# Railway Deployment Guide (No Credit Card Required)

Railway offers a generous free tier with $5 monthly credit and no credit card required for signup.

## Prerequisites

1. A Railway account (sign up at https://railway.app)
2. Your code pushed to GitHub (already done)
3. No credit card required!

## Deployment Steps

### Method 1: Railway CLI (Recommended)

1. **Install Railway CLI**:
   ```bash
   npm install -g @railway/cli
   ```

2. **Login to Railway**:
   ```bash
   railway login
   ```

3. **Deploy from your project directory**:
   ```bash
   cd /Users/ken/Desktop/comment
   railway init
   railway up
   ```

### Method 2: GitHub Integration

1. **Connect GitHub**:
   - Go to https://railway.app
   - Click "New Project"
   - Select "Deploy from GitHub repo"
   - Choose your repository: `Vankum100/django-comment-system`

2. **Configure Services**:
   - Railway will auto-detect your Dockerfiles
   - Create separate services for each microservice

### Method 3: Railway Blueprint (Advanced)

Create a `railway.toml` file in your project root:

```toml
[build]
builder = "dockerfile"
dockerfilePath = "services/frontend/Dockerfile"

[deploy]
startCommand = "gunicorn --bind 0.0.0.0:$PORT frontend.wsgi:application"
healthcheckPath = "/"
```

## Service Configuration

### 1. Frontend Service
- **Dockerfile**: `services/frontend/Dockerfile`
- **Port**: Railway will set `$PORT` environment variable
- **Environment Variables**:
  - `DJANGO_SETTINGS_MODULE=frontend.settings`
  - `COMMENTS_BASE_URL=https://your-comments-service.railway.app`
  - `USERS_BASE_URL=https://your-users-service.railway.app`
  - `SECRET_KEY` (auto-generated)
  - `DEBUG=False`

### 2. Users Service
- **Dockerfile**: `services/users/Dockerfile`
- **Environment Variables**:
  - `DJANGO_SETTINGS_MODULE=users_service.settings`
  - `DATABASE_URL` (from PostgreSQL service)
  - `SECRET_KEY` (auto-generated)
  - `DEBUG=False`

### 3. Comments Service
- **Dockerfile**: `services/comments/Dockerfile`
- **Environment Variables**:
  - `DJANGO_SETTINGS_MODULE=comments_service.settings`
  - `DATABASE_URL` (from PostgreSQL service)
  - `SECRET_KEY` (auto-generated)
  - `DEBUG=False`

### 4. PostgreSQL Database
- **Service Type**: PostgreSQL
- **Plan**: Free tier
- **Connection**: Automatic via `DATABASE_URL`

## Step-by-Step Deployment

### Step 1: Create Railway Account
1. Go to https://railway.app
2. Sign up with GitHub (no credit card required)
3. Verify your email

### Step 2: Create New Project
1. Click "New Project"
2. Select "Deploy from GitHub repo"
3. Choose `Vankum100/django-comment-system`

### Step 3: Add Services
1. **Add Frontend Service**:
   - Click "New Service" → "GitHub Repo"
   - Select your repo
   - Set root directory to `services/frontend`
   - Railway will auto-detect Dockerfile

2. **Add Users Service**:
   - Click "New Service" → "GitHub Repo"
   - Select your repo
   - Set root directory to `services/users`

3. **Add Comments Service**:
   - Click "New Service" → "GitHub Repo"
   - Select your repo
   - Set root directory to `services/comments`

4. **Add Database**:
   - Click "New Service" → "Database" → "PostgreSQL"
   - Railway will create a PostgreSQL instance

### Step 4: Configure Environment Variables

For each service, go to Settings → Variables:

#### Frontend Service:
```
DJANGO_SETTINGS_MODULE=frontend.settings
COMMENTS_BASE_URL=https://your-comments-service.railway.app
USERS_BASE_URL=https://your-users-service.railway.app
SECRET_KEY=your-secret-key
DEBUG=False
```

#### Users Service:
```
DJANGO_SETTINGS_MODULE=users_service.settings
DATABASE_URL=${{PostgreSQL.DATABASE_URL}}
SECRET_KEY=your-secret-key
DEBUG=False
```

#### Comments Service:
```
DJANGO_SETTINGS_MODULE=comments_service.settings
DATABASE_URL=${{PostgreSQL.DATABASE_URL}}
SECRET_KEY=your-secret-key
DEBUG=False
```

### Step 5: Deploy
1. Railway will automatically build and deploy each service
2. Check the logs for any errors
3. Your services will be available at Railway-generated URLs

## Alternative: Fly.io Deployment

If you prefer Fly.io (also no credit card required):

### 1. Install Fly CLI
```bash
curl -L https://fly.io/install.sh | sh
```

### 2. Login to Fly
```bash
fly auth login
```

### 3. Create Fly Apps
```bash
# For each service
fly launch --dockerfile services/frontend/Dockerfile
fly launch --dockerfile services/users/Dockerfile
fly launch --dockerfile services/comments/Dockerfile
```

### 4. Create PostgreSQL Database
```bash
fly postgres create --name comment-db
```

## Alternative: Vercel (Frontend Only)

For a simpler approach, deploy just the frontend to Vercel:

### 1. Install Vercel CLI
```bash
npm install -g vercel
```

### 2. Deploy
```bash
cd services/frontend
vercel
```

## Cost Comparison

| Platform | Free Tier | Credit Card Required | Best For |
|----------|-----------|---------------------|----------|
| **Railway** | $5/month credit | ❌ No | Full-stack apps |
| **Fly.io** | 3 VMs, 256MB each | ❌ No | Global deployment |
| **Heroku** | $5/month minimum | ❌ No (hobby plans) | Traditional apps |
| **Vercel** | Generous limits | ❌ No | Frontend + serverless |
| **Netlify** | 100GB bandwidth | ❌ No | Static sites |

## Recommended Approach

1. **Start with Railway** - Most similar to Render, excellent Docker support
2. **Use Fly.io as backup** - Great for global deployment
3. **Consider Vercel** - If you want to simplify to frontend-only

## Next Steps

1. Choose your preferred platform
2. Follow the deployment guide
3. Set up environment variables
4. Test your application
5. Configure custom domains (optional)

All these platforms offer generous free tiers without requiring a credit card!