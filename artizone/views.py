from flask import *

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/login')
def login():
	return render_template('views/login.html')

@app.route('/inscription')
def inscription():
	return render_template('views/inscription.html')

@app.route('/erreurs/forgot_password')
def forgot_password():
	return render_template('views/erreurs/forgot_password.html')

if __name__ == '__main__':
	app.run()
