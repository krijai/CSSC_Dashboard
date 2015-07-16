from flask import Flask,render_template,request
import sys, os

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('layout.html') #Main Page
@app.route('/radio', methods=['GET','POST'])
def rad():
	x= 'rogerr'
	return render_template('layout.html',roger=x)