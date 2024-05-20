import unittest
from flask import current_app
from app import create_app, db
from app.models import *

class RoleTestСase(unittest.TestCase):


    def test_anon(self):
        user=AnonymousUser()
        self.assertFalse(user.can(Permission.ADMIN))
        self.assertFalse(user.can(Permission.MODERATE))
        self.assertFalse(user.can(Permission.FOLLOW))
        self.assertFalse(user.can(Permission.WRITE))
        self.assertFalse(user.can(Permission.COMMENT))

    def test_user_role(self):
        hash = generate_password_hash('qq')
        user=Users(email='tfgv60@gmail.com',psw=hash)
        self.assertFalse(user.can(Permission.ADMIN))
        self.assertFalse(user.can(Permission.MODERATE))
        self.assertFalse(user.can(Permission.FOLLOW))
        self.assertFalse(user.can(Permission.COMMENT))
        self.assertFalse(user.can(Permission.WRITE))

