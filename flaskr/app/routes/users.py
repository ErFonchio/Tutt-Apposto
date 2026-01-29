from flask import Blueprint, request, jsonify, current_app
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity

users_bp = Blueprint("users", __name__)
users = {}

@users_bp.route("/", methods=["GET"])
def home():
    return jsonify({"message": "you did it motherfucker"})

@users_bp.before_request
def log_request():
    print("REQUEST FROM:", request.remote_addr)

@users_bp.route("/register", methods=["POST"])
def register():

    username = request.json.get('username')
    password = request.json.get('password')
 
    # Input validation
    if not username or not password:
        return jsonify({"message": "Missing username or password"}), 400
 
    # Check if user already exists
    if username in users:
        return jsonify({"message": "User already exists"}), 400
 
    # Store user
    users[username] = password
    return jsonify({"message": "User registered successfully"}), 201

@users_bp.route('/login', methods=['POST'])
def login():
    
    username = request.json.get('username')
    password = request.json.get('password')
 
    # Input validation
    if not username or not password:
        return jsonify({"message": "Missing username or password"}), 400
 
    # Authentication
    if users.get(username) != password:
        return jsonify({"message": "Invalid credentials"}), 401
 
    # Create JWT
    access_token = create_access_token(identity=username)
    return jsonify({"message": "login done", "access_token": access_token}), 200

@users_bp.route("/protected_home", methods=['GET'])
@jwt_required()
def protected_home():
    
    current_user = get_jwt_identity()
    return jsonify({"message": "you're in!", "user": f"{current_user}"})

