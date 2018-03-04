# Part 3: Templates in Flask

In the [Flask introduction](https://github.com/macloo/python-beginners/tree/master/flask) and in [flask/part2](https://github.com/macloo/python-beginners/tree/master/flask/part2), we wrote some HTML directly in the Flask app script. This is very awkward, so naturally, Flask provides a better way to store the HTML (and CSS) you will want your Flask functions to generate.

## Folder structure for a Flask app

A proper Flask app is going to use multiple files &mdash; some of which will be template files. The organization of these files has to follow rules so the app will work. Here is a diagram of the typical structure:

```
my-flask-app
├── static/
│   └── css/
│       └── main.css
├── templates/
│   ├── index.html
│   └── student.html
├── data.py
└── students.py
```

1. Everything the app needs is in one folder, here named *my-flask-app*.
2. That folder contains two folders, specifically named *static* and *templates*.
   * The *static* folder contains assets used by the templates, including CSS files, JavaScript files, and images. In the example, we have only one asset file, *main.css*. Note that it's inside a *css* folder that's inside the *static* folder.
   * The *templates* folder contains only templates. These have an `.html` extension. As we will see, they contain more than just regular HTML.
3. In addition to the *static* and *templates* folders, this app also contains `.py` files. Note that these must be *outside* the two folders named *static* and *templates*.

The templates will not work if this folder structure is not exactly as described above. Your app folder can be named anything (not only *my-flask-app*), but the *static* and *templates* folders must be named and organized as shown above.

## Get started with templates

We'll start with a small Flask app similar to the one explained in [flask/part2](https://github.com/macloo/python-beginners/tree/master/flask/part2).

```python
from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    greet = '<h1>Welcome to the student records Flask example!</h1>'
    link = '<p><a href="student/778-73-1993">Click me!</a></p>'
    return greet + link

@app.route('/student/<idnum>')
def student(idnum):
    # the curly braces {} are a placeholder for the value in
    # parentheses, in format()
    personal = '<h1>Hello, student number {}!</h1>'.format(idnum)
    instruc = '<p>Change the number in the <em>browser address bar</em> and reload the page.</p>'
    return personal + instruc

if __name__ == '__main__':
    app.run(debug=True)
```

To replace the awkward HTML in the functions and use templates instead, we make one change to the **top part** of the file (where we *initialize* the app):

```python
from flask import Flask, render_template
app = Flask(__name__)
```

We must import `render_template` from the `flask` module, or else templates will not work.

The rest of our changes take place in the route functions:

```python
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/student/<idnum>')
def student(idnum):
    return render_template('student.html', id=idnum)
```

Nice, eh? You might recall that in the folder structure diagram above, the *templates* folder contained two files, named *index.html* and *student.html*. Those files do not appear by magic &mdash; you will need to write them.

*index.html* will be a normal HTML file, with `<html>`, `<head>`, `<body>`, etc. Inside the body, we'll write:

```html
<h1>Welcome to the student records Flask example!</h1>

<ul>
    <li><a href="student/778-73-1993">Student Ramos</a></li></p>
    <li><a href="student/578-92-7338">Student Thomas</a></li></p>
</ul>
```

*student.html* will include a **placeholder** in *double curly braces* to enable a student ID number to be written into the HTML when it loads. In all other respects, it is a normal HTML file, with `<html>`, `<head>`, `<body>`, etc. Inside the body, we'll write:

```html
<h1>Hello, student number {{ id }}!</h1>

<p><a href="/">Return to the list</a> to select a different student.</p>
```

A crucial part of this is the **variable name** inside those *double curly braces*. For the template to work, that variable MUST be passed to the template with a **value**. So the template HTML, above, contains one variable, `id`. In the Flask route function, we gave `id` the value of `idnum` &mdash; which received its value from the URL requested.

```python
@app.route('/student/<idnum>')
def student(idnum):
    return render_template('student.html', id=idnum)
```

The complete code for this app is in the folder [flask/part3_templates/ex1-app](https://github.com/macloo/python-beginners/tree/master/flask/part3_templates/ex1-app). To run it, `cd` into the `ex1-app` directory and type this at the bash prompt (`$`) in Terminal:

```bash
python students2.py
```

## The “base” template

Because we have two templates, I'm going to add a base template named *base.html* to the *templates* folder.
