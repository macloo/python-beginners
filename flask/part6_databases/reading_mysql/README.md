# Reading from a MySQL database

The prerequisites for this tutorial are explained in the README in [part6_databases](part6_databases) in this repo. It's essential to get your database connection working without errors before you try doing more with the database and Flask.

The MySQL database used in this tutorial has only one table:

<img src="../images/mysql_table.png" alt="MySQL database table structure">

*MySQL database:* sockmarket *Structure for the table* socks *viewed in phpMyAdmin.*

We will thoroughly test the app locally before deploying it to a live server.

Let's examine the *app.py* file. The final app is [here](https://weimergeeks.com/flask_db2/). The code is all here in this repo in the *flask-db-read* folder.

## Imports

In addition to Flask, Flask-SQLAlchemy, and PyMySQL, we also import Flask-WTF for forms and Flask-Bootstrap for CSS styles.

```python
import pymysql
from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import SubmitField, SelectField
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SECRET_KEY'] = 'som$secrt*strng!here!'
```

The "secret key" is explained in the [Flask forms](../../part4_forms) section of this repo.

`from flask`: Your app might require additional modules to be imported from Flask.

`from wtforms` If you are using a form, you might be using different fields.

## The database connection

Most of this was explained in the README in [part6_databases](part6_databases) in this repo. Note that the username and password for the database will be different on a live web server.

```python
# connect to local database
userpass = 'mysql+pymysql://root:@'
basedir  = '127.0.0.1'
dbname   = '/sockmarket'
socket   = '?unix_socket=/Applications/XAMPP/xamppfiles/var/mysql/mysql.sock'
dbname   = dbname + socket

# setup required for SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = userpass + basedir + dbname

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)

# setup required for Bootstrap
bootstrap = Bootstrap(app)
```

## Configure the database model for SQLAlchemy

Each table in the database needs a Python class to be created for it. Name the class after the table. Starting with an uppercase letter and using camel case (not underscores) is Python style for classes. This database has only ONE table, *socks*.

This is called [Declaring Models](http://flask-sqlalchemy.pocoo.org/2.1/models/) in the Flask-SQLAlchemy documentation. Note that we’re doing it in the Flask-SQLAlchemy manner, which differs from the straight-up SQLAlchemy way.

The class inherits from `db.Model` (in SQLAlchemy), so don't change `db.Model`!

`__tablename__ = 'socks'`: Do not alter `__tablename__ =`; the right side value must exactly match the table name in your database.

Identify all of your columns by both name and data type. Make sure column names match exactly what you have in your database. Remember that Python is case-sensitive, so note where uppercase is used, and don't change it.

The **data types** (String, Integer, Float, etc.) must MATCH what you have in your database. Don’t guess. Look it up if you’re not sure. Note that you need to specify your Primary Key.

```python
class Sock(db.Model):
    __tablename__ = 'socks'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    style = db.Column(db.String)
    color = db.Column(db.String)
    quantity = db.Column(db.Integer)
    price = db.Column(db.Float)
    updated = db.Column(db.String)

    def __init__(self, name, style, color, quantity, price, updated):
        self.name = name
        self.style = style
        self.color = color
        self.quantity = quantity
        self.price = price
        self.updated = updated

    def __repr__(self):
        return '<Sock %s>' % self.name
```

That's the entire class for *one table*. If you're unfamiliar with classes in Python &mdash; `self` is required in all instances where you see it above; don't change or omit it.

Note the repetition of the column names in `def __init__()`.

`return '<Sock %s>' % self.name`: Replace *Sock* with whatever your class name is. If you don’t have `self.name` in your `def __init__()`, then substitute the title or other column heading from your table that best identifies an individual record in your database.

Compare to [this simple example](http://flask-sqlalchemy.pocoo.org/2.1/models/#simple-example).

## A Flask form

How to create forms with the Flask-WTF extension is explained in the [Flask forms](../../part4_forms) section of this repo.

Here we configure a small, simple form with only a select menu and a submit button. The select menu choices correspond to the *style* field in the database.

```python
class SockForm(FlaskForm):
    select = SelectField('Choose a sock style:',
      choices=[ ('ankle', 'Ankle'),
      ('knee-high', 'Knee-high'),
      ('mini', 'Mini'),
      ('other', 'Other') ])
    submit = SubmitField('Submit')
```

## The Flask routes

This app has three routes and three templates. In terms of how the local browser sees the routes, they are:

* localhost:5000/
* localhost:5000/list
* localhost:5000/sock/32

The number *32* would change depending on the id in the HTTP request.

```python
# starting page for app
@app.route('/', methods=['GET'])
def index():
    # make an instance of the WTF form class we created, above
    form = SockForm()
    # pass it to the template
    return render_template('index.html', form=form)
```

The first route does not use the database at all. When the form there is submitted, code in the template *index.html* calls the next route:

```html+jinja
{{ wtf.quick_form(form, action=url_for("socklist"), method="post") }}
```

Here's that second route:

```python
@app.route('/list', methods=['POST'])
def socklist():
    # 'select' is the name quick_form assigned automatically to
    # the select menu
    style = request.form['select']
    # now we know which style was selected in the form
    # here's a SQLAlchemy query -
    socks = Sock.query.filter_by(style=style).order_by(Sock.name).all()
    # and we pass the results to the template
    return render_template('list.html', style=style, socks=socks)
```

On the first page of the app, the user selects a *style* from the form. Submitting the form calls the route above, which passes that *style* in a SQL query to the database. The returned value, in the new variable *socks*, is passed to the template *list.html*, which generates a list of links to all the sock records that match that style.

Note that `Sock` is **the Python class** I made that represents the table (*socks*) in my MySQL database.

Here's the Flask-SQLAlchemy documentation for [querying the database](http://flask-sqlalchemy.pocoo.org/2.1/queries/#querying-records).

If the user clicks any link in the list of socks, the third route is called:

```python
@app.route('/sock/<id>')
def sock(id):
    # get all columns for the one sock with the supplied id
    # a SQLAlchemy query -
    the_sock = Sock.query.filter_by(id=id).first_or_404()
    # pass them to the template
    return render_template('sock.html', the_sock=the_sock)
```

This time, the database is queried for ONE record, which matches the id in the clicked link. A 404 (file not found) error results if for any reason no record exists with that id.
