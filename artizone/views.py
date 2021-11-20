"""Script to run flask webserver for routing views."""
from flask import Flask, render_template, request
from .models.models import *


app = Flask(__name__)


@app.route('/')
def index():
    """Route to the index."""
    return render_template('index.html')


@app.route('/login')
def login():
    """Route to go to login page."""
    return render_template('views/login.html')


@app.route('/authentifier')
def authentifier():
    """S'authentifier pour l'artisant."""
    auth = Login()
    donnees = (request.form['identifiant'], request.form['identifiant'], request.form['password'])
    data = auth.get_info_artisant(donnees)
    if data[0] == '1' and data[1] != "":
        return data[0]


@app.route('/inscription')
def inscription():
    """Route to go to register page."""
    return render_template('views/inscription.html')


@app.route('/forgot_password')
def forgot_password():
    """Route to go to forgoten page."""
    return render_template('views/erreurs/forgot_password.html')


if __name__ == '__main__':
    app.run()
