import os

from flask import Flask
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

from flask_sqlalchemy import SQLAlchemy
# from app.api.fundamental_data import fundamental_data_blueprint
# from app.api.historical_data import historical_data_blueprint

from config import config


# import postgres.__all_models


def register_blueprints(app):
    from app.api import api as api_blueprint
    from app.api.historical_data import historical_data_blueprint
    from app.api.fundamental_data import fundamental_data_blueprint

    app.register_blueprint(api_blueprint, url_prefix='/api/')
    app.register_blueprint(historical_data_blueprint, url_prefix='/api/historical_data/')
    app.register_blueprint(fundamental_data_blueprint, url_prefix='/api/fundamental_data/')


def create_app(config_name) -> Flask:
    print('Creating Flask app for {}'.format(config_name))
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    # register_blueprints(app)

    return app

# print('os.getenv(FLASK_CONFIG): {}'.format(os.getenv('FLASK_CONFIG')))
app = create_app(os.getenv('FLASK_CONFIG') or 'default')
db = SQLAlchemy(app)

register_blueprints(app)

manager = Manager(app)

manager.add_command('db', MigrateCommand)
migrate = Migrate(app, db)
