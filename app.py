from flask import Flask, render_template, request;

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/register', methods=['GET','POST'])
def register():
    if request.method == 'POST':

        username = request.form.get('login')
        password = request.form.get('password')
        
        print("POST REQUEST WITH: "+str(username)+" "+str(password))
        return f"Successfully registered user {username} with password: {password}"
    
    # If it's a GET request, render the registration form
    return "TO JE GET REQUEST WE NO"