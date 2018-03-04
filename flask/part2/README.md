# Baby Steps with Flask

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
