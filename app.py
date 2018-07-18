from flask import Flask, request, flash, url_for, redirect, render_template
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URI','sqlite:///students.sqlite3')
app.config['SECRET_KEY'] = "random string"

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column('student_id', db.Integer, primary_key = True)
    firstname = db.Column(db.String(100))
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

@app.route('/')
def show_all():
    return render_template('index.html')

@app.route('/new', methods = ['GET', 'POST'])
def new():
    if request.method == 'POST':
        if not request.form['name'] or not request.form['city'] or not request.form['addr']:
            flash('Please enter all the fields', 'error')
        else:
            user = User(request.form['name'], request.form['city'],
            request.form['addr'], request.form['pin'])

            db.session.add(user)
            db.session.commit()
            flash('Record was successfully added')
            return redirect(url_for('show_all'))
		
    return render_template('new.html')

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT',5000)))
