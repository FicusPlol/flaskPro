import os
from flask_admin.contrib.sqla import ModelView
import flask_admin
from flask_bootstrap import Bootstrap5
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
from flask import Flask,abort, redirect, url_for, request
from flask_wtf import CSRFProtect
from flask_login import LoginManager, current_user
from config import config
from authlib.integrations.flask_client import OAuth
from flask_admin import Admin, AdminIndexView
from flask_admin import Admin, expose
from flask_admin.contrib import sqla
from flask_login import LoginManager, current_user






bootstrap = Bootstrap5()
db = SQLAlchemy()
mail = Mail()
oauth = OAuth()
migrate = Migrate()
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'
admin = Admin()


class MyModelView(sqla.ModelView):
    def is_accessible(self):
        return (current_user.is_active and
                current_user.is_authenticated and
                current_user.role_id == 1
                )

    def _handle_view(self, name, **kwargs):
        if not self.is_accessible():
            if current_user.is_authenticated:
                abort(403)
            else:
                return redirect(url_for('main.index', next=request.url))


class MyAdminIndexView(flask_admin.AdminIndexView):
    @expose('/')
    def index(self):
        if not current_user.is_authenticated:
            return redirect(url_for('auth.login'))
        return super(MyAdminIndexView, self).index()


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
    app.register_blueprint(main_blueprint, config=config, name='main')
    # new
    from .post import post as post_blueprint
    app.register_blueprint(post_blueprint, config=config,url_prefix='/post')
    #
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, name='auth', url_prefix='/auth')
    from app.models import Users,Profiles,Extra_Info_Profile
    admin = flask_admin.Admin(app, index_view=MyAdminIndexView())
    admin.add_view(MyModelView(Users, db.session))
    admin.add_view(MyModelView(Profiles, db.session))
    admin.add_view(MyModelView(Extra_Info_Profile, db.session))

    return app


#admin = Admin(name="My Web")
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
