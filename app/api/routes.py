from flask import Blueprint

api_bp = Blueprint("api", __name__)

@api_bp.route("/")
def hello():
    return "Hello, World!"

@api_bp.route("/message")
def message():
    return {"message": "Welcome to Flask!"}
