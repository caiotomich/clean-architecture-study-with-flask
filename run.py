from app.infrastructure.api import create_app
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Create an instance of the Flask application
app = create_app()

if __name__ == '__main__':
    # Run the application on the default port (5000) or a port specified by an environment variable
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
