from app.config.dev import DevelopmentConfig
from app.config.prod import ProductionConfig
from app.infra.api.app import create_app
from dotenv import load_dotenv
import os

load_dotenv()

Config = DevelopmentConfig \
    if os.getenv('FLASK_ENV') == 'development' \
    else ProductionConfig

app = create_app(Config)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))