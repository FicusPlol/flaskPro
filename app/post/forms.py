from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed
from wtforms import *
from wtforms.validators import DataRequired


class PostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    content = TextAreaField('Article', validators=[DataRequired()])
    picture = FileField('Picture (png,jpg)')
    submit = SubmitField('Submit')


class PostUpdateForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    content = TextAreaField('Article', validators=[DataRequired()])
    picture = FileField('Picture (png,jpg)', validators=[FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Submit')
