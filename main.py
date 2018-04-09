from flask import Flask, request, redirect, render_template
import cgi

app = Flask(__name__)

app.config['DEBUG'] = True


@app.route('/error', methods=['POST'])
def validate():
    username = request.form['username']
    password = request.form['password']
    verify_pass = request.form['verify-pass']
    email = request.form['email']

    username_error = ''
    password_error = ''
    email_error = ''
    verify_error = ''


    if (not username) or (username.strip() == '') or ((len(username) > 20 or len(username) < 3)) or (' ' in username):
        username_error = "That's not a valid username"

    if (not password) or (password.strip() == '') or ((len(password) > 20 or len(password) < 3)) or (' ' in password):
            password_error = "That's not a valid password"

    if (password != verify_pass) or (not verify_pass):
        verify_error = "Passwords don't match"

    if email == '':
        email = ''
    else:
        if ('@' and '.') not in email:
            email_error = "That's not a valid email"
    
    if (not username_error) and (not password_error) and (not verify_error) and (not email_error):        
        return redirect('/welcome')
    else:
        return render_template('edit.html', username_error = username_error, 
            password_error = password_error, verify_error = verify_error,
            email_error = email_error)    


@app.route('/welcome', methods=['POST'])
def success():
    return render_template('welcome.html')

@app.route('/')
def index():
    return render_template('edit.html')


app.run()