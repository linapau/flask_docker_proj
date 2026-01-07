# business logic
# not dependent on Flask and https requests, can be tested independently

from typing import Dict
from app.core.security import hash_password, verify_password

_USERS: Dict[str, str] = {}


class AuthService:
    @staticmethod
    def register(email: str, password: str) -> None:
        if email in _USERS:
            raise ValueError("User already exists")

        password_hash = hash_password(password)
        _USERS[email] = password_hash

    @staticmethod
    def login(email: str, password: str) -> None:
        if email not in _USERS:
            raise ValueError("Invalid credentials")

        password_hash = _USERS[email]

        if not verify_password(password, password_hash):
            raise ValueError("Invalid credentials")
