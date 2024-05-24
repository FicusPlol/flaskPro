import unittest

from app.models import Users, Profiles

from flask_migrate import Migrate

from app import create_app, db

app = create_app('default')
app1 = app
app1.run(debug=True)


@app.cli.command('test')
def test():
    tests = unittest.TestLoader().discover('tests')  # test
    unittest.TextTestRunner(verbosity=2).run(tests)


import os

'''
alex tfgv tfgv60@gmail.com qq
anita rambler124413@gmail.com 11
lola lola lola@gmail.com 12
'''

'''app.run(debug=True)
@app.shell_context_processors
def make_shell():
    return dict(db=db, Users=Users, Profiles=Profiles)
    '''

'''
old 

from app import app

if __name__ == "__main__":
    app.run(debug=True)'''
