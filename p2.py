#!/usr/bin/python
# -*- coding: latin-1 -*-
from flask import Flask,render_template, request
import pyodbc
from functools import partial
import pandas as pd
import numpy as np
from pandas import *
from xlrd import *
import os.path
import shutil
from decimal import Decimal
from p3 import *

app = Flask(__name__)
@app.route('/', methods=['GET','POST'])
def value():
	return render_template('layout.html')

@app.route('/P',methods=['GET','POST'])
def index():
	connection = pyodbc.connect('Driver={SQL Server};Server=INQ69NBOCBPWMV1;Database=Test;Trusted_Connection=yes;')
	cursor = connection.cursor()
	if request.method=='POST':
		dateval2 = request.form['datepick']
		dateval = dateval2.encode('utf-8')
	else:
		dateval2 = request.form['datepick']
		dateval = dateval2.encode('utf-8')
	result = "SELECT * FROM OE_TAT where convert(date,Time_IST)=?"
	df = pd.read_sql_query(result,connection, params=(dateval,))
	Count(dateval)
	if df.empty:
		table = pandas.DataFrame({'No Data Available': ['']})
	else:
		table = pivot_table(df, values=["Document"], index=["Name"],columns=["TAT"], aggfunc=lambda x: len(x), margins=True, dropna=True)
		#table = pd.crosstab(df.Name,df.TAT).apply(lambda r: r/len(table), axis=1)
		#table = table.apply(lambda x : x / x.len(), axis='index')
		table = table.rename(columns = {'All':'Total'})
		table = table.rename(index = {'All':'Total'})
		table = table.div(table.Document["Total"], axis='index')
		table = 100*np.round(table, 4)
		table = table.fillna('')	
	dir = 'C:\\Users\\TE236863\\Desktop\\proj\\templates\\my_file.html'
	if os.path.isfile(dir):
		os.remove('C:\\Users\\TE236863\\Desktop\\proj\\templates\\my_file.html')
		
		Data = table.to_html(open('C:\\Users\\TE236863\\Desktop\\proj\\templates\\my_file.html', 'w'))
	else:
		
		Data = table.to_html(open('C:\\Users\\TE236863\\Desktop\\proj\\templates\\my_file.html', 'w'))
	os.chdir("C:\\Users\\TE236863\\Desktop\\proj\\templates")
	
	with open("ph1.html") as index:
		index_text = index.read()
	with open("my_file.html") as menu:
		menu_text = menu.read()
		# I called it index2 so it doesn't overwrite... you can change that
	with open("my_file2.html") as menu2:
		menu_text2 = menu2.read()	
	with open("index2.html", "w") as index2:
		index2.write(index_text.replace('<!-- Insert Menu here -->', menu_text))
	with open("index2.html") as index3:
		index_text2 = index3.read()
	with open("index2.html", "w") as index2:	
		index2.write(index_text2.replace('<!-- EOD Count -->', menu_text2))	
	return render_template('index2.html')
if __name__ == "__main__":
	app.run(debug=True)