from flask import Blueprint, jsonify, request
from app.api.auth.services import AuthService

api_bp = Blueprint("api", __name__)


@api_bp.route("/")
def hello():
    return "Hello, World!"


@api_bp.route("/message")
def message():
    return {"message": "some message!"}


@api_bp.route("/register", methods=["GET", "POST"])
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
        return jsonify({"message": "User registered successfully!"}), 201
    except ValueError as e:
        return jsonify({"error": str(e)}), 400


@api_bp.route("/login", methods=["GET", "POST"])
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
        return jsonify({"message": "User logged in successfully!", "access_token": token}), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 401
