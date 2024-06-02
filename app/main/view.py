from flask import render_template, redirect, url_for, request
from flask_login import current_user, login_required
from app.models import *
from . import main
from .forms import *
from .utils import *


@main.route('/')
@main.route('/index')
def index():
    """
    Функция возвращает главную страницу
    :return: переход на главный экран
    """
    return render_template('index.html')


@main.app_context_processor
def now_user():
    """
    общая информация о юзере досмтупная во всех вкладках и темплейтах
    :return: словарь с информацией о нынешнем юзере
    """
    user = current_user
    return dict(now_user=user)


@main.route('/none')
def none():
    """
    страница выхода
    :return: происходит переход на страницу с сообщением о выходе из уч.записи
    """
    return render_template('none.html')


@main.route('/user/<id>')
@login_required
def user(id):
    """
    Если пользователь открыл свою страницу. то ему доступна кнопка редактирования профиля, иначе ее нет-
    авторизированный пользователь может лишь просмотреть информацию профиля, владелец - еще и редактировать
    :param id: id юзера
    :return: отправляет на стринцу пользователя
    """
    user = Users.query.filter_by(id=id).first_or_404()
    profile = Profiles.query.filter_by(user_id=user.id).first_or_404()
    info = Extra_Info_Profile.query.filter_by(prof_id=profile.id).first_or_404()
    posts = Post.query.filter_by(user_id=id)
    f = False
    if int(user.id) == int(current_user.get_id()):
        f = True
    return render_template('profile.html', f=f, user=user, profile=profile, info=info, posts=posts)


@main.route('/user_edit/<id>', methods=['GET', 'POST'])
@login_required
def user_edit(id):
    """
    Открывает страницу для редактирования данных пользователя
    :param id: id юзера
    :return: возвращает на страницу профиля
    """
    user = Users.query.filter_by(id=id).first_or_404()
    profile = Profiles.query.filter_by(user_id=user.id).first_or_404()
    info = Extra_Info_Profile.query.filter_by(prof_id=profile.id).first_or_404()
    posts = Post.query.filter_by(user_id=id)
    form = Edit()
    if request.method == 'POST':
        if form.image.data:
            if profile.image != 'def.jpg':
                p = os.path.join(current_app.root_path, 'static', 'profile_images', profile.image)
                os.remove(p)
            pic = save_picture_post(form.image.data)
            profile.image = pic

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
        return redirect(url_for('main.user', id=user.id))

    return render_template('profile_edit.html', user=user, profile=profile, form=form, info=info, posts=posts)


@main.route('/post_delete/<id>', methods=['GET', 'POST'])
@login_required
def post_edit(id):
    """
    Удаление поста
    :param id: id поста
    :return: страница редактирования профиля (пользователь остается на той же странице)
    """
    post = Post.query.filter_by(id=id).first_or_404()
    db.session.delete(post)
    db.session.commit()
    p = os.path.join(current_app.root_path, 'static', 'post_images', post.image_post)
    os.remove(p)
    return redirect(url_for('main.user_edit', id=post.user_id))


@main.errorhandler(404)
def page_not_found(e):
    """
    Открывает страницу с ошибкой 404
    :param e: error
    :return: страницу ошибки
    """
    return render_template("error.html"), 404
