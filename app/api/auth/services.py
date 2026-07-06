# business logic
# not dependent on Flask and https requests, can be tested independently

from app.core.extensions import db
from app.core.security import hash_password, verify_password
from app.core.jwt import create_access_token
from app.models.user import User


class AuthService:
    @staticmethod
    def register(email: str, password: str) -> None:
        normalized_email = (email or "").strip().lower()

        if not normalized_email or not password:
            raise ValueError("Email and password are required")

        if User.query.filter_by(email=normalized_email).first():
            raise ValueError("User already exists")

        user = User(email=normalized_email, password_hash=hash_password(password))
        db.session.add(user)

        try:
            db.session.commit()
        except Exception:
            db.session.rollback()
            raise

    @staticmethod
    def login(email: str, password: str) -> str:
        normalized_email = (email or "").strip().lower()

        if not normalized_email or not password:
            raise ValueError("Email and password are required")

        user = User.query.filter_by(email=normalized_email).first()
        if not user:
            raise ValueError("Invalid credentials")

        if not verify_password(password, user.password_hash):
            raise ValueError("Invalid credentials")

        return create_access_token(subject=str(user.id))

