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
    verify_error = ''

    #Validates username and if username error, clears it
    if (not username) or (username.strip() == '') or ((len(username) > 20 or len(username) < 3)) or (' ' in username):
        username_error = "That's not a valid username"
        username = ''
    
    #Validates password
    if (not password) or (password.strip() == '') or ((len(password) > 20 or len(password) < 3)) or (' ' in password):
            password_error = "That's not a valid password"

    #Password verification
    if (password != verify_pass) or (not verify_pass):
        verify_error = "Passwords don't match"

    #Email check
    if email == '':
        email = ''
    else:
        x = '.'
        y = '@'
        if ('@' and '.') not in email or (' ' in email) or (email.count(x) > 1) or (email.count(y) > 1) or (len(email) > 20) or (len(email) < 3):
            email_error = "That's not a valid email"
            email = ''
    
    if (not username_error) and (not password_error) and (not verify_error) and (not email_error):        
        return redirect('/welcome?username={0}'.format(username))
    else:
        #Renders the error page
        return render_template('edit.html', username_error = username_error, 
            password_error = password_error, verify_error = verify_error,
            email_error = email_error, username = username, email = email)    


@app.route('/welcome')
def success():
    username = request.args.get('username')
    return render_template('welcome.html', username = username)

@app.route('/')
def index():
    return render_template('edit.html')


app.run()