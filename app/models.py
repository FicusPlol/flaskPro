from datetime import datetime

from authlib.jose import JsonWebSignature
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from . import db, login_manager


class Users(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50), unique=True)
    psw = db.Column(db.String(500), nullable=True)
    date = db.Column(db.DateTime, default=datetime.utcnow)
    confirmed = db.Column(db.Boolean, default=False)


    def generate_confirmation_token(self):
        jws = JsonWebSignature()
        protected = {'alg': 'HS256'}
        payload = self.id
        secret = 'secret'
        return jws.serialize_compact(protected, payload, secret)

    def confirm(self, token):
        jws = JsonWebSignature()
        data = jws.deserialize_compact(s=token, key='secret')
        if data.payload.decode('utf-8') != str(self.id):
            print("it's not your token")
            return False
        else:
            self.confirmed = True
            db.session.add(self)
            return True

    pr = db.relationship('Profiles', backref='users', uselist=False)

    @property
    def password(self):
        raise AttributeError("password not enable to read")

    @password.setter
    def password(self, password):
        self.psw = generate_password_hash(password, method='pbkdf2:sha256')

    def verify(self, password):
        return check_password_hash(self.psw, password)

    def __repr__(self):
        return f"<users {self.id}>"


@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(int(user_id))

    def __repr__(self):
        return f"<users {self.id}>"


class Profiles(UserMixin, db.Model):
    __tablename__ = 'profiles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=True)
    city = db.Column(db.String(50))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __repr__(self):
        return f"<profiles {self.id}>"


'''
class Profile(db.Model):
    __tablename__ = 'profiles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=True)
    city = db.Column(db.String(50))

    def __repr__(self):
        return f"<profile {self.id}>"
'''
