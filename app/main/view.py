from flask import render_template, redirect, url_for, request
from flask_login import current_user, login_required
from werkzeug.security import generate_password_hash
from flask_mail import Message
import app
from app.models import *
from . import main
from .forms import ContactForm
from .. import mail

from ..decorators import admin_requared,permission_required
@main.route('/')
@main.route('/index')
def index():
    print(current_user._get_current_object())
    print(current_user.get_id())
    info = []
    try:
        info = Users.query.all()
    except:
        print("Ошибка чтения из БД")
    if current_user._get_current_object() in info:
        return render_template('index.html', list=info)
    else:
        return render_template('index.html')

@main.route('/admin')
@login_required
@admin_requared
def for_admin():
    return 'for admin'


@main.route('/moder')
@login_required
@permission_required(Permission.MODERATE)
def for_moder():
    return 'for moder'
@main.app_context_processor
def now_user():
    user = current_user
    return dict(now_user=user)


@main.route('/none')
def none():
    return render_template('none.html')
@main.route('/art')
def art():
    return render_template('article.html')


@main.route('/user/<id>')
@login_required
def user(id):
    print(id)
    user = Users.query.filter_by(id=id).first_or_404()
    profile = Profiles.query.filter_by(user_id=user.id).first_or_404()
    info = Extra_Info_Profile.query.filter_by(prof_id=profile.id).first_or_404()
    print(user, profile)

    return render_template('profile.html', user=user, profile=profile, info=info)


@main.route('/user_edit/<id>', methods=['GET', 'POST'])
@login_required
def user_edit(id):
    print(id)
    user = Users.query.filter_by(id=id).first_or_404()
    profile = Profiles.query.filter_by(user_id=user.id).first_or_404()
    info = Extra_Info_Profile.query.filter_by(prof_id=profile.id).first_or_404()
    print(user, profile, info)
    if request.method == 'POST':
        print('there issssssssss')
        user.email = request.form['email']

        profile.name = request.form['name']
        profile.city = request.form['city']

        info.phone = request.form['phone']
        info.website = request.form['web']
        info.github = request.form['git']
        info.twiter = request.form['twit']
        info.insta = request.form['insta']
        info.facebook = request.form['face']
        info.job = request.form['job']
        db.session.commit()
        print(info.job)
        return redirect(url_for('main.user', id=user.id))

    return render_template('profile_edit.html', user=user, profile=profile, info=info)


'''
@main.route('/register', methods=['POST', 'GET'])
def register():
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


@main.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        email1 = request.form['email']
        print(email1)
        return redirect(url_for('main.index'))

    return render_template('form_login.html')

'''


@main.errorhandler(404)
def page_not_found(e):
    return render_template("error.html"), 404


''''
@main.view('/error')
def error():
    return render_template('error.html'), 403


@app.errorhandler(404)
def page_not_found(e):
    return render_template("error.html"), 404
    
    
old version

from flask_mail import Message

from flask import render_template, session, redirect, url_for, request
from werkzeug.security import generate_password_hash
from models import Users,Profiles
from app.forms import ContactForm
from app import app, db,mail


@app.route('/')
@app.route('/index')
def index():
    info = []
    try:
        info = Users.query.all()
    except:
        print("Ошибка чтения из БД")
    return render_template('index.html',list=info)



@app.route('/register', methods=['POST','GET'])
def register():
    if request.method == 'POST':
        hash = generate_password_hash(request.form['psw'])
        u = Users(email=request.form['email'], psw=hash)#not work
        email1 = request.form['email']
        db.session.add(u)
        db.session.commit()
        p = Profiles(name=request.form['name'], city=request.form['city'], user_id=u.id)  # not work
        db.session.add(p)
        db.session.commit()

        if request.form.get('send')=='True':
            msg = Message('Subject', sender=app.config['MAIL_USERNAME'], recipients=[email1])
            msg.html = render_template('email.html', name='Project')
            mail.send(msg)
            print('Email sent!')


        return redirect(url_for('index'))

    return render_template('form_register.html')

@app.route('/login', methods=['POST','GET'])
def login():
    if request.method == 'POST':
        email1 = request.form['email']
        print(email1)
        return redirect(url_for('index'))

    return render_template('form_login.html')



@app.route('/error')
def error():
    return render_template('error.html'), 403


@app.errorhandler(404)
def page_not_found(e):
    return render_template("error.html"), 404
'''
