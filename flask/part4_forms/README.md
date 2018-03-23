# Part 3: Forms in Flask

WTForms is “a flexible forms validation and rendering library for Python Web development.” With Flask-WTF, we get WTForms in Flask.

* WTForms includes security features for submitting form data.
* WTForms has built-in validation techniques.
* WTForms can be combined with Bootstrap to help us make clean-looking, responsive forms for mobile and desktop screens.

## Setup for using forms in Flask

We will install the **Flask-WTF** extension to help us work with forms in Flask. There are many extensions for Flask, and each one adds a different set of functions and capabilities. See the [list of Flask extensions](http://flask.pocoo.org/extensions/) for more.

In Terminal, change into your Flask projects folder and activate your virtualenv there. Then install at the bash prompt (`$`):

```bash
pip install Flask-WTF
```

We will also install the **Flask-Bootstrap** extension to provide Bootstrap styles for our forms.

```bash
pip install flask-bootstrap
```

This installation is done only once in any virtualenv. It is assumed you already have Flask installed here.

### Resources

[Flask-WTF documentation](https://flask-wtf.readthedocs.io/en/latest/index.html)

[Flask-Bootstrap documentation](https://pythonhosted.org/Flask-Bootstrap/)
