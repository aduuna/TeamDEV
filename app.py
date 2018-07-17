from flask import Flask, request, flash, url_for, redirect, render_template
from flask_sqlalchemy import SQLAlchemy
import os

#forms imports
from forms import SignUpForm, LoginForm, CommentForm
from passlib.hash import sha256_crypt

#configurations
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URI','sqlite:///app.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = "random string"

db = SQLAlchemy(app)

import models



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
        user = Freelancer(request.form['firstname'],
            request.form['lastname'],
            request.form['status'],
            request.form['email'],
            request.form['password'])
        db.session.add(user)
        db.session.commit()
        flash('successfully logged in')
        return redirect(url_for('jobs_index'))
    return render_template('signup.html', form=form)


@app.route('/jobs')
def jobs_index():
	job_list = [
		{
			'amount':500,
			'title':'Tonaton manager',
			'description':'become the first and ever manager of tonaton Ghana limited',
			'duration':'8 weeks',
			'no_of_people':2
		},
		{
			'amount':500,
			'title':'Adowa dancer',
			'description':'Dance for the fan of it',
			'duration':'40 years',
			'no_of_people':1000000
		},
		{
			'amount':500,
			'title':'Adowa dancer',
			'description':'Dance for the fan of it',
			'duration':'40 years',
			'no_of_people':1000000
		},
		{
			'amount':500,
			'title':'Adowa dancer',
			'description':'Dance for the fan of it',
			'duration':'40 years',
			'no_of_people':1000000
		},
	
	]
	return render_template('jobindex.html', job_list=job_list)


@app.route('/')
def show_all():
    return render_template('index.html')

"""
@app.route('/home')
def home():
    out = get_users()
    return "Home page"
	
                    
@app.route('/signup')
def signup():
    return "Sign up page"

                    
@app.route('/login')
def login():
    return "Login page"	

                    
@app.route('/about')
def about():
    return "About page"
"""	



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT',5000)))
