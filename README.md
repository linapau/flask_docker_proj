# Flask Authentication App with Docker

## Overview
A simple Flask application with user registration and login, backed by MySQL and containerized with Docker.

## Features
- User registration via API
- User login via API
- JWT-based authentication
- MySQL persistence through SQLAlchemy
- Docker Compose support for development and production

## Prerequisites
- Docker
- Docker Compose
- Python 3.12 (for local development outside Docker)

## Setup

1. Clone the repository.
2. Start the app with Docker Compose:

Development:
```bash
docker-compose \
  -f docker-compose.yml \
  -f docker-compose.dev.yml \
  up --build
```

Production:
```bash
docker-compose \
  -f docker-compose.yml \
  -f docker-compose.prod.yml \
  up --build
```

3. Open the app at `http://localhost:5000`.

## Environment variables
The app uses the following environment variables:

- `FLASK_ENV` - environment name (`development`, `testing`, `production`)
- `DATABASE_URL` - full SQLAlchemy database URL (optional)
- `DB_HOST`, `DB_PORT`, `DB_NAME`, `DB_USER`, `DB_PASSWORD` - used if `DATABASE_URL` is not provided
- `SECRET_KEY` - secret used for JWT signing

## API usage

### Register user
```http
POST /auth/register
Content-Type: application/json

{
  "email": "user@example.com",
  "password": "secret123"
}
```

### Login user
```http
POST /auth/login
Content-Type: application/json

{
  "email": "user@example.com",
  "password": "secret123"
}
```

If you open the endpoints in a browser, the app now returns a helpful JSON response for `GET` requests as well.

## Technologies
- Flask 3.1.0
- Werkzeug 3.1.0
- Gunicorn 23.0.0
- SQLAlchemy 2.0.41
- Flask-SQLAlchemy 3.1.1
- Flask-Migrate 4.1.0
- PyJWT 2.10.1
- PyMySQL 1.1.1
- cryptography 45.0.0
- Python 3.12
- MySQL 8.4.9
- Docker & Docker Compose

## How it works
```text
Client
  ↓
Flask routes
  ↓
Auth service
  ↓
SQLAlchemy / MySQL
  ↓
JSON response or JWT
```

The application initializes the database tables on startup, then handles registration and login requests through the auth endpoints.
