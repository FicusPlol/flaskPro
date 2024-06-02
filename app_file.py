import unittest
from app import create_app, db

app = create_app('default')
app1 = app
app1.run(debug=True)


@app.cli.command('test')
def test():
    tests = unittest.TestLoader().discover('tests')  # test
    unittest.TextTestRunner(verbosity=2).run(tests)


'''
alex tfgv tfgv60@gmail.com qq
anita rambler124413@gmail.com 11
lola lola lola@gmail.com 12
'''
