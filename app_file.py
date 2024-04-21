from app.models import Users, Profiles


from flask_migrate import Migrate

from app import create_app, db


app = create_app('default')

app.run(debug=True)
import os
'''
@app.shell_context_processors
def make_shell():
    return dict(db=db, Users=Users, Profiles=Profiles)

'''


@app.cli.command('test')
def test():
    tests = unittest.TestLoader().discover('tests')  # test
    unittest.TextTestRunner(verbosity=2).run(tests)


'''
old 

from app import app

if __name__ == "__main__":
    app.run(debug=True)'''
