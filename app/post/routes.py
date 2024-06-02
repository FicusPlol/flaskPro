from flask import flash, url_for, redirect, render_template, request
from . import post
from .forms import *
from ..models import *
from .utils import *


@post.route('/new', methods=['GET', 'POST'])
def new_post():
    form = PostForm()
    if request.method == 'POST':
        post = Post(title=request.form['title'], content=request.form['content'], image_post=form.picture.data,
                    user_id=current_user.get_id())
        print(1, form.picture)
        print(2, form.picture.data)
        file_name = secure_filename(form.picture.data.filename)
        print(3, file_name)
        picture_file = save_picture_post(form.picture.data)
        post.image_post = picture_file
        db.session.add(post)
        db.session.commit()
        flash('okk', 'success')
        return redirect(url_for('main.index'))
    image_file = url_for('static', filename='pic/reg.jpg')
    return render_template('create_post.html', form=form, image_file=image_file)


@post.route('/posts')
def articles():
    posts = []
    posts = Post.query.all()
    print('posts: ', posts)
    return render_template('all_posts.html', posts=posts)


@post.route('/post/<id>')
def open_article(id):
    post = Post.query.filter_by(id=id).first_or_404()
    user = post.user_id
    u = Profiles.query.filter_by(user_id=user).first_or_404()
    print(post)
    return render_template('article.html', post=post, name=u.name)
