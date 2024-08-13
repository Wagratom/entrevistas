# app/app.py
from flask import Flask
from app.infrastructure.db.database import init_db
from app.infrastructure.web.controllers.equipamento_controllers import equipamento_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.Config')

    init_db(app)

    app.register_blueprint(equipamento_bp)

    return app
