from flask import Flask
from config import config

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    config[config_name].init_app(app)

    #assiciar rotas a paginas de erro personalizadas aqui
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app

