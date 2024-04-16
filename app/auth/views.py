from flask import render_template, redirect, url_for, flash, request, session
from flask_login import login_user, logout_user
from werkzeug.security import generate_password_hash
from flask_mail import Message

from app_file import app
from .forms import *
from .. import mail
from .. import db
from ..models import *
from . import auth


@auth.route("/login", methods=['GET', 'POST'])
def login():
    pass

@auth.route('/register', methods=['POST', 'GET'])
def register():
    print(66666)
    form = ContactForm()
    if request.method == 'POST':

        hash = generate_password_hash(request.form['psw'])
        u = Users(email=request.form['email'], psw=hash)  # not work
        email1 = request.form['email']
        db.session.add(u)
        db.session.commit()
        p = Profiles(name=request.form['name'], city=request.form['city'], user_id=u.id)  # not work
        db.session.add(p)
        db.session.commit()

        if request.form.get('send') == 'True':
            msg = Message('Subject', sender=app.config['MAIL_USERNAME'], recipients=[email1])
            msg.html = render_template('email.html', name='Project')
            mail.send(msg)
            print('Email sent!')

        return redirect(url_for('main.index'))

    return render_template('form_register.html')
