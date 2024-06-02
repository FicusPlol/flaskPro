from wtforms.validators import DataRequired, Email, EqualTo, Length
from flask_wtf import FlaskForm
from wtforms import *


class ContactForm(FlaskForm):
    name = StringField("Name",
                       validators=[Length(min=2, max=30, message="The name must be between 2 and 30 characters long")])

    city = StringField("City",
                       validators=[Length(min=2, max=30, message="The city must be between 2 and 30 characters long")])
    email = StringField("Email", validators=[Email("Invalid email")])
    psw = PasswordField("Password", validators=[DataRequired(), Length(min=2, max=30,
                                                                       message="The password must be between 4 and 30 characters long")])
    submit = SubmitField("Register now")


class LoginForm(FlaskForm):
    email = StringField("Email", validators=[Email("Invalid email")])
    psw = PasswordField("Password", validators=[DataRequired(), Length(min=2, max=30,
                                                                       message="The password must be between 4 and 30 characters long")])
