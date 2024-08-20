from flask import Flask
from app.infrastructure.database import db

def create_app(Config):
    app = Flask(__name__)

    app.config.from_object(Config)

    db.init_app(app)

    # Import and register blueprints or routes
    from app.infrastructure.api.controllers.api import api_controller
    app.register_blueprint(api_controller)

    from app.infrastructure.api.controllers.users import user_controller
    app.register_blueprint(user_controller)

    with app.app_context():
        try:
            db.create_all()
            print(" * Database tables created")
        except Exception as e:
            print(f"Error creating tables: {e}")

    return app