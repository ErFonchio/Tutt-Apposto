from flask import Blueprint, request, jsonify

auth_bp = Blueprint("auth", __name__)  # <--- crea un blueprint

@auth_bp.route("/register", methods=["POST"])
def register_user():
    data = request.get_json()
    return jsonify({"message": "Utente registrato!"})

@auth_bp.route("/login", methods=["POST"])
def login_user():
    data = request.get_json()
    return jsonify({"message": "Utente loggato!"})
