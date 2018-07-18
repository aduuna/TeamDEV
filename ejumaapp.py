from flask import Flask
import urllib.parse as urlparse
import psycopg2
import os
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/users')
def get_users():
    conn = ""
    out = []
    try:
        url = urlparse.urlparse(os.environ['DATABASE_URL'])
        dbname = url.path[1:]
        user = url.username
        password = url.password
        host = url.hostname
        port = url.port
        conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host, port=port)
    except:
        out = {"err": "Unable to connect to the database"}
    try:
        cur = conn.cursor()
        cur.execute("""SELECT * FROM freelancer""")
        rows = cur.fetchall()
        out = []
        for row in rows:
            out.append({"freelancer_id": row[0], "first_name": row[1]})
    except:
        out = {"err": "General SQL Error"}
        
            
@app.route('/')
def index():
    return render_template("index.html", rows=out)
   

if __name__=='__main__':
   
    app.run(host='0.0.0.0', debug=True, port=int(os.environ.get('PORT',8000)))
    
