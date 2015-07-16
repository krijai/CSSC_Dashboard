#!/usr/bin/python
# -*- coding: latin-1 -*-
from flask import Flask,render_template, request
import psycopg2
from functools import partial
import pandas as pd
import numpy as np
from pandas import *
from xlrd import *
import os.path
import shutil
from decimal import Decimal


app = Flask(__name__)
@app.route('/', methods=['GET','POST'])
def value():
	return render_template('layout.html')

@app.route('/connect',methods=['GET','POST'])
def index():
	conn_string = "dbname='deaup6nh066ma2' user='xibtwlbzmsbctw' password='PDfZm6nQ2bHXjNNPwrnEKFQGoa' host='ec2-54-217-202-110.eu-west-1.compute.amazonaws.com' port='5432'"
	connection = psycopg2.connect(conn_string)
	cursor = connection.cursor()
	if request.method=='POST':
		dateval2 = request.form['datepick']
		dateval = dateval2.encode('utf-8')
	else:
		dateval2 = request.form['datepick']
		dateval = dateval2.encode('utf-8')
	result = "SELECT * FROM O where Time_IST=%s"
	df = pd.read_sql_query(result,connection,params=(dateval,))
	#Count(dateval)
	if df.empty:
		table = pandas.DataFrame({'No Data Available': ['']})
	else:
		table = pivot_table(df, values=["document"], index=["name"],columns=["tat"], aggfunc=lambda x: len(x), margins=True, dropna=True)
		
if __name__ == "__main__":

	app.run(debug=True)

