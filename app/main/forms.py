from wtforms.validators import DataRequired, Email, EqualTo, Length
from flask_wtf import FlaskForm
from wtforms import *


class ContactForm(FlaskForm):
    name = StringField("Nickname: ",
                       validators=[Length(min=2, max=30, message="The name must be between 2 and 30 characters long")])
    email = StringField("Email: ", validators=[Email("Invalid email")])
    city = StringField("City: ",
                       validators=[Length(min=2, max=30, message="The city must be between 2 and 30 characters long")])
    psw = PasswordField("Password: ", validators=[DataRequired(), Length(min=2, max=30,
                                                                         message="The password must be between 4 and 30 characters long")])
    psw2 = PasswordField("Confirm password: ",validators=[DataRequired(), EqualTo('psw', message="Passwords don't match")])
    submit = SubmitField("Registration!")