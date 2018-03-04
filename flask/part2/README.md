# Part 2: Baby Steps with Flask

You've seen a very, very simple Flask app in the [introduction](https://github.com/macloo/python-beginners/tree/master/flask). Let's step it up a little.

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

Now we have two routes, not one. The first route, for `'/'`, is not very different from our first Flask app. The second route, for `'/user/<name>'`, is doing something new.

1. Copy this code into a new file named `hello2.py` and run it at the bash (`$`) prompt with:

   ```bash
   python hello2.py
   ```

   **Note:** With the final two lines in this script, we do not need the longer command we ran in in the introduction.

2. In your browser, type `localhost:5000` into the address bar.

This script demonstrates the following:

* The URL in the browser causes a Python function to run. Remember, the *path* is specified in the decorator &mdash; `@app.route('/')`. The function *immediately after* the decorator is called when that path is sent to the server.
* The link written in the `hello()` function opens the URL specified in `@app.route('/user/<name>')`: `localhost:5000/user/Albert`
* The path can have a dynamic component &mdash; in this case, `<name>`. The function after `@app.route('/user/<name>')` takes the *value* of `name` from the HTTP request (the path sent to the server) and uses that value in the function.
* The string `"Albert"` from the URL is used in the function `user()` to write dynamically in the browser window.
* You can change the name value in the browser's address bar, refresh/reload, and the contents of the window will change accordingly.

## Running your Flask apps

In most cases, the last lines in your Flask app script will be:

```python
if __name__ == '__main__':
    app.run(debug=True)
```

This enables you to launch Flask's built-in server and run the app simply by typing `python filename.py` at the bash (`$`) prompt in Terminal.

* `if __name__ == '__main__':` <br>
   This returns `True` when the program (the file) is being *run by itself,* and was not imported.

* `app.run()` <br>
  `app` is the Flask application object you created with `app = Flask(__name__)`. It has all the methods and attributes of the *Flask* class, and one of those is `run()`.

* `debug=True` is very useful when you're developing, because with it, any errors that occur will be written out in the browser.
