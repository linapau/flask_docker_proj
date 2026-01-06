import os
from flask import Flask
from app.api.routes import api_bp

def create_app():
    app = Flask(__name__)

    # Load configuration based on the environment
    env = os.getenv("FLASK_ENV", "development")

    if env == "production":
        app.config.from_object("app.config.prod.ProdConfig")
    elif env == "testing":
        app.config.from_object("app.config.test.TestConfig")
    else:
        app.config.from_object("app.config.dev.DevConfig")

    app.register_blueprint(api_bp)

    return app
