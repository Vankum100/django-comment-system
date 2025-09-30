# Railway Complete Setup Guide - All 3 Services

This guide will help you deploy all three services (frontend, users, comments) to Railway with proper connections.

## 🚨 **CRITICAL: Root Directory Configuration**

The most important step is setting the correct **Root Directory** for each service. This fixes the `requirements.txt not found` error.

## 📋 **Step-by-Step Deployment**

### **Step 1: Fix Frontend Service (Current)**

1. **Go to Railway Dashboard**: https://railway.app/project/10ce995b-a424-4983-9f35-bcbc8390dd4d
2. **Click on "frontend" service**
3. **Go to Settings → Build & Deploy**
4. **Set Root Directory to**: `services/frontend`
5. **Verify Dockerfile Path**: `Dockerfile`
6. **Click Save**
7. **Go to Deployments → Redeploy**

### **Step 2: Add Users Service**

1. **Click "New +" → "GitHub Repo"**
2. **Select repository**: `Vankum100/django-comment-system`
3. **Configuration**:
   - **Root Directory**: `services/users` ⚠️ **CRITICAL**
   - **Build Command**: Leave empty
   - **Start Command**: `gunicorn --bind 0.0.0.0:$PORT users_service.wsgi:application`
   - **Dockerfile Path**: `Dockerfile`
4. **Click Deploy**

### **Step 3: Add Comments Service**

1. **Click "New +" → "GitHub Repo"**
2. **Select repository**: `Vankum100/django-comment-system`
3. **Configuration**:
   - **Root Directory**: `services/comments` ⚠️ **CRITICAL**
   - **Build Command**: Leave empty
   - **Start Command**: `gunicorn --bind 0.0.0.0:$PORT comments_service.wsgi:application`
   - **Dockerfile Path**: `Dockerfile`
4. **Click Deploy**

### **Step 4: Add PostgreSQL Database**

1. **Click "New +" → "Database" → "PostgreSQL"**
2. **Railway creates PostgreSQL instance**
3. **Link database to users service**:
   - Go to users service → Settings → Variables
   - Add: `DATABASE_URL=${{PostgreSQL.DATABASE_URL}}`
4. **Link database to comments service**:
   - Go to comments service → Settings → Variables
   - Add: `DATABASE_URL=${{PostgreSQL.DATABASE_URL}}`

### **Step 5: Configure Environment Variables**

#### **Frontend Service Variables**:
```
DJANGO_SETTINGS_MODULE=frontend.settings
DEBUG=False
SECRET_KEY=your-secret-key-here
COMMENTS_BASE_URL=https://your-comments-url.railway.app
USERS_BASE_URL=https://your-users-url.railway.app
```

#### **Users Service Variables**:
```
DJANGO_SETTINGS_MODULE=users_service.settings
DEBUG=False
SECRET_KEY=your-secret-key-here
DATABASE_URL=${{PostgreSQL.DATABASE_URL}}
```

#### **Comments Service Variables**:
```
DJANGO_SETTINGS_MODULE=comments_service.settings
DEBUG=False
SECRET_KEY=your-secret-key-here
DATABASE_URL=${{PostgreSQL.DATABASE_URL}}
```

### **Step 6: Get Service URLs and Update**

1. **After all services deploy, note their URLs**:
   - Frontend: `https://frontend-production-xxxx.up.railway.app`
   - Users: `https://users-production-xxxx.up.railway.app`
   - Comments: `https://comments-production-xxxx.up.railway.app`

2. **Update frontend service variables**:
   - Replace `your-comments-url.railway.app` with actual comments URL
   - Replace `your-users-url.railway.app` with actual users URL

3. **Redeploy frontend service** to apply URL changes

## 🔧 **Troubleshooting**

### **"requirements.txt not found" Error**:
- **Cause**: Wrong Root Directory
- **Fix**: Set Root Directory to `services/frontend`, `services/users`, or `services/comments`

### **Service Communication Issues**:
- **Check**: URLs are correct and accessible
- **Verify**: Services are using HTTPS URLs
- **Ensure**: No trailing slashes in URLs

### **Database Connection Issues**:
- **Verify**: `DATABASE_URL` is set correctly
- **Check**: Database is linked to users and comments services
- **Format**: `${{PostgreSQL.DATABASE_URL}}`

## 📊 **Expected Final Architecture**

```
Frontend (Railway) → Users API (Railway) → PostgreSQL (Railway)
                  → Comments API (Railway) → PostgreSQL (Railway)
```

## 🎯 **Success Indicators**

- ✅ All three services show "Ready" status
- ✅ Frontend loads without errors
- ✅ Comments can be created and displayed
- ✅ User authentication works
- ✅ Database connections are active

## 💰 **Cost**

- **Free Tier**: $5 monthly credit
- **Usage**: Each service uses minimal credits
- **Database**: Included in free tier
- **No credit card required**

This setup gives you a fully functional microservices architecture on Railway!
