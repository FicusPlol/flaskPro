import os
import secrets
from PIL import Image
from werkzeug.utils import secure_filename
from flask import current_app


def save_picture_post(form_picture):
    random_hex = secrets.token_hex(16)
    picture_r = random_hex + '.png'
    print(picture_r)
    full_path = os.path.join(current_app.root_path, 'static', 'post_images')
    if not os.path.isdir(full_path):
        os.makedirs(full_path)
    picture_p = os.path.join(full_path, picture_r)
    print(picture_p)
    form_picture.save(picture_p)
    return picture_r
