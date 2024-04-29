from flask import Flask
from config import Config
from models import db
from routes import blacklist_bp
import os

print('test_02')

application = Flask(__name__)
application.app_context()
application.config.from_object(Config)

if os.environ.get("FLASK_ENV") is None:
    application.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    application.config['TESTING'] = True


db.init_app(application)

application.register_blueprint(blacklist_bp)


if __name__ == '__main__':
    application.run(port=3000, debug=True)
