from datetime import datetime

from authlib.jose import JsonWebSignature
from flask_login import UserMixin, AnonymousUserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from . import db, login_manager


class Post(db.Model):
    __tablename__ = 'post'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    data_post = db.Column(db.DateTime, default=datetime.utcnow)
    content = db.Column(db.Text(2000), nullable=False)
    image_post = db.Column(db.String(50), nullable=True, default='def.jpg')
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    def __repl__(self):
        return f'Users({self.title},{self.data_post},{self.image_post}'


class Permission:
    FOLLOW = 1
    COMMENT = 2
    WRITE = 4
    MODERATE = 8
    ADMIN = 16


class Role(db.Model):
    __tablename__ = 'role'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60))
    users = db.relationship('Users', backref='role', lazy='dynamic')
    default = db.Column(db.Boolean, default=False, index=True)
    permission = db.Column(db.Integer)

    def __init__(self, **kwargs):
        super(Role, self).__init__(**kwargs)
        if self.permission is None:
            self.permission = 0

    def __repl__(self):
        return '<Role %r>' % self.name

    @staticmethod
    def insert_roles():
        roles = {
            'User': [Permission.FOLLOW, Permission.COMMENT, Permission.WRITE],
            'Moderator': [Permission.FOLLOW, Permission.COMMENT, Permission.WRITE, Permission.MODERATE],
            'Administrator': [Permission.FOLLOW, Permission.COMMENT, Permission.WRITE, Permission.MODERATE,
                              Permission.ADMIN],

        }
        default_role = 'User'
        for r in roles:
            role = Role.query.filter_by(name=r).first()
            if role is None:
                role = Role(name=r)
            role.reset_permission()
            for perm in roles[r]:
                role.add_permission(perm)
            role.default = (role.name == default_role)
            db.session.add(role)
        db.session.commit()

    def has_permission(self, perm):
        return self.permission & perm == perm

    def reset_permission(self):
        self.permission = 0

    def add_permission(self, perm):
        if not self.has_permission(perm):
            self.permission += perm

    def remove_permission(self, perm):
        if self.has_permission(perm):
            self.permission -= perm


class Users(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50), unique=True)
    psw = db.Column(db.String(500), nullable=True)
    date = db.Column(db.DateTime, default=datetime.utcnow)
    confirmed = db.Column(db.Boolean, default=False)
    role_id = db.Column(db.Integer, db.ForeignKey('role.id'),default=2)

    def __init__(self, **kwargs):
        super(Users, self).__init__(**kwargs)
        if self.role is None:
            if self.email == 'tfgv60@gmail.com':
                self.role = Role.query.filter_by(name='Administrator').first()
            if self.role is None:
                self.role = Role.query.filter_by(default=True).first()

    def can(self, perm):
        return self.role is not None and self.role.has_permission(perm)

    def is_admin(self):
        return self.can(Permission.ADMIN)

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
            print("uuuuuu")
            self.confirmed = True
            db.session.add(self)
            return True

    pr = db.relationship('Profiles', backref='users', uselist=False)

    @property
    def password(self):
        raise AttributeError("password not enable to read")

    @password.setter
    def set_password(self, password):
        self.psw = generate_password_hash(password, method='pbkdf2:sha256')

    def verify(self, password):
        return check_password_hash(self.psw, password)

    def __repr__(self):
        return f"<users {self.id}>"


class Profiles(UserMixin, db.Model):
    __tablename__ = 'profiles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=True)
    city = db.Column(db.String(50))
    image = db.Column(db.String(50), nullable=True, default='default.jpg')
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    ex = db.relationship('Extra_Info_Profile', backref='profiles', uselist=False)

    def __repr__(self):
        return f"<profiles {self.id}>"


class Extra_Info_Profile(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    job = db.Column(db.String(50), default="--")
    website = db.Column(db.String(100), default="--")
    github = db.Column(db.String(100), default="--")
    twiter = db.Column(db.String(100), default="--")
    insta = db.Column(db.String(100), default="--")
    facebook = db.Column(db.String(100), default="--")
    phone = db.Column(db.String(20), default="--")
    prof_id = db.Column(db.Integer, db.ForeignKey('profiles.id'))


class AnonymousUser(AnonymousUserMixin):
    def can(self, perm):
        return False

    def is_admin(self):
        return False


@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(int(user_id))

    def __repr__(self):
        return f"<users {self.id}>"


login_manager.anonymous_user = AnonymousUser
