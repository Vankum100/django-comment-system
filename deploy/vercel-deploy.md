# Vercel Deployment Guide (Simplest Option)

Vercel is the easiest option - just connect your GitHub repo and deploy!

## Prerequisites

1. A Vercel account (sign up at https://vercel.com)
2. Your code pushed to GitHub (already done)
3. No credit card required!

## Quick Deployment

### Option 1: One-Click Deploy

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https://github.com/Vankum100/django-comment-system)

### Option 2: Manual Setup

1. **Go to Vercel Dashboard**:
   - Visit https://vercel.com
   - Click "New Project"
   - Import your GitHub repository: `Vankum100/django-comment-system`

2. **Configure Project**:
   - **Framework Preset**: Other
   - **Root Directory**: `services/frontend`
   - **Build Command**: `pip install -r requirements.txt && python manage.py collectstatic --noinput`
   - **Output Directory**: Leave empty
   - **Install Command**: `pip install -r requirements.txt`

3. **Environment Variables**:
   ```
   DJANGO_SETTINGS_MODULE=frontend.settings
   DEBUG=False
   SECRET_KEY=your-secret-key-here
   ```

4. **Deploy**:
   - Click "Deploy"
   - Wait for deployment to complete
   - Your app will be available at `https://your-app.vercel.app`

## Alternative: Deploy All Services

Since Vercel is great for frontend, you can also deploy the backend services separately:

### Backend Services (Users & Comments)

For the backend services, I recommend using **Railway** (as described in the manual guide) or **Heroku**:

#### Heroku (No Credit Card Required)
1. Go to https://heroku.com
2. Create new apps for each service
3. Connect GitHub repository
4. Set buildpacks to Python
5. Configure environment variables

#### Railway (Recommended)
1. Follow the manual deployment guide
2. Deploy each service separately
3. Connect to PostgreSQL database

## Vercel + Railway Hybrid Approach

This is the most reliable approach:

1. **Frontend on Vercel**:
   - Deploy the frontend service to Vercel
   - Get the Vercel URL

2. **Backend on Railway**:
   - Deploy users and comments services to Railway
   - Get the Railway URLs

3. **Connect Services**:
   - Update frontend environment variables with Railway URLs
   - Redeploy frontend

## Environment Variables for Vercel

In your Vercel project settings, add:

```
DJANGO_SETTINGS_MODULE=frontend.settings
DEBUG=False
SECRET_KEY=your-secret-key-here
COMMENTS_BASE_URL=https://your-comments-service.railway.app
USERS_BASE_URL=https://your-users-service.railway.app
```

## Vercel CLI (Optional)

If you prefer CLI:

```bash
# Install Vercel CLI
npm install -g vercel

# Login
vercel login

# Deploy
cd services/frontend
vercel

# Set environment variables
vercel env add SECRET_KEY
vercel env add COMMENTS_BASE_URL
vercel env add USERS_BASE_URL
```

## Advantages of Vercel

- ✅ **No credit card required**
- ✅ **Generous free tier**
- ✅ **Automatic deployments** from GitHub
- ✅ **Global CDN**
- ✅ **Easy custom domains**
- ✅ **Built-in analytics**

## Limitations

- ⚠️ **Serverless functions** (not full Django)
- ⚠️ **Cold starts** (first request might be slow)
- ⚠️ **Limited database options** (better to use external DB)

## Recommended Architecture

```
Frontend (Vercel) → Backend APIs (Railway) → Database (Railway PostgreSQL)
```

This gives you:
- Fast frontend delivery via Vercel's CDN
- Reliable backend services via Railway
- Managed PostgreSQL database
- No credit card required for any service

## Next Steps

1. **Deploy frontend to Vercel** (5 minutes)
2. **Deploy backend to Railway** (10 minutes)
3. **Connect the services** (5 minutes)
4. **Test everything** (5 minutes)

Total time: ~25 minutes for a fully deployed application!
