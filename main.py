from flask import Flask, request, redirect, render_template
import cgi

app = Flask(__name__)

app.config['DEBUG'] = True

@app.route('/user-signup', methods=['POST'])
def user_signup():
    username = request.form['username']
    password = request.form['password']
    verify_pass = request.form['verify-pass']
    email = request.form['email']

    return

@app.route('/welcome')
def success():
    return render_template('welcome.html')

@app.route('/')
def index():
    error = request.args.get("error")
    return render_template('edit.html', error = error)


app.run()