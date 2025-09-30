# Fly.io Deployment Guide (No Credit Card Required)

Fly.io offers 3 free shared-cpu VMs with 256MB RAM each - perfect for your microservices!

## Prerequisites

1. A Fly.io account (sign up at https://fly.io)
2. Your code pushed to GitHub (already done)
3. No credit card required for free tier!

## Quick Start

### 1. Install Fly CLI
```bash
curl -L https://fly.io/install.sh | sh
```

### 2. Login to Fly
```bash
fly auth login
```

### 3. Deploy Each Service

#### Frontend Service
```bash
cd services/frontend
fly launch --dockerfile Dockerfile
# Follow prompts, name it: comment-frontend
```

#### Users Service
```bash
cd services/users
fly launch --dockerfile Dockerfile
# Follow prompts, name it: comment-users
```

#### Comments Service
```bash
cd services/comments
fly launch --dockerfile Dockerfile
# Follow prompts, name it: comment-comments
```

### 4. Create PostgreSQL Database
```bash
fly postgres create --name comment-db
```

### 5. Connect Database to Services
```bash
# Connect to users service
fly postgres connect -a comment-db
# Get the connection string and set it as DATABASE_URL

# Connect to comments service
fly postgres connect -a comment-db
# Get the connection string and set it as DATABASE_URL
```

## Detailed Configuration

### Frontend Service (fly.toml)
```toml
app = "comment-frontend"
primary_region = "sjc"

[build]

[http_service]
  internal_port = 8000
  force_https = true
  auto_stop_machines = true
  auto_start_machines = true
  min_machines_running = 0

[[vm]]
  memory = "256mb"
  cpu_kind = "shared"
  cpus = 1

[env]
  DJANGO_SETTINGS_MODULE = "frontend.settings"
  DEBUG = "False"
```

### Environment Variables

Set these for each service:

#### Frontend:
```bash
fly secrets set -a comment-frontend SECRET_KEY="your-secret-key"
fly secrets set -a comment-frontend COMMENTS_BASE_URL="https://comment-comments.fly.dev"
fly secrets set -a comment-frontend USERS_BASE_URL="https://comment-users.fly.dev"
```

#### Users:
```bash
fly secrets set -a comment-users SECRET_KEY="your-secret-key"
fly secrets set -a comment-users DATABASE_URL="postgresql://..."
```

#### Comments:
```bash
fly secrets set -a comment-comments SECRET_KEY="your-secret-key"
fly secrets set -a comment-comments DATABASE_URL="postgresql://..."
```

## Deployment Commands

### Deploy All Services
```bash
# Frontend
cd services/frontend && fly deploy

# Users
cd services/users && fly deploy

# Comments
cd services/comments && fly deploy
```

### Check Status
```bash
fly status -a comment-frontend
fly logs -a comment-frontend
```

### Scale Services
```bash
fly scale count 1 -a comment-frontend
```

## Free Tier Limits

- **3 shared-cpu VMs** (256MB RAM each)
- **160GB outbound data transfer** per month
- **3GB persistent volume** per VM
- **Global edge locations**

## URLs After Deployment

- Frontend: `https://comment-frontend.fly.dev`
- Users: `https://comment-users.fly.dev`
- Comments: `https://comment-comments.fly.dev`

## Troubleshooting

### Common Issues:
1. **Out of memory**: Reduce memory usage or upgrade plan
2. **Build failures**: Check Dockerfile and requirements.txt
3. **Database connection**: Verify DATABASE_URL is set correctly

### Useful Commands:
```bash
# View logs
fly logs -a comment-frontend

# SSH into machine
fly ssh console -a comment-frontend

# Check machine status
fly status -a comment-frontend

# Restart service
fly restart -a comment-frontend
```

## Cost Management

- **Free tier**: 3 VMs, 256MB each
- **Paid plans**: Start at $1.94/month per VM
- **Database**: PostgreSQL starts at $1.94/month

## Next Steps

1. Deploy all three services
2. Set up the database
3. Configure environment variables
4. Test the application
5. Set up custom domains (optional)

Fly.io is excellent for global deployment with edge locations worldwide!
