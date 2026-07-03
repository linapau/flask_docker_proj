
# Flask Authentication App with Docker

## Overview
Simple Flask application with user login and registration functionality, containerized with Docker.

## Features
- User registration
- User login
- Session management
- Docker support

## Prerequisites
- Docker
- Docker Compose

## Setup

1. Clone the repository
2. Build and run with Docker:
- Production server:

```bash
docker-compose \
-f docker-compose.yml \
-f docker-compose.prod.yml \
up --build
```

Development server:
```bash
docker-compose \
-f docker-compose.yml \
-f docker-compose.dev.yml \
up --build
```

3. Access the app at `http://localhost:5000`

## Usage
- Register a new account at `/register`
- Login at `/login`
- Access protected routes after authentication

## Technologies
- Flask 3.1.0
- Werkzeug 3.1.0
- Gunicorn 26.0.0
- SQLAlchemy 2.0.41
- Flask-SQLAlchemy 3.1.1
- Flask-Migrate 4.1.0
- PyJWT 2.10.1
- Python 3.12
- MySQL 8.4.9
- Docker & Docker Compose


### How it works
REQUEST
  ↓
ROUTES (HTTP)
  ↓
SERVICES (logic)
  ↓
SECURITY / DB / EVENTS
  ↓
RESPONSE
