"""
test for a MySQL database connection on your hosted website
code below works for a MySQL database in phpMyAdmin on Reclaim Hosting
"""

import pymysql
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# the next line is necessary with cPanel deployment
application = app

# make sure you get the username, password and databasename right
# note colon : and "at" sign @ in userpass - keep them
userpass = 'mysql+pymysql://username:password@'
basedir  = '127.0.0.1'
# keep the slash /
dbname   = '/databasename'

# change NOTHING below

# put them all together as a string that shows SQLAlchemy where the database is
app.config['SQLALCHEMY_DATABASE_URI'] = userpass + basedir + dbname

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

# this variable, db, will be used for all SQLAlchemy commands
db = SQLAlchemy(app)

# NOTHING BELOW THIS LINE NEEDS TO CHANGE
# this route will test the database connection and nothing more
@app.route('/')
def testdb():
    try:
        db.session.query('1').from_statement('SELECT 1').all()
        return '<h1>It works.</h1>'
    except Exception as e:
        # see Terminal for description of the error
        print("\nThe error:\n" + str(e) + "\n")
        return '<h1>Something is broken.</h1>'

if __name__ == '__main__':
    app.run(debug=True)
