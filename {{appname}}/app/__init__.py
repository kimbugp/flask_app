
import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


db = SQLAlchemy()
migrate = Migrate()


def create_app(script_info=None):

    # instantiate the app
    app = Flask(
        __name__
    )

    app_settings = os.environ.get(
        "APP_SETTINGS", "project.server.config.ProductionConfig"
    )
    app.config.from_object(app_settings)

    db.init_app(app)
    migrate.init_app(app, db)

    # register blueprints
    from views import sample_blueprint
    app.register_blueprint(sample_blueprint)

    return app
