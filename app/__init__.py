import os
from flask_bootstrap import Bootstrap5
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
from flask import Flask
from flask_wtf import CSRFProtect
from flask_login import LoginManager
from config import config
from authlib.integrations.flask_client import OAuth
bootstrap = Bootstrap5()
db = SQLAlchemy()
mail = Mail()
oauth=OAuth()
migrate = Migrate()
login_manager = LoginManager()
login_manager.session_protection ='strong'
login_manager.login_view = 'auth.login'
def create_app(config_name="default"):
    app = Flask(__name__)
    csrf = CSRFProtect(app)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    migrate.init_app(app, db)
    bootstrap.init_app(app)
    mail.init_app(app)

    db.init_app(app)
    oauth.init_app(app)
    login_manager.init_app(app)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint, config=config)

    from .auth import auth as auth_blueprint

    app.register_blueprint(auth_blueprint, url_prefix='/auth')



    return app



'''

from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='auth')
    
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
