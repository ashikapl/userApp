from flask import Flask
from app.api.api import user_bp

def create_app():
    app = Flask(__name__)
    app.register_blueprint(user_bp, url_prefix="/users")
    return app