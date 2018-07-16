from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>it worked</h1>"

if __name__=='__main__':
    import os
    app.run(host='0.0.0.0', debug=True, port=os.environ.get('PORT',8000))
    
