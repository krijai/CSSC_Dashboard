from flask import Flask,render_template,request
import sys, os
import psycopg2
import urlparse
app = Flask(__name__)

@app.route("/")
def hello():
	DATABASES = {'default': database_url.config(default='postgres://xibtwlbzmsbctw:PDfZm6nQ2bHXjNNPwrnEKFQGoa@localhost/deaup6nh066ma2')}
	return render_template('layout.html') #Main Page
@app.route('/radio', methods=['GET','POST'])
def rad():
	x= 'ec2-54-217-202-110.eu-west-1.compute.amazonaws.com'
	y='5432'
	urlparse.uses_netloc.append("postgres")
	url = urlparse.urlparse(os.environ["DATABASE_URL"])
	conn = psycopg2.connect(
    database=url.path[1:],#deaup6nh066ma2,
    user=url.username, #xibtwlbzmsbctw,
    password=url.password, #PDfZm6nQ2bHXjNNPwrnEKFQGoa
    host=url.hostname,
    port=url.port
)

	cursor = conn.cursor()
	return render_template('layout.html')
	#conn_string = "host='ec2-54-217-202-110.eu-west-1.compute.amazonaws.com' dbname='deaup6nh066ma2' user='xibtwlbzmsbctw' password='PDfZm6nQ2bHXjNNPwrnEKFQGoa'"
	# print the connection string we will use to connect
	#print "Connecting to database\n	->%s" % (conn_string)
 
	# get a connection, if a connect cannot be made an exception will be raised here
	#conn = psycopg2.connect(conn_string)
 
	# conn.cursor will return a cursor object, you can use this cursor to perform queries
	#cursor = conn.cursor()
 
	# execute our Query
	#cursor.execute("SELECT * FROM my_table")
 
	# retrieve the records from the database
	#records = cursor.fetchall()
 
	# print out the records using pretty print
	# note that the NAMES of the columns are not shown, instead just indexes.
	# for most people this isn't very useful so we'll show you how to return
	# columns as a dictionary (hash) in the next example.
	#pprint.pprint(records)
 
if __name__ == "__main__":
	app.run(debug=True)