from flask import Flask, request, redirect, render_template
import cgi

app = Flask(__name__)

app.config['DEBUG'] = True

@app.route('/user-signup', methods=['POST'])
def validate():
    username = request.form['username']
    password = request.form['password']
    verify_pass = request.form['verify-pass']
    email = request.form['email']

    username_error = ''
    password_error = ''
    email_error = ''

    if (not username) or (username.strip() == '') or ((len(username) > 20 or len(username) < 3)):
        username_error = "That's not a valid username"

    if (not password) or (password.strip() == '') or ((len(password) > 20 or len(password) < 3)):
            password_error = "That's not a valid password"
    
    if (not username_error) and (not password_error):        
        return redirect('/welcome')
    else:
        return render_template('edit.html', username_error = username_error, password_error = password_error)    

@app.route('/welcome', methods=['POST'])
def success():
    username = request.form['username']
    return render_template('welcome.html')

@app.route('/')
def index():
    error = request.args.get("username_error")
    return render_template('edit.html', username_error = error)


app.run()