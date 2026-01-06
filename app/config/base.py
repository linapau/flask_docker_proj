#common part of configurations for the production, development, and testing environments

import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

class BaseConfig:
    SECRET_KEY = os.getenv("SECRET_KEY", "dev-secret-key")
    DEBUG = False
    TESTING = False

    JSON_SORT_KEYS = False

    ACCESS_TOKEN_EXPIRES_MINUTES = 15
    REFRESH_TOKEN_EXPIRES_DAYS = 7

    
    # DB_HOST = os.getenv("DB_HOST", "localhost")
    # DB_NAME = os.getenv("DB_NAME", "app_db")
    # DB_USER = os.getenv("DB_USER", "app_user")
    # DB_PASSWORD = os.getenv("DB_PASSWORD", "password")
