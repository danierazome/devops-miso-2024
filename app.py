from flask import Flask
from flask_migrate import Migrate, upgrade
from config import Config
from models import db
from routes import blacklist_bp


def create_app():
    app = Flask(__name__)
    app.app_context()
    app.config.from_object(Config)

    db.init_app(app)
    migrate = Migrate(app, db)

    with app.app_context():
        upgrade()
    print('Migraciones aplicadas correctamente')

    app.register_blueprint(blacklist_bp)

    return app


app = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)