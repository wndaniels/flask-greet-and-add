from flask import Flask

app = Flask(__name__)


@app.route('/welcome')
def welcome_page():
    return "Welcome"


@app.route('/welcome/home')
def home_page():
    return "Welcome Home"


@app.route('/welcome/back')
def back_page():
    return "Welcome Back"
