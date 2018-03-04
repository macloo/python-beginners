# Part 2: Baby Steps with Flask

You've seen a very, very simple Flask app in the [Flask introduction](https://github.com/macloo/python-beginners/tree/master/flask). Let's step it up a little.

Here is your second small Flask app:

```python
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    greet = '<h1>Hello, Gators!</h1>'
    link = '<p><a href="user/Albert">Click me!</a></p>'
    return greet + link

@app.route('/user/<name>')
def user(name):
    # the curly braces {} are a placeholder for the value in
    # parentheses, in format()
    personal = '<h1>Hello, {}!</h1>'.format(name)
    return personal

if __name__ == '__main__':
    app.run(debug=True)
```

Now we have **two routes,** not one. The first route, for `'/'`, is not very different from our first Flask app. The second route, for `'/user/<name>'`, is doing something new.

1. Copy this code into a new file named `hello2.py` and run it at the bash (`$`) prompt with:

   ```bash
   python hello2.py
   ```

   **Note:** Because of the final two lines in this script, we do not need the longer command we ran in in the introduction. Now you're running this file in exactly the same way you've run every other `.py` file, in your *virtualenv.*

2. In your browser, type `localhost:5000` into the address bar. Press Return/Enter, and the app runs.

This script demonstrates the following:

* The URL in the browser causes a Python function to run. Remember, the *path* is specified in the decorator &mdash; `@app.route('/')`. The function *immediately after* the decorator (`hello()`) is called when that path is requested from the server.
* Clicking the link written in the `hello()` function opens the URL specified in `@app.route('/user/<name>')`: `localhost:5000/user/Albert`
* The path can have a dynamic component &mdash; in this case, `<name>`. The function after `@app.route('/user/<name>')` takes the *value* of `name` from the HTTP request (the path sent to the server) and uses that value in the function.
* The string `"Albert"` from the URL is used in the function `user()` to write dynamically in the browser window. Note that `<name>` in the **route** matches `name` in the function; that is necessary for it to work.
* You can change the `name` value in the browser's address bar, refresh/reload, and the contents of the window will change accordingly. Try it!

This example doesn't have an immediate practical use, but just wait for [part3](https://github.com/macloo/python-beginners/tree/master/flask/part3).

## About routes

Here are three examples of routes with their matching URLs on `localhost` and on a live server:

* `@app.route('/')` <br>
   localhost:5000/ <br>
   mydomain.com/

* `@app.route('/sports')` <br>
   localhost:5000/sports <br>
   mydomain.com/sports

* `@app.route('/students/<id>')` <br>
  localhost:5000/students/9876-4321 <br>
  mydomain.com/students/9876-4321 <br>
  (Note that `9876-4321` would likely be passed in by a user's action, e.g. she selected that ID from a drop-down menu.)

The path or URL shown for `localhost` or the live server does not open a web page; it causes the associated Python function to be executed.

## Running your Flask apps

In most cases, the last lines in your Flask app script will be:

```python
if __name__ == '__main__':
    app.run(debug=True)
```

This enables you to launch Flask's built-in server and run the app simply by typing `python filename.py` at the bash (`$`) prompt in Terminal.

* `if __name__ == '__main__':` <br>
   This returns `True` when the program (the file) is being *run by itself,* and was not imported. The double-underscore entities are specific pre-defined variables in Python, as explained in the [Flask introduction](https://github.com/macloo/python-beginners/tree/master/flask).

* `app.run()` <br>
  `app` is the Flask application object you created with `app = Flask(__name__)`. It has all the methods and attributes of the *Flask* class, and one of those is `run()`.

* `debug=True` is very useful when you're developing, because with it, any errors that occur will be written out in the browser.

## String formatters in Python

This might be the first time you have seen a string formatter used.

```python
personal = '<h1>Hello, {}!</h1>'.format(name)
```

This has nothing to do with Flask; it's just a normal part of Python3. It's the alternative to writing:

```python
personal = '<h1>Hello, ' + name + '!</h1>'
```

The benefit might not be apparent when only one variable is inserted into the string, as seen here, but string formatters are great when you have to insert multiple variables &mdash; they save you from typing all those quotation marks and plus signs!

```python
personal = '<p>Dear {} {}, We are pleased to inform you that your {} has been awarded {}.</p>'.format(title, name, relative, award)
```

Imagine that a query to a database has been made, and the values of `title`, `name`, `relative` and `award` are, respectively, `Ms.`, `Smith`, `daughter` and `the Gator Greatness Prize`. In that case, the *value* of the variable `personal` would be: `<p>Dear Ms. Smith, We are pleased to inform you that your daughter has been awarded the Gator Greatness Prize.</p>`

More details: [How To Use String Formatters in Python 3](https://www.digitalocean.com/community/tutorials/how-to-use-string-formatters-in-python-3)
