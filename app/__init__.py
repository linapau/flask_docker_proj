import os
from flask import Flask
from app.api.routes import api_bp
from app.api.auth.routes import auth_bp
from app.core.extensions import db, migrate

# migrations have to be seen by flask-migrate, so we need to import them here
from app.models.user import User


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

    db.init_app(app)
    migrate.init_app(app, db)

    # wires the blueprints to the app, so that the routes are registered and can be accessed via the app
    app.register_blueprint(api_bp)
    app.register_blueprint(auth_bp)

    # Create database tables if they don't exist. this triggers SQLAlchemy to build an Engine from SQLALCHEMY_DATABASE_URI and attempt a DB connection.
    with app.app_context():
        db.create_all()

    return app
