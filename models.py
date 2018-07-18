from flask import Flask, request, flash, url_for, redirect, render_template
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URI','sqlite:///students.sqlite3')
app.config['SECRET_KEY'] = "random string"

db = SQLAlchemy(app)

class Freelancer(db.Model):
    id = db.Column('freelancer_id', db.Integer, primary_key = True)
    firstname = db.Column(db.String(100))
    lastname = db.Column(db.String(50))
    image = db.Column(db.Blob(50))
    contact = db.Column(db.String(50))
    skills = db.Column(db.String(50))
    dob = db.Column(db.Date)
    status = db.Column(db.String(200))
    email = db.Column(db.String(200)) #to be changed to the propper fields
    password = db.Column(db.String(32)) #to be changed to the propper fields

    def __init__(self, firstname, lastname, contact, skills, dob, status, email, password):
        self.firstname = firstaname
        self.lastname = lastname
        self.contact = contact
        self.skills = skills
        self.dob = dob
        self.status = status
        self.email = email
        self.password = password
        
        
class Employer(db.Model):
    id = db.Column('employer_id', db.Integer, primary_key = True)
    companyname = db.Column(db.String(100))
    companydescription = db.Column(db.String(50))
    email = db.Column(db.String(200)) #to be changed to the propper fields
    contact = db.Column(db.String(32)) #to be changed to the propper fields

    def __init__(self, companyname, companydescription, email, contact):
        self.companyname = companyname
        self.companydescription = companydescription
        self.email = email
        self.contact = contact
        
class Job_postings(db.Model):
    id = db.Column('job_id', db.Integer, primary_key = True)
    amount = db.Column(db.Real)
    title = db.Column(db.String(100))
    description = db.Column(db.String(50))
    duration = db.Column(db.String(200)) #to be changed to the propper fields
    no_of_people = db.Column(db.Integer) #to be changed to the propper fields
    employer_id = db.Column(db.Integer, db.ForeignKey('employer.id'),
        nullable=False)
    emp = db.relationship('Employer',
        backref=db.backref('job_postings', lazy=True))


    def __init__(self, employer_id, amount, title, description, duration, no_of_people):
        self.employer_id = employer_id
        self.amount = amount
        self.title = title
        self.description = description
        self.duration = duration
        self.no_of_people = no_of_people
        
        
class Comments(db.Model):
    id = db.Column('comment_id', db.Integer, primary_key = True)
    employer_id = db.Column(db.Integer, db.ForeignKey('employer.id'),
        nullable=False)
    employ = db.relationship('Employer',
        backref=db.backref('comments', lazy=True))
    freelancer_id = db.Column(db.Integer, db.ForeignKey('freelancer.id'),
        nullable=False)
    free = db.relationship('Freelancer',
        backref=db.backref('comments', lazy=True))
    rating = db.Column(db.Integer)
    comment = db.Column(db.String(100))
    doc = db.Column(db.DateTime)
    toc = db.Column(db.DateTime) #to be changed to the propper fields
   

    def __init__(self, employer_id, freelancer_id, rating, comment, doc, toc):
        self.employer_id = employer_id
        self.freelancer_id = freelancer_id
        self.rating = rating
        self.comment = comment
        self.doc = doc
        self.toc = toc
        
class Job_allocation(db.Model):
    id = db.Column('id', db.Integer, primary_key = True)
     employer_id = db.Column(db.Integer, db.ForeignKey('employer.id'),
        nullable=False)
     emp = db.relationship('Employer',
        backref=db.backref('job_allocation', lazy=True))
     freelancer_id = db.Column(db.Integer, db.ForeignKey('freelancer.id'),
        nullable=False)
     freelancer = db.relationship('Freelancer',
        backref=db.backref('job_allocation', lazy=True))
   

    def __init__(self, job_id, freelancer_id, employer_id):
		self.job_id = job_id
        self.freelancer_id = freelancer_id
        self.employer_id = employer_id
        
        


  
