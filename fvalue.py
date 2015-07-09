from flask import Flask,render_template, request
import pyodbc
import os,sys
app = Flask(__name__)
@app.route('/')
def index():
	return render_template('home.html')
@app.route('/fvalue', methods=['GET','POST'])
def formval():
	connection = pyodbc.connect('Driver={SQL Server};Server=INQ69NBOCBPWMV1;Database=Test;Trusted_Connection=yes;')
	cursor = connection.cursor()
	if request.method == 'POST':
		x = request.form['weekno']
		cursor.execute("SELECT Document FROM Backlog where Cust Req Ship Date=?",x)
		result = cursor.fetchall()
		return render_template('home.html',weekno=result)
if __name__ == "__main__":
	app.run(debug=True)