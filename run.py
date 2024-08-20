from app.config.development import DevelopmentConfig
from app.config.production import ProductionConfig
from app.infrastructure.api.api import create_app
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Create an instance of the Flask application
Config = DevelopmentConfig \
    if os.getenv('FLASK_ENV') == 'development' \
    else ProductionConfig

app = create_app(Config)

if __name__ == '__main__':
    # Run the application on the default port (5000) or a port specified by an environment variable
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
