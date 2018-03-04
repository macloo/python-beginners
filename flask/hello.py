# to run this, type at bash prompt:
# FLASK_APP=hello.py flask run

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"
