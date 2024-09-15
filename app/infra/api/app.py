from flask import Flask
from app.infra.database import db

def create_app(Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    # Import and register blueprints or routes
    from app.infra.api.controllers.api_controller import api_controller
    app.register_blueprint(api_controller)
    from app.infra.api.controllers.auth_controller import authentication
    app.register_blueprint(authentication)
    from app.infra.api.controllers.users_controller import users_controller
    app.register_blueprint(users_controller)

    with app.app_context():
        try:
            db.create_all()
            print(" * Database tables created")
        except Exception as e:
            print(f"Error creating tables: {e}")

    return app