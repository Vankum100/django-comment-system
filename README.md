# Django Microservices Comment System

A Django-based microservices application with separate frontend, users, and comments services.

## Architecture

- **Frontend Service**: Django app with user authentication and UI
- **Users Service**: User management API
- **Comments Service**: Comments API with SQLite database
- **Telegram Integration**: Feedback form sends messages to Telegram

## Features

- User registration/login/logout
- Public comments display on main page
- Personal comments management
- Feedback form with Telegram notifications
- Docker containerized services

## Quick Start

### Local Development
```bash
cd deploy
docker compose up
```

### Production
```bash
cd deploy
docker compose -f docker-compose.prod.yml up
```

## Services

- Frontend: http://localhost:8000
- Users API: http://localhost:8001
- Comments API: http://localhost:8002

## Environment Variables

- `TELEGRAM_BOT_TOKEN`: Your Telegram bot token
- `TELEGRAM_CHAT_ID`: Your Telegram chat ID
- `COMMENTS_BASE_URL`: Comments service URL (for frontend)

## Docker Images

- `kumovish/comment-frontend:latest`
- `kumovish/comment-users:latest`
- `kumovish/comment-comments:latest`
