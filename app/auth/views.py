from threading import Thread

from flask import render_template, redirect, url_for, flash, request, session, current_app
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash
from flask_mail import Message
from flask_mail import *

from .forms import *
from . import auth
from .. import db
from ..models import *
from .. import mail


@auth.before_app_request
def before_request():
    if current_user.is_authenticated and not current_user.confirmed and request.blueprint != 'auth' \
            and request.endpoint != 'static':
        return redirect(url_for('auth.unconfirmed'))

@auth.route('/confirm/<token>')
@login_required
def confirm(token):
    if current_user.confirm:
        return redirect(url_for('main.index'))
    if current_user.confirm(token):
        db.session.commit()
        flash('it is okk')
    else:
        flash('opppsss')
    return redirect(url_for('main.index'))

@auth.route("/unconfirmed")
def unconfirmed():
    return "Not confirmed. Unfortunately"

def send_confirm(msg):
    from app_file import app
    thread = Thread(target=send_async_email, args=[app, msg])
    thread.start()
    return thread


@auth.route("/register", methods=['POST', 'GET'])
def register():
    form = ContactForm()
    if request.method == 'POST':
        hash = generate_password_hash(request.form['psw'])
        user = Users(email=request.form['email'], psw=hash)
        name = request.form['name']
        email1=request.form['email']
        db.session.add(user)
        db.session.commit()
        p = Profiles(name=name, city=request.form['city'], user_id=user.id)
        db.session.add(p)
        db.session.commit()
        print(user,p)
        token = user.generate_confirmation_token()
        print(token)
        msg = Message('Subject', sender=current_app.config['MAIL_USERNAME'], recipients=[email1])
        msg.body = render_template('confirm.txt', name=name, token=token.decode('utf-8'))
        send_confirm(msg)
        id = user.id
        return redirect(url_for('main.user', id=id))

    return render_template('form_register.html')


def send_async_email(app, msg):
    with app.app_context():
        mail.send(msg)




@auth.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email1 = request.form['email']
        psw = request.form['psw']
        hash = generate_password_hash(request.form['psw'])
        user = Users.query.filter((Users.email == email1) and (Users.psw == hash)).first()
        id = user.id
        print(user)
        if user:
            print('if yess')
            login_user(user)
            print("вошел!")
            next_page = request.args.get("next")
            if not next_page or not next_page.startswith('/'):
                next_page = url_for('main.user', id=id)
            return redirect(next_page)
        flash('Invalid username or password', 'error')
    return render_template('form_login.html')


@auth.route("/logout")
def logout():
    print('before logout')
    logout_user()
    print('успех!')
    flash('You have been logged out.')
    return redirect(url_for('main.none'))


'''
@auth.route("/register", methods=['POST', 'GET'])
def register():

    form = ContactForm()
    if request.method == 'POST':
        hash = generate_password_hash(request.form['psw'])
        u = Users(email=request.form['email'], psw=hash)
        email1 = request.form['email']
        db.session.add(u)
        db.session.commit(u)
        p = Profiles(name=request.form['name'], city=request.form['city'], user_id=u.id)
        db.session.add(p)
        db.session.commit()
        id=u.id
        return redirect(url_for('main.user',id=id))

    return render_template('form_register.html')



        if request.form.get('send') == 'True':
            msg = Message('Subject', sender=app.config['MAIL_USERNAME'], recipients=[email1])
            msg.html = render_template('email.html', name='Project')
            mail.send(msg)
            print('Email sent!')
'''
