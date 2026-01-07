
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
```bash
docker-compose up --build
```

3. Access the app at `http://localhost:5000`

## Usage
- Register a new account at `/register`
- Login at `/login`
- Access protected routes after authentication

## Technologies
- Flask
- Docker
- Python 3.9+


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
