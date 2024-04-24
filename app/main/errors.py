from flask import render_template

from . import main


@main.route('/error')
def error():
    return render_template('error.html'), 403


@main.app_errorhandler(404)
def page_not_found(e):
    return render_template("error.html"), 404
