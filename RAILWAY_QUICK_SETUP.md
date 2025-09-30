# 🚀 Railway Quick Setup - 3 Services

## ⚠️ **CRITICAL: Root Directory Must Be Set Correctly**

Each service needs the correct Root Directory to find `requirements.txt` and `Dockerfile`.

## 📋 **Quick Steps**

### **1. Fix Frontend (Current Service)**
- Go to frontend service → Settings → Build & Deploy
- **Root Directory**: `services/frontend`
- **Dockerfile Path**: `Dockerfile`
- Save → Redeploy

### **2. Add Users Service**
- New + → GitHub Repo
- **Root Directory**: `services/users`
- **Start Command**: `gunicorn --bind 0.0.0.0:$PORT users_service.wsgi:application`
- Deploy

### **3. Add Comments Service**
- New + → GitHub Repo
- **Root Directory**: `services/comments`
- **Start Command**: `gunicorn --bind 0.0.0.0:$PORT comments_service.wsgi:application`
- Deploy

### **4. Add Database**
- New + → Database → PostgreSQL
- Link to users and comments services

### **5. Set Environment Variables**

**Frontend**:
```
DJANGO_SETTINGS_MODULE=frontend.settings
DEBUG=False
SECRET_KEY=your-secret-key
COMMENTS_BASE_URL=https://your-comments-url.railway.app
USERS_BASE_URL=https://your-users-url.railway.app
```

**Users**:
```
DJANGO_SETTINGS_MODULE=users_service.settings
DEBUG=False
SECRET_KEY=your-secret-key
DATABASE_URL=${{PostgreSQL.DATABASE_URL}}
```

**Comments**:
```
DJANGO_SETTINGS_MODULE=comments_service.settings
DEBUG=False
SECRET_KEY=your-secret-key
DATABASE_URL=${{PostgreSQL.DATABASE_URL}}
```

## 🎯 **Result**
All 3 services connected and working on Railway!

## 🔗 **Your Railway Project**
https://railway.app/project/10ce995b-a424-4983-9f35-bcbc8390dd4d
