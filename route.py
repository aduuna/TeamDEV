               
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
	