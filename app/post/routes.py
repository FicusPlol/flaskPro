from flask import flash, url_for, redirect, render_template, request
from flask_login import current_user

from . import post
from .forms import *
from ..models import *
from .utils import *


@post.route('/new', methods=['GET', 'POST'])
def new_post():
    '''
    Содает новый пост
    из полученных данных(формы) создает и сохраняет новый пост и картинку
    return: на страницу со всеми постами
    '''
    form = PostForm()
    if request.method == 'POST':
        post = Post(title=request.form['title'], content=request.form['content'], image_post=form.picture.data,
                    user_id=current_user.get_id())
        # file_name = secure_filename(form.picture.data.filename)
        picture_file = save_picture_post(form.picture.data)
        post.image_post = picture_file
        db.session.add(post)
        db.session.commit()
        flash('okk', 'success')
        return redirect(url_for('post.articles'))
    image_file = url_for('static', filename='pic/reg.jpg')
    return render_template('create_post.html', form=form, image_file=image_file)


@post.route('/articles')
def articles():
    """
    Открывает страницу со всеми постами
    """
    posts = Post.query.all()
    return render_template('all_posts.html', posts=posts)


@post.route('/post/<id>')
def open_article(id):
    """
    Открывает пост по id
    :param id: id поста
    :return: открывает страницу поста по id
    """
    post = Post.query.filter_by(id=id).first_or_404()
    user = post.user_id
    u = Profiles.query.filter_by(user_id=user).first_or_404()
    print(post)
    return render_template('article.html', post=post, name=u.name)
