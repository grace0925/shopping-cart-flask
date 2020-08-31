from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import os


db = SQLAlchemy()


def create_app():
    template_dir = os.path.abspath('./templates')
    static_dir = os.path.abspath('./static')

    app = Flask(__name__, template_folder=template_dir, static_folder=static_dir)
    app.config.from_object("config.Config")
    CORS(app)

    db.init_app(app)

    with app.app_context():
        from . import routes
        db.create_all()
        return app


