# endpoints for user authentication such as registration and login.
# routes maps url to functions

from flask import Blueprint, request, jsonify
from app.api.auth.services import AuthService

auth_bp = Blueprint("auth", __name__, url_prefix="/auth")


@auth_bp.route("/register", methods=["POST"])
def register():
    data = request.get_json()

    try:
        AuthService.register(
            email=data["email"],
            password=data["password"],
        )
        return jsonify({"message": "User registered"}), 201

    except ValueError as e:
        return jsonify({"error": str(e)}), 400


@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.get_json()

    try:
        token = AuthService.login(
            email=data["email"],
            password=data["password"],
        )
        return jsonify({"message": "Login successful", "access_token": token}), 200
    
    except ValueError as e:
        return jsonify({"error": str(e)}), 401

