# routes/user_routes.py
from flask import Blueprint, jsonify
from config.firebase_config import db

user_bp = Blueprint("user", __name__)

@user_bp.route("/users", methods=["GET"])
def get_users():
    users_ref = db.collection("users")
    docs = users_ref.stream()
    users = [doc.to_dict() for doc in docs]
    return jsonify(users)
