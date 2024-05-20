from functools import wraps
from flask import abort
from flask_login import current_user

from .models import Permission


def permission_required(perm):
    def decorator(f):
        @wraps(f)
        def decoder_function(*args, **kwargs):
            if not current_user.can(perm):
                abort(403)
            return f(*args, **kwargs)

        return decoder_function

    return decorator


def admin_requared(f):
    return permission_required(Permission.ADMIN)(f)
