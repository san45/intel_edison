from flask import Flask
app = Flask(__name__)
from flask import render_template


@app.route('/')
def home():
	
	return render_template('hello.html')

@app.route('/user1')
def user():
	return render_template('index.html')

@app.route('/user2')
def user2():
	return render_template('index2.html')

@app.route('/<useer>')
def mod():
	url=useer
	return render_template(url)


	
