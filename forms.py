from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, PasswordField
from wtforms.validators import DataRequired,Length, EqualTo

#Forms
class LoginForm(FlaskForm):
    email = StringField('email', validators=[DataRequired(), Length(min=6, max=100)])
    password = PasswordField('password', validators=[DataRequired()])
    
class SignUpForm(FlaskForm):
    firstname = StringField('first name', validators=[DataRequired(), Length(min=1, max=50)])
    lastname = StringField('last name', validators=[DataRequired(), Length(min=1, max=50)])
    email = StringField('email', validators=[DataRequired(), Length(min=6, max=100)])
    password = PasswordField('password', validators=[DataRequired(), EqualTo('confirm', message='passwords should match')])
    confirm = PasswordField('confirm password')


class CommentForm(FlaskForm):
	text = TextAreaField('comment', [Length(min=1, max=50)])
