from flask import Flask
from flask_jwt_extended import JWTManager

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.ProductionConfig')

    # Set JWT manager
    jwt = JWTManager(app)

    # registra i gruppi di rotte
    from app.routes.users import users_bp

    app.register_blueprint(users_bp, url_prefix='/users')

    return app