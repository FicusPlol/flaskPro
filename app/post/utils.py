import os
import secrets
from PIL import Image

from flask import current_app
from flask_login import current_user


def save_picture_post(form_pic):
    random_hex = secrets.token_hex(16)
    picture_r = random_hex + '.png'
    full_path = os.path.join(current_app.root_path, 'static', 'profile_pics', current_user.get_id(), 'post_images')
    print(os.path.exists(full_path) )
    if not os.path.isdir(full_path):
        print(full_path,777)
        os.makedirs(full_path)

    picture_p = os.path.join(full_path, picture_r)
    print(picture_p,picture_r)
    output_size = (500, 500)
    form_pic.save(picture_p)

    i = Image.open(form_pic) #полный игнор этого!!!!
    i.thumbnail(output_size)
    i.save(picture_p)
    return picture_r
