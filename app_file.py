import unittest
from app import create_app, db
from app.models import Users, Profiles

app = create_app('default')
import os
'''
@app.shell_context_processors
def make_shell():
    return dict(db=db, Users=Users, Profiles=Profiles)

'''


@app.cli.command('test')
def test():
    """yyyy"""
    tests = unittest.TestLoader().discover('tests')  # test
    unittest.TextTestRunner(verbosity=2).run(tests)


'''
old 

from app import app

if __name__ == "__main__":
    app.run(debug=True)'''
