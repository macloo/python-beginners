# Introduction to Flask

Flask is a Python framework for building web apps. It's small, light and simple compared with the other widely used Python framework, [Django](https://www.djangoproject.com/).

[This site](http://flask.pocoo.org/) is the home of Flask.

We will install Flask in a new Python3 virtual environment. Students have already installed both Python3 and virtualenv.

[Install Python3, virtualenv, Jupyter](http://bit.ly/install-python3-jupyter)

## Setup for Flask

### Create a directory and change into it

The first step is to create a new folder (directory) for all your Flask projects. Mine is:

```bash
Documents/python/flask
```

**Change into that directory.** For me, the command would be:

```bash
cd Documents/python/flask
```

### Create a new virtualenv in that directory and activate it

Create a new **virtualenv** there (this is done only once):

**Mac OS/bash**
```bash
$ virtualenv --python=/usr/local/bin/python3 env
```

**Windows PowerShell**
```bash
PS> virtualenv --python=C:\Python36\python.exe env
```

Activate the **virtualenv**:

**Mac OS/bash**
```bash
$ source env/bin/activate
```

**Windows PowerShell**
```bash
PS> env\Scripts\activate.bat
```

**Important:** You should now see `(env)` at the far left side of your prompt. This indicates that the **virtualenv** is active. Example (Mac OS/bash):

```bash
(env) mcadams flask $
```

### Install Flask

In Mac OS or Windows, at the `$` bash prompt (or Windows `PS>`), type:

```bash
pip install Flask
```

This is how you install *any* Python library that exists in the [Python Package Index](https://pypi.python.org/pypi). Pretty handy. **pip** is a tool for installing Python packages, which is what you just did.

**Note:** You installed Flask in the Python3 **virtualenv** that is currently active. When that **virtualenv** is *not* active, Flask will not be available to you. This is ideal, because you will create different virtual environments for different Python projects, and you won't need to worry about updated libraries in the future breaking your (past) code.

### Test Flask

Using Atom, create a file in your *flask* directory, copy/paste the code into it, and save it with the name *hello.py*.

```python
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"
```

In Terminal, at the `$` bash prompt, type this:

```bash
FLASK_APP=hello.py flask run
```

You'll see this:

<img src="images/flask_server_starts.png" alt="Results of FLASK_APP=hello.py flask run">

Open your web browser and, in the address bar, type: `localhost:5000`

<img src="images/flask_in_browser.png" alt="Result in the browser" width="50%">

Flask includes a built-in web server, for development use. What you've done is:

1. With the `hello.py` file, you have written a small (and essentially useless) web app in Flask.
2. With the command `FLASK_APP=hello.py flask run`, you started the server and ran the app on it.

**To shut down the server,** press Control-C in Terminal.

## Deconstruct the code in a small Flask app

```python, lineNo
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"
```

The first line is a typical Python import statement. Flask is a Python library, and it must be imported. As always, *case matters,* so note the lowercase *f* and the uppercase *F*. (We are importing the *Flask* class from the *flask* module, and they are two different things.)

The second line, which is new to you, begins with a new variable, `app`, which will be used in every Flask app. The value of that new variable, `Flask(__name__)`, is a new *object* that inherits from the class *Flask* &mdash; meaning that it gets all the attributes and methods built into that class. Imagine we could clone Wonder Woman or Superman. The clone has all the same powers and attributes of the superhero, but the clone can be modified so that does certain things under certain conditions.
