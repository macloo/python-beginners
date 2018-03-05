# Part 3: Templates in Flask

In the [Flask introduction](https://github.com/macloo/python-beginners/tree/master/flask) and in [flask/part2](https://github.com/macloo/python-beginners/tree/master/flask/part2), we wrote some HTML directly in the Flask app script. This is very awkward, so naturally, Flask provides a better way to store the HTML (and CSS) you will want your Flask functions to generate.

## Contents

* [Folder structure for a Flask app](#folder-structure-for-a-flask-app)
* [Example 1: Get started with templates](#example-1-get-started-with-templates)
* [Example 2: Using a “base” template](#example-2-using-a-base-template)
* [Example 3: The real power of templates is revealed](#example-3-the-real-power-of-templates-is-revealed)
   * [Understanding a Python dictionary](#understanding-a-python-dictionary)
   * [Data in and data out (functions)](#data-in-and-data-out-functions)
   * [Changes to the templates](#changes-to-the-templates)
* [Templates: Conclusion](#templates-conclusion)

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

## Example 1: Get started with templates

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

## Example 2: Using a “base” template

A great time-saving feature of templates in Flask: We can tremendously shorten and streamline multiple template files by creating *one base template* that contains all the standard HTML. I have a base template named *base.html* in the *templates* folder in the [second version of the students app](https://github.com/macloo/python-beginners/tree/master/flask/part3_templates/ex2-app).

Inside the `<body>` in the file, you'll see this:

```html
{% block content %}
{% endblock %}
```

Each of those two lines is a Jinja2 directive. Jinja2 is the [template engine](http://jinja.pocoo.org/docs/2.10/templates/) used by Flask. If you've used PHP, you should be able to understand pretty quickly how these directives work.

**block label** (in this case, the label is *content*; it can be anything) signifies the start of inserted material. If you have more than one **block** in your template, make sure each block has a unique label. The block labels must *match* what is used in the dependent templates that use this one.

**endblock** signifies the end of inserted material.

Using this *base.html* template, we can trim our *index.html* template down to only this:

```html
{% extends 'base.html' %}

{% block content %}

<h1>Welcome to the student records Flask example!</h1>

<ul>
    <li><a href="student/778-73-1993">Student Ramos</a></li></p>
    <li><a href="student/578-92-7338">Student Thomas</a></li></p>
</ul>

{% endblock %}
```

That's the entire contents of the file. Note the following two important points:

* `{% extends 'base.html' %}` matches the exact filename of our base template, which is in the same *templates* folder.
* `{% block content %}` matches the exact label in the block in the base template. If, for example, it were *block foobar* in the template, it would need to also be *block foobar* here.

The only difference between the [ex1-app](https://github.com/macloo/python-beginners/tree/master/flask/part3_templates/ex1-app) example app and the  [ex2-app](https://github.com/macloo/python-beginners/tree/master/flask/part3_templates/ex2-app) example app is the addition of the *base.html* template file in the second example.

## Example 3: The real power of templates is revealed

Now you'll see how to write 100 web pages with no actual HTML files. Well, except for the three template files you already have.

We are building on the  [ex2-app](https://github.com/macloo/python-beginners/tree/master/flask/part3_templates/ex2-app) example app, discussed above.

Now, in the third version &mdash; the  [ex3-app](https://github.com/macloo/python-beginners/tree/master/flask/part3_templates/ex3-app) example app &mdash; we will make our two templates much more useful by enabling them to use data read from a separate file, *data.py*. That file contains information (name, ID, address, etc.) about 100 students (not real people).

Instead of working with the whole file while working out the bugs, the *students3.py* file uses just two records from the dataset. In addition to the list named DATA, two new functions have been added. These functions are outside the routes, but they are called *in* the routes.

```
get_all_students() --> used in index()
makes a list of all students in the dataset

get_student()      --> used in student()
gets the following details about ONE student: name, address, photo
```

* We still have only two routes in our Flask app.
* We still have only two templates, plus the base template.
* We have added data about two students in *students3.py*.
* We have added two new Python functions (no Flask code in these):
   * get_all_students()
   * get_student()

The goal is to provide a list of all students (last names only) with an `<a href="">` that contains the student's ID number. When we click any student's name, a new URL opens, showing us details and a photo for just that one student.

The ID number is used in the link because it is sure to be unique, unlike a name. We have been using a number in the route `@app.route('/student/<idnum>')` all along.

The complete code for this app is in the folder [ex3-app](https://github.com/macloo/python-beginners/tree/master/flask/part3_templates/ex3-app). To run the final, complete app, `cd` into the `ex3-app` directory and type this at the bash prompt (`$`) in Terminal:

```bash
python students4.py
```

### Understanding a Python dictionary

If the two new functions don't make sense to you, it's probably because you have not learned about Python dictionaries.

The [week04](https://github.com/macloo/python-beginners/tree/master/week04) folder has examples for working with dictionaries. [This example](https://github.com/macloo/python-beginners/blob/master/week04/complex_dicts.py) uses the same data structure as the *students3.py* and *students4.py* files.

### Data in and data out (functions)

`get_all_students()` takes in the whole dataset as an argument, extracts the last name and ID number (SSN) for each person, and returns a sorted list of tuples. Each tuple contains two items, the last name and the ID number.

The route function `index()` calls `get_all_students()` and sends the list of tuples to a template as `student_list`.

`get_student()` takes in two arguments: the whole dataset, and the ID number that appears in the URL. The record for that ID number is found in the dataset, and each needed data value is taken from the record. Three values are returned.

The route function `student()` calls `get_student()` and sends the ID and three values to a template as `id`, `name`, `photo` and `address`.

### Changes to the templates

`index.html` now receives a list of links from the route function:

```html
<ul>
{% for item in student_list %}
    <li><a href="/student/{{ item[0] }}">{{ item[1] }}</a></li>
{% endfor %}
</ul>
```

You'll recognize `for item in student_list` as the beginning of a Python for-loop. It's wrapped in `{%` and `%}` &mdash; as is the Jinja2 directive that marks the end of the for-loop: `{% endfor %}`. If this reminds you of working with PHP &mdash; yes! It's the same idea.

`item[0]` an `item[1]` come from the tuple. The route function `index()` sends the list of tuples to this template as `student_list`. We loop over the list, and for each list item (that is, each tuple), the code puts the ID number (`item[0]`) into the `href` attribute and the last name (`item[1]`) between the `<a>` tags.

`student.html` receives four variables (`id`, `name`, `photo` and `address`) from the route function:

```html
<h1>{{ name }}</h1>

<p><strong>Student number:</strong> {{ id }}</p>

<p><strong>Address:</strong> {{ address }}</p>

<img src="{{ photo }}" alt="Student photo">
```

The variables are inserted where needed in the HTML as placeholders in *double curly braces*, which we've already covered here.

**Take note of the difference** between the Jinja2 elements in `index.html` and `student.html`:

* A list representing *every record* in the data source is generated in `index.html`; therefore, it has a for-loop to extract items from every record.
* Only *one record* is examined and represented in `student.html`, so there is no loop there. Only variables &mdash; which were passed in by the route.

## Templates: Conclusion

I hope the final app in *students4.py* has demonstrated clearly why using templates in Flask is well worth the effort required to learn.

Here is another [GitHub repo](https://github.com/macloo/flask_project1) and a [live website](https://weimergeeks.com/flask_proj1/awards/) for a very similar Flask app **with a much simpler data source.** If you compare the two projects, it might improve your understanding.

* [Flask template documentation](http://jinja.pocoo.org/docs/2.10/templates/) &mdash; all the commands for the Jinja2 template syntax are here.
* [Welcome to Jinja2](http://jinja.pocoo.org/docs/2.10/) &mdash; everyhting about Jinja2.
