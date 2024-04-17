from flask import render_template, redirect, url_for, flash, request, session
from flask_login import login_user, logout_user
from werkzeug.security import generate_password_hash
from flask_mail import Message


from .forms import *
from . import auth
from .. import db
from ..models import *
from .. import mail


@auth.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email1 = request.form['email']
        psw = request.form['psw']
        hash = generate_password_hash(request.form['psw'])
        user = Users.query.filter((Users.email == email1) and (Users.psw == hash)).first()
        print(user)
        if user:
            print('if yess')
            login_user(user)
            print("вошел!")
            next_page = request.args.get("next")
            if not next_page or not next_page.startswith('/'):
                next_page = url_for('main.index')
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

@auth.route("/register", methods=['POST', 'GET'])
def register():

    form = ContactForm()
    if request.method == 'POST':

        hash = generate_password_hash(request.form['psw'])
        u = Users(email=request.form['email'], psw=hash)
        email1 = request.form['email']
        db.session.add(u)
        db.session.commit()
        p = Profiles(name=request.form['name'], city=request.form['city'], user_id=u.id)
        db.session.add(p)
        db.session.commit()

        return redirect(url_for('main.index'))

    return render_template('form_register.html')

'''
        if request.form.get('send') == 'True':
            msg = Message('Subject', sender=app.config['MAIL_USERNAME'], recipients=[email1])
            msg.html = render_template('email.html', name='Project')
            mail.send(msg)
            print('Email sent!')
'''