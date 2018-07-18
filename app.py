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
        user = db.session.query(models.Freelancer).filter_by(email=request.form['email']).first()
        if user.password == request.form['password']:
            flash('logged in as {}'.format(user.firstname))
            return redirect(url_for('jobs_index'))
        else:
    	    flash('Failed to login')
        
    return render_template('login.html', form=form)


@app.route('/signup', methods = ['GET', 'POST'])
def signup():
    form = SignUpForm()
    if request.method == 'POST' and form.validate_on_submit():
        user = models.Freelancer(request.form['firstname'],
            request.form['lastname'],
            request.form['contact'],
            request.form['skills'],
            request.form['dob'],
            request.form['status'],
            request.form['email'],
            request.form['password'],
            )
        db.session.add(user)
        db.session.commit()
        flash('successfully logged in')
        return redirect(url_for('jobs_index'))
    return render_template('signup.html', form=form)


@app.route('/jobs')
def jobs_index():
	job_list = user = db.session.query(models.Job_postings).all()
	return render_template('jobindex.html', job_list=job_list)

@app.route('/jobs/<job_id>')
def job_detail(job_id):
	job = user = db.session.query(models.Job_postings).filter_by(id=job_id).first()
	return render_template('job_detail.html', job=job)

@app.route('/jobs/new', methods = ['GET', 'POST'])
def new_job():
    form = JobPostForm()
    if request.method == 'POST' and form.validate_on_submit():
        user = models.Job_postings(request.form['firstname'],#employer_id
            request.form['lastname'],
            request.form['contact'],
            request.form['skills'],
            request.form['dob'],
            request.form['status'],
            request.form['email'],
            request.form['password'],
            )
        db.session.add(user)
        db.session.commit()
        flash('successfully logged in')
        return redirect(url_for('jobs_index'))
    return render_template('signup.html', form=form)


@app.route('/about')
def about():
    return redirect('/home#about')


@app.route('/')
@app.route('/home')
def index():
    return render_template('index.html')




if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT',5000)))
