from flask import Flask
from .models import db
from .models.task import Task

app = Flask(__name__)


def create_app(environment):
    app.config.from_object(environment)

    with app.app_context():
        db.init_app(app)
        db.create_all()

    return app
