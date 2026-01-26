from flask import Blueprint

main_bp = Blueprint("pages", __name__)

@main_bp.route("/")
def home():
    return "Hello, Home!"

@main_bp.route("/about")
def about():
    return "Hello, About!"

@main_bp.route("/testing")
def about():
    return "Hello, Testing!"