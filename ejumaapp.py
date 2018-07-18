from flask import Flask
import urllib.parse as urlparse
import psycopg2
import os
from flask import Flask, render_template


app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
db = SQLAlchemy(app)

from models import Job

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
    return out
                    
@app.route('/')
def index():
    out = get_users()
    return render_template("home.html", rows=out)
   

if __name__=='__main__':
    import os
    app.run(host='0.0.0.0', debug=True, port=int(os.environ.get('PORT',8000)))

