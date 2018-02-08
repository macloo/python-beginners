# Web Scraping

We use this book: *Web Scraping with Python: Collecting Data from the Modern Web,* by Ryan Mitchell (O’Reilly, 2015). A new 2nd edition of this will be published in 2018 but is not yet available, so we must use the 1st edition.

Python3 is used throughout this book.

## Contents

* [Setup for BeautifulSoup](#setup-for-beautifulsoup)
    * [Create a directory and change into it](#create-a-directory-and-change-into-it)
    * [Create a new virtualenv in that directory and activate it](#create-a-new-virtualenv-in-that-directory-and-activate-it)
    * [Install the BeautifulSoup library](#install-the-beautifulsoup-library)
    * [Test BeautifulSoup](#test-beautifulsoup)
* [Understanding BeautifulSoup](#understanding-beautifulsoup)
    * [How BeautifulSoup handles the object](#how-beautifulsoup-handles-the-object)

## Setup for BeautifulSoup

**BeautifulSoup** is a scraping library for Python. We want to run all our scraping projects in a virtual environment. Students have already installed both Python3 and virtualenv.

* [Install Python3, virtualenv, Jupyter](http://bit.ly/install-python3-jupyter)

### Create a directory and change into it

The first step is to create a new folder (directory) for all your scraping projects. Mine is:

```bash
Documents/python/scraping
```

Do not use any spaces in your folder names. If you must use punctuation, do not use anything other than an underscore (\_). It's easiest if you use only lowercase letters.

**Change into that directory.** For me, the command would be:

```bash
cd Documents/python/scraping
```

### Create a new virtualenv in that directory and activate it

Create a new **virtualenv** there (this is done only once).

**Mac OS**
```bash
$ virtualenv --python=/usr/local/bin/python3 env
```

**Windows**
```bash
PS> virtualenv --python=C:\Python36\python.exe env
```

Activate the **virtualenv**:

**Mac OS**
```bash
$ source env/bin/activate
```

**Windows**
```bash
PS> env\Scripts\activate.bat
```

**Important:** You should now see `(env)` at the far left side of your prompt. This indicates that the **virtualenv** is active. Example (Mac OS):

```bash
(env) mcadams scraping $
```

When you are finished working in a **virtualenv**, you should *deactivate* it. The command is the same in Mac OS or Windows (DO **NOT** DO THIS NOW):

```
deactivate
```

You'll know it worked because `(env)` will no longer be at the far left side of your prompt.

### Install the BeautifulSoup library

In Mac OS or Windows, at the bash prompt (Mac `$` or Windows `PS>`), type:

```bash
pip install beautifulsoup4
```

This is how you install *any* Python library that exists in the [Python Package Index](https://pypi.python.org/pypi). Pretty handy. **pip** is a tool for installing Python packages, which is what you just did.

**Note:** You installed BeautifulSoup in the Python3 **virtualenv** that is currently active. When that **virtualenv** is *not* active, BeautifulSoup will not be available to you. This is ideal, because you will create different virtual environments for different Python projects, and you won't need to worry about updated libraries in the future breaking your (past) code.

### Test BeautifulSoup

**Start Python.** Because you are in a Python3 **virtualenv**, you need only type `python`.

You should now be at the `>>>` prompt &mdash; the Python prompt.

In Mac OS or Windows, type (or copy/paste) *one line at a time*:

```python
from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen("http://www.pythonscraping.com/exercises/exercise1.html")
bsObj = BeautifulSoup(html, "html.parser")
print(bsObj.h1)
```

1. You imported two Python modules, `urlopen` and `BeautifulSoup` (the first two lines).
2. You used `urlopen` to copy the entire contents of the URL given into a new Python variable, `html`.
3. You used `BeautifulSoup` to process the value of that variable (the contents of the file at that URL) through a built-in HTML parser (`html.parser` is not the only option for this). The result: All the HTML from the file is now in a BeautifulSoup object with the new Python variable name `bsObj`.
4. Using the syntax of the BeautifulSoup library, you printed the first H1 element (including its tags) from that parsed value. Check out [the page on the web](http://www.pythonscraping.com/exercises/exercise1.html) to see what you scraped.

If it works, you'll see:

```python
<h1>An Interesting Title</h1>
```

The example comes from page 8 of Mitchell's book; the code is updated in her [GitHub repo](https://github.com/REMitchell/python-scraping) (chapter1) for the book, where we can find **updated code** that will no doubt appear in her 2nd edition.

## Understanding BeautifulSoup

It's very important to understand that many of the BeautifulSoup commands work on an *object*, which is not the same as a simple *string*. Throughout her book, Mitchell uses the variable name `bsObj` to remind us of that fact.

Many programming languages include objects as a data type. Python does, JavaScript does, etc. An *object* is an even more powerful and complex data type than an *array* (JavaScript) or a *list* (Python) and can contain many other data types in a structured format.

When you extract information from an *object* with a BeautifulSoup command, sometimes you get a simple string, and sometimes you get a Python *list* (which is very similar to an *array* in JavaScript). The way you treat that extracted information will be **different** depending on whether it is a string (*one* item) or a list (usually *more than one* item).

## How BeautifulSoup handles the object

In the previous code, when this line ran:

```python
html = urlopen("http://www.pythonscraping.com/exercises/exercise1.html")
```

... you copied the entire contents of a file into a new Python variable named `html`. The contents were stored as an *HTTPResponse object*. We can read the contents of that object like this:

<img src="images/url_blob.png" alt="Results of html.read()">

... but that's not going to be very usable, or useful &mdash; especially for a file with a lot more content in it.

When you transform that *HTTPResponse object* into a *BeautifulSoup object*, with the following line, you create an object from which you can extract *any HTML element* and the text *within* any HTML element.

```python
bsObj = BeautifulSoup(html, "html.parser")
```

### Finding all the elements with a class

Deciding the best way to extract what you want from a large HTML file requires you to dig around in the source before you write the Python/BeautifulSoup commands. In many cases, you'll see that everything you want has the same **CSS class** on it. After creating a *BeautifulSoup object* (here, as before, it is in the variable `bsObj`), this line will create a Python *list* (you can think of it as an *array*) containing all the `<td>` elements that have the class `city`.

```python
city_list = bsObj.findAll( "td", {"class":"city"} )
```


* Searching for tags by attributes
* Working with lists of tags
* Parse tree navigation 

*to be continued*
