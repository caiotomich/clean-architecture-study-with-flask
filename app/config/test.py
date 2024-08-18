import os

class TestConfig:
    TESTING = True
    # SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'  # Use an in-memory SQLite database
    SQLALCHEMY_DATABASE_URI = 'sqlite:///test.db'  # Use an in-memory SQLite database
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv('SECRET_KEY', 'default_secret_key')
