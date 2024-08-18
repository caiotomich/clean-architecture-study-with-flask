from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.config.development import DevelopmentConfig
from app.config.production import ProductionConfig
import os

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    Config = DevelopmentConfig \
        if os.getenv('FLASK_ENV') == 'development' \
        else ProductionConfig

    app.config.from_object(Config)

    db.init_app(app)

    # Import and register blueprints or routes
    from app.domain.entities.user.controller import user_controller
    app.register_blueprint(user_controller)

    with app.app_context():
        try:
            db.create_all()
            print(" * Database tables created")
        except Exception as e:
            print(f"Error creating tables: {e}")

    return app