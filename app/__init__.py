from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask import Flask

from app.config import Config

db = SQLAlchemy()
mi = Migrate()


def create_app():
    """
    function run app
    """
    app = Flask(__name__)

    app.config.from_object(Config)
    db.init_app(app)

    mi.init_app(app, db, render_as_batch=True)

    from .views import views
    app.register_blueprint(views)

    return app
