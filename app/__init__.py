from flask import Flask
from flask_migrate import Migrate
from app.models import db
from app.models.all_models import *
from app.views import api_v1

migrate = Migrate()

app = Flask(__name__)

def create_app(enviroment):
    app.config.from_object(enviroment)

    db.init_app(app)

    if enviroment.TEST:
        with app.app_context():
            db.create_all()
    else:
        with app.app_context():
            migrate.init_app(app, db)

    app.register_blueprint(api_v1)

    return app