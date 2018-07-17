from flask import Flask, request, flash, url_for, redirect, render_template
from flask_sqlalchemy import SQLAlchemy
import os

#forms imports
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, PasswordField
from wtforms.validators import DataRequired,Length, EqualTo
from passlib.hash import sha256_crypt

#configurations
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URI','sqlite:///students.sqlite3')
app.config['SECRET_KEY'] = "random string"

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column('student_id', db.Integer, primary_key = True)
    firstname = db.Column(db.String(50))
    lastname = db.Column(db.String(50))
    status = db.Column(db.String(200))
    email = db.Column(db.String(200)) #to be changed to the propper fields
    password = db.Column(db.String(32)) #to be changed to the propper fields

    def __init__(self, name, city, addr,pin):
        self.firstname = firstaname
        self.lastname = lastname
        self.status = status
        self.email = email
        self.password = password
        
#Forms
class LoginForm(FlaskForm):
    username = StringField('username', validators=[DataRequired(), Length(min=1, max=50)])
    password = PasswordField('password', validators=[DataRequired()])
    
class SignUpForm(FlaskForm):
    firstname = StringField('first name', validators=[DataRequired(), Length(min=1, max=50)])
    lastname = StringField('last name', validators=[DataRequired(), Length(min=1, max=50)])
    username = StringField('user name', validators=[DataRequired(), Length(min=1, max=50)])
    email = StringField('email', validators=[DataRequired(), Length(min=6, max=100)])
    password = PasswordField('password', validators=[DataRequired(), EqualTo('confirm', message='passwords should match')])
    confirm = PasswordField('confirm password')

@app.route('/login', methods=('GET', 'POST'))
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect('/')
    return render_template('login.html', form=form)


@app.route('/signup', methods = ['GET', 'POST'])
def signup():
    form = SignUpForm()
    if request.method == 'POST' and form.validated():
        user = User(request.form['firstname'],
            request.form['lastname'],
            request.form['status'],
            request.form['email'],
            request.form['password'])
        db.session.add(user)
        db.session.commit()
        flash('Record was successfully added')
        return redirect(url_for('show_all'))
    return render_template('signup.html', form=form)


@app.route('/')
def show_all():
    return render_template('index.html')



if __name__ == '__main__':
    db.create_all()
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT',5000)))
