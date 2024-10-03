from flask import Flask
from database.sessao import db
from settings.config import Config
from routes.transacao import register_routes

def create_app():
    app = Flask(__name__)

    app.config.from_object(Config)

    db.init_app(app)

    with app.app_context():
        db.create_all() # criar todas as tabelas

    register_routes(app)
    
    return app