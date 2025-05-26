from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os
import logging


db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)

    # Load config from environment variable
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    migrate.init_app(app, db)

    # Import and register blueprints/routes here
    from . import models
    from .routes import students_bp
    app.register_blueprint(students_bp)
    from .routes import health_bp
    app.register_blueprint(health_bp)
    return app
