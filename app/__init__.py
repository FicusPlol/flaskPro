import os
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
from flask import Flask
from config import config

bootstrap = Bootstrap()
db = SQLAlchemy()
mail = Mail()


def create_app(config_name="default"):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    bootstrap.init_app(app)
    mail.init_app(app)
    db.init_app(app)
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app


'''
стар версия
import os
from datetime import datetime

from flask_sqlalchemy import SQLAlchemy
from flask_mail import *
from flask import Flask
from flask_wtf import CSRFProtect

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret6754345356567rrr'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/flask_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

csrf = CSRFProtect(app)
from flask_bootstrap5 import Bootstrap

bootstrap = Bootstrap(app)
db = SQLAlchemy(app)


app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
app.config['MAIL_PORT']= 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'ficusplol@gmail.com'
app.config['MAIL_PASSWORD'] = 'vaqm jhyq fhdf nsue'
mail = Mail(app)

from app import routes
from models import Users, Profiles

from flask_bootstrap5 import Bootstrap


with app.app_context():
    db.create_all()
    '''