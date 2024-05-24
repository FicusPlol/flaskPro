

from flask import flash, url_for, redirect, render_template, request
from flask_login import current_user

from . import post
from .forms import *
from ..models import *
from .utils import *


@post.route('/post/new', methods=['GET', 'POST'])
def new_post():
    form = PostForm()
    if request.method == 'POST' :
        post = Post(title= request.form['title'], content= request.form['content'], image_post=form.picture.data,
                    user_id=current_user.get_id())
        picture_file = save_picture_post(form.picture.data)
        post.image_post = picture_file
        db.session.add(post)
        db.session.commit()
        flash('okk', 'success')
        return redirect(url_for('main.index'))
    image_file = url_for('static', filename='pic/reg.jpg')
    return render_template('create_post.html', form=form, image_file=image_file)
