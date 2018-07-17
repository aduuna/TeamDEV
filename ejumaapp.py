from flask import Flask, render_template
from flask.ext.sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
db = SQLAlchemy(app)

from models import Job

@app.route('/')
def index():
    return "<h1>it worked</h1>"

if __name__=='__main__':
    import os
    app.run(host='0.0.0.0', debug=True, port=int(os.environ.get('PORT',8000))) 
