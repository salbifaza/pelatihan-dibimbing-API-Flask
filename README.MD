
command:
- docker exec -it postgresql-postgres-api-1 psql -U postgres

- python3 -m venv venv

# Activate virtual Environment
- .\venv\Scripts\activate # for Windows
- source venv/bin/activate # for Linux

# Install package
- pip install Flask psycopg2-binary

# create a database named flask_db
CREATE DATABASE flask_db;

# jalankan app.py
- buka postman set ke 127.0.0.1:5000/create
- pilih body -> form-data

reference :
- https://flask.palletsprojects.com/en/3.0.x/

- https://www.geeksforgeeks.org/python-introduction-to-web-development-using-flask/

- https://www.geeksforgeeks.org/sending-data-from-a-flask-app-to-postgresql-database/

- https://www.geeksforgeeks.org/making-a-flask-app-using-a-postgresql-database/



tes

# created a user demouser with password 12345678
CREATE USER demouser WITH PASSWORD '12345678';

# configured client encoding to utf8
ALTER ROLE demouser SET client_encoding TO 'utf8';
ALTER ROLE demouser SET default_transaction_isolation TO 'read committed';
ALTER ROLE demouser SET timezone TO 'UTC';

# grant all required privileges to demouser over demo db
GRANT ALL PRIVILEGES ON DATABASE demo TO demouser; 
