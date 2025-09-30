# Local Tunnel Deployment Guide

Deploy your Django comment system locally and expose it publicly using tunnels - no credit card required!

## 🚀 **Quick Start**

### **Option 1: One-Command Setup**
```bash
# Start everything with ngrok tunnel
./start-with-tunnel.sh
```

### **Option 2: Manual Setup**
```bash
# Start locally first
./start-local.sh

# Then expose with tunnel (in another terminal)
ngrok http 8000
```

## 📋 **Tunnel Options**

### **1. ngrok (Recommended)**
- **Pros**: Most popular, reliable, good free tier
- **Cons**: Requires signup for custom domains

```bash
# Install
brew install ngrok

# Start your app
docker-compose -f deploy/docker-compose.yml up --build

# Expose (in another terminal)
ngrok http 8000
```

### **2. Cloudflare Tunnel (Free)**
- **Pros**: No signup required, very fast
- **Cons**: Less features than ngrok

```bash
# Install
brew install cloudflared

# Start your app
docker-compose -f deploy/docker-compose.yml up --build

# Expose (in another terminal)
cloudflared tunnel --url http://localhost:8000
```

### **3. LocalTunnel (Node.js)**
- **Pros**: No signup, simple
- **Cons**: Can be less reliable

```bash
# Install
npm install -g localtunnel

# Start your app
docker-compose -f deploy/docker-compose.yml up --build

# Expose (in another terminal)
lt --port 8000
```

### **4. serveo (SSH-based)**
- **Pros**: No installation, uses SSH
- **Cons**: Requires SSH

```bash
# Start your app
docker-compose -f deploy/docker-compose.yml up --build

# Expose (in another terminal)
ssh -R 80:localhost:8000 serveo.net
```

## 🔧 **Configuration**

### **Update Service URLs for Tunnel**

When using a tunnel, you'll need to update the service URLs. The tunnel will give you a public URL like `https://abc123.ngrok.io`.

Update your Docker Compose environment variables:

```yaml
environment:
  - COMMENTS_BASE_URL=https://abc123.ngrok.io:8002
  - USERS_BASE_URL=https://abc123.ngrok.io:8001
```

### **For Multiple Services**

If you want to expose all services:

```bash
# Terminal 1: Start Docker Compose
docker-compose -f deploy/docker-compose.yml up --build

# Terminal 2: Expose frontend
ngrok http 8000

# Terminal 3: Expose users API
ngrok http 8001

# Terminal 4: Expose comments API
ngrok http 8002
```

## 🌐 **Access Your App**

After starting the tunnel, you'll get URLs like:
- **Frontend**: `https://abc123.ngrok.io`
- **Users API**: `https://def456.ngrok.io` (if exposing separately)
- **Comments API**: `https://ghi789.ngrok.io` (if exposing separately)

## 📱 **Mobile Testing**

Tunnels are perfect for mobile testing:
1. Start your app with tunnel
2. Get the public URL
3. Test on your phone using the public URL
4. Share with others for testing

## 🔒 **Security Notes**

- **Tunnels are public** - anyone with the URL can access
- **Use for development/testing only**
- **Don't expose production data**
- **Consider authentication for sensitive apps**

## 💰 **Cost Comparison**

| Service | Free Tier | Custom Domain | Signup Required |
|---------|-----------|---------------|-----------------|
| **ngrok** | 1 tunnel, 40 connections/min | ✅ Paid | ✅ Yes |
| **Cloudflare** | Unlimited | ✅ Free | ❌ No |
| **LocalTunnel** | Unlimited | ❌ No | ❌ No |
| **serveo** | Unlimited | ❌ No | ❌ No |

## 🎯 **Recommended Workflow**

1. **Development**: Use `./start-local.sh` for local development
2. **Testing**: Use `./start-with-tunnel.sh` for public testing
3. **Sharing**: Use tunnel URLs to share with team/clients
4. **Production**: Deploy to Railway/Vercel for permanent hosting

## 🚨 **Troubleshooting**

### **Port Already in Use**
```bash
# Kill processes using port 8000
lsof -ti:8000 | xargs kill -9
```

### **Docker Issues**
```bash
# Clean up Docker
docker-compose down
docker system prune -f
```

### **Tunnel Connection Issues**
- Try a different tunnel service
- Check your firewall settings
- Restart the tunnel service

## 📊 **Performance**

- **Local development**: Fastest (localhost)
- **Tunnel**: Slightly slower (goes through tunnel server)
- **Cloud deployment**: Fastest for end users

This approach gives you the best of both worlds - local development speed with public accessibility!
