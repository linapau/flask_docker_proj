import jwt
from datetime import datetime, timedelta, timezone
from flask import current_app


def create_access_token(subject: str) -> str:
    now = datetime.now(timezone.utc)
    payload = {
        "sub": subject, # user identifier (e.g., user id or email)
        "iat": now, # issued at - when token was issued
        "exp": now + timedelta( # expiration time 15min 
            minutes=current_app.config["ACCESS_TOKEN_EXPIRES_MINUTES"]
        ),
    }

    token = jwt.encode( # encode the token with payload and secret key
        payload,
        current_app.config["SECRET_KEY"],
        algorithm="HS256",
    )

    return token


def decode_access_token(token: str) -> dict:
    return jwt.decode(
        token,
        current_app.config["SECRET_KEY"],
        algorithms=["HS256"],
    )
