import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'secret6754345356567rrr'
    MAIL_SERVER = os.environ.get('MAIL_SERVER') or 'smtp.googlemail.com'
    MAIL_PORT = os.environ.get('MAIL_PORT') or '587'
    MAIL_USE_TLS = int(os.environ.get('MAIL_USE_TLS', '5870'))
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME') or 'ficusplol@gmail.com'
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD') or 'vaqm jhyq fhdf nsue'
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    @staticmethod
    def init_app(app):
        pass


class DevelConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
                              "mysql://root:@localhost/flask_db"


class TestConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
                              'mysql://root:@localhost/flask_db'


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
                              'mysql://root:@localhost/flask_db'


config = {
    'development': DevelConfig,
    'testing': TestConfig,
    'production': ProductionConfig,
    'default': DevelConfig
}

'''
import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'secret6754345356567rrr'
    MAIL_SERVER = os.environ.get('MAIL_SERVER') or 'smtp.googlemail.com'
    MAIL_PORT = os.environ.get('MAIL_PORT') or '587'
    MAIL_USE_TLS = int(os.environ.get('MAIL_USE_TLS', '5870'))
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME') or 'ficusplol@gmail.com'
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD') or 'vaqm jhyq fhdf nsue'
    SQLALCHEMY_TRACK_MODIFICATIONS = True


class DevelConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
                              'mysql://root:@localhost/flask_db'


class TestConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
                              'mysql://root:@localhost/flask_db'


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
                              'mysql://root:@localhost/flask_db'


config = {
    'development': DevelConfig,
    'testing': TestConfig,
    'production': ProductionConfig,
    'default': DevelConfig
}

'
app.config['SECRET_KEY'] = 'secret6754345356567rrr'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/flask_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'rambler124413@gmail.com'
app.config['MAIL_PASSWORD'] = 'vkru wwgm rjpy aabf'


'
app.config['SECRET_KEY'] = 'secret6754345356567rrr'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/flask_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'rambler124413@gmail.com'
app.config['MAIL_PASSWORD'] = 'vkru wwgm rjpy aabf'
'''
