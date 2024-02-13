from flask import Flask, request
import psycopg2

# Create a Flask app
app = Flask(__name__)

# Connect to the database using psycopg2 library and the database credentials
conn = psycopg2.connect(database="flask_db", user="postgres", 
						password="root", host="localhost", port="5432") 

# create a cursor 
cur = conn.cursor() 

# if you already have any table or not id doesnt matter this 
# will create a products table for you. 
cur.execute( 
	'''CREATE TABLE if not exists users (id SERIAL PRIMARY KEY,username VARCHAR(50) UNIQUE NOT NULL, email VARCHAR(120) UNIQUE NOT NULL);''') 

# commit the changes 
conn.commit() 

# close the cursor and connection 
cur.close() 
# conn.close() 
# Root route


@app.route('/', methods=['GET'])
def hello_world():
	return 'Hello, World!'


@app.route('/create', methods=['POST'])
def create():
	# Get the username and email from the request body
	username = request.form.get('username')
	email = request.form.get('email')

	# Insert the data into the database
	cur = conn.cursor()
	cur.execute(
		"INSERT INTO users (username, email) VALUES (%s, %s)", (username, email))
	conn.commit()

	return 'User created successfully!'

if __name__ == '__main__': 
	app.run(debug=True) 

