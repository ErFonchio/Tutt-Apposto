import os
from datetime import timedelta

class DevelopmentConfig():
    FLASK_SECRET_KEY = os.getenv("FLASK_SECRET_KEY", "dev-key")
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", "jwt-key")
    
    # Nordigen secrets
    SECRET_ID_NORDIGEN = os.getenv("SECRET_KEY_NORDIGEN")
    SECRET_KEY_NORDIGEN = os.getenv("SECRET_KEY_NORDIGEN")
    
    DEBUG = True

    # jwt configuration
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(minutes=int(os.getenv("JWT_ACCESS_TOKEN_EXPIRES")))
    JWT_REFRESH_TOKEN_EXPIRES = timedelta(days=int(os.getenv("JWT_REFRESH_TOKEN_EXPIRES")))

class ProductionConfig:
    FLASK_SECRET_KEY = os.getenv("FLASK_SECRET_KEY")
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")
    
    SECRET_ID_NORDIGEN = os.getenv("SECRET_KEY_NORDIGEN")
    SECRET_KEY_NORDIGEN = os.getenv("SECRET_KEY_NORDIGEN")
    
    DEBUG = False

    # jwt configuration
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(minutes=int(os.getenv("JWT_ACCESS_TOKEN_EXPIRES")))
    JWT_REFRESH_TOKEN_EXPIRES = timedelta(days=int(os.getenv("JWT_REFRESH_TOKEN_EXPIRES")))
