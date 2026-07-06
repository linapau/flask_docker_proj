# endpoints for user authentication such as registration and login.
# routes maps url to functions

from flask import Blueprint, jsonify, request
from app.api.auth.services import AuthService

auth_bp = Blueprint("auth", __name__, url_prefix="/auth")


@auth_bp.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return jsonify({
            "message": "Use POST to register a user.",
            "example": {"email": "user@example.com", "password": "secret123"},
        }), 200

    data = request.get_json(silent=True) or {}

    try:
        AuthService.register(
            email=data.get("email"),
            password=data.get("password"),
        )
        return jsonify({"message": "User registered"}), 201

    except ValueError as e:
        return jsonify({"error": str(e)}), 400


@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return jsonify({
            "message": "Use POST to log in.",
            "example": {"email": "user@example.com", "password": "secret123"},
        }), 200

    data = request.get_json(silent=True) or {}

    try:
        token = AuthService.login(
            email=data.get("email"),
            password=data.get("password"),
        )
        return jsonify({"message": "Login successful", "access_token": token}), 200

    except ValueError as e:
        return jsonify({"error": str(e)}), 401

