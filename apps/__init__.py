import os
from flask import Flask
from apps.config import config

def create_app():
    app = Flask(__name__)
    config_name = os.environ.get("CONFIG", "local")
    app.config.from_object(config[config_name])

    from .routes import bp
    app.register_blueprint(bp)
    return app
