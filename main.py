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

    if (not username) or (username.strip() == ''):
        username_error = "That's not a valid username"
        return redirect("/?error=" + cgi.escape(username_error, quote=True))
    else:
        if (len(username) < 3) or (len(username) > 20):
            error = "Username needs to be between 3 and 20 characters"
            return redirect("/?error=" + cgi.escape(error, quote=True))
        else:
            if (not password) or (password.strip()== ''):
                error = "Please enter a password"
                return redirect("/?error=" + cgi.escape(error, quote=True))
            else:
                if (len(password) < 3) or (len(password) > 20):
                    error = "Password needs to be between 3 and 20 characters"
                    return redirect("/?error=" + cgi.escape(error, quote=True))
                else:
                    if (password != verify_pass) or (not verify_pass):
                        error = "Password didn't verify"
                        return redirect("/?error=" + cgi.escape(error, quote=True))
                    else:
                
                
                        return redirect('/welcome')

@app.route('/welcome', methods=['POST'])
def success():
    username = request.form['username']
    return render_template('welcome.html')

@app.route('/')
def index():
    error = request.args.get("error")
    return render_template('edit.html', error = error)


app.run()