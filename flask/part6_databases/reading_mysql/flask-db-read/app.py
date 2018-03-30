import pymysql
from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import SubmitField, SelectField
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SECRET_KEY'] = 'som$secrt*strng!here!'

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


# each table in the database needs a class to be created for it
# db.Model is required - don't change it
# this database has only ONE table, socks
# identify all of your columns by name and data type
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
# above: the class that maps the table structure to be used by SQLAlchemy
# for one table only - if you had more tables, you'd need a class for each one
# you can put classes in another file and import them


# Flask-WTF form magic
# set up the quickform - select includes value, option text (value matches db)
# all that is in this form is one select menu and one submit button
class SockForm(FlaskForm):
    select = SelectField('Choose a sock style:',
      choices=[ ('ankle', 'Ankle'),
      ('knee-high', 'Knee-high'),
      ('mini', 'Mini'),
      ('other', 'Other') ])
    submit = SubmitField('Submit')


# three routes: index, socklist, and sock

# starting page for app
@app.route('/', methods=['GET'])
def index():
    # make an instance of the WTF form class we created, above
    form = SockForm()
    # pass it to the template
    return render_template('index.html', form=form)

# this route is called by the form - see index.html template
@app.route('/list', methods=['POST'])
def socklist():
    # request was imported - line 4, this file -
    # form is the variable in the wtf.quick_form() - see index.html template -
    # 'select' is the name quick_form assigned
    # automatically to the select element - its value comes from the
    # attribute (value=) in the selected option
    style = request.form['select']
    # now we know which style was selected in the form
    # so we get all socks of _that_ style from the db with filter_by()
    # and sort the names alphabetically with order_by()
    socks = Sock.query.filter_by(style=style).order_by(Sock.name).all()
    # and we pass them to the template
    return render_template('list.html', style=style, socks=socks)

# whichever id is in the browser address bar, that one sock will be displayed
@app.route('/sock/<id>')
def sock(id):
    # get all columns for the one sock with the supplied id
    the_sock = Sock.query.filter_by(id=id).first_or_404()
    # pass them to the template
    return render_template('sock.html', the_sock=the_sock)


# error handlers

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(405)
def form_not_posted(e):
    return render_template('405.html'), 405

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500


# run the app
if __name__ == '__main__':
    app.run(debug=True)
