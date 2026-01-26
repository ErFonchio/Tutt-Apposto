from flask import Flask
from flask_cors import CORS

from routes.auth_routes import auth_bp
from routes.user_routes import user_bp
from routes.main_routes import main_bp

def create_app():
    
    app = Flask(__name__)
    CORS(app)

    app.register_blueprint(main_bp)
    app.register_blueprint(user_bp)
    app.register_blueprint(auth_bp, url_prefix="/auth")

    return app