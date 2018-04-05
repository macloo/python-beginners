# Part 5: Deploy a Flask app

When professionals deploy their Python web apps, nowadays they commonly deploy to a cloud service such as [Amazon's AWS](https://aws.amazon.com/) or [Heroku](https://www.heroku.com/).

One thing to understand, though, is that they often do not deploy a Python executable. That is, the site they upload to a web server is not the Flask app and its associated templates, etc., but rather a traditional website with hard-coded HTML files that has been *“baked out”* from Flask.

In this document, we'll learn how to do that. Then we will also learn how to install a Flask app (one that has not been “baked out”) on:

* Heroku, via `git` commands, and using Gnunicorn.
* A typical web hosting service such as [Reclaim Hosting](https://reclaimhosting.com/), using a simple **cPanel** service there.

## “Baking it out” with Frozen-Flask

**Frozen-Flask** is a Flask extension, so we'll need to install it. In Terminal, change into your Flask projects folder and activate your virtualenv there. Then install at the bash prompt (`$`):

```bash
pip install Frozen-Flask
```

After installing the extension, create a new file named *freeze.py* and copy/paste this script into it:

```python
from flask_frozen import Freezer
# instead of routes, use the name of the file that runs YOUR Flask app
from routes import app

app.config['FREEZER_RELATIVE_URLS'] = True

freezer = Freezer(app)

if __name__ == '__main__':
    freezer.freeze()
```

Save the file *freeze.py* inside the folder with your Flask app. For example:

```
my-flask-app
├── static/
│   └── css/
│       └── main.css
├── templates/
│   ├── index.html
│   └── detail.html
├── data.py
├── freeze.py
├── modules.py
└── routes.py
```

Save your files.

If the Flask web server is running, quit it with Control-c.

In Terminal, change into the directory for the Flask app and enter this command at the bash prompt (`$`):

```bash
python freeze.py
```

**If freezing worked:** Inside your Flask app folder, you’ll now see a new folder named *build*. Open it. Inside *build*, you’ll see a folder that has the same name as your Flask route (for example, *president*). Open that folder.

There are all your files, created by Frozen-Flask.

For an example, open the *pres_app* folder in this repo, find the *build* folder, and look inside. You'll see 45 fully coded `.html` files.

The entire *build* folder can be uploaded to a web server, and the folder name can be changed (from *build* to anything), and all the pages will work.

Need to update the site? Make your edits, run *freeze.py* again, and re-deploy.

### The benefits of freezing

Pause for a moment and consider this: Imagine you needed to build a site with detailed data about the 535 members of the U.S. Congress. You build it with Flask (using a CSV file, a Python dictionary, or an SQL database to generate all the data) with two or maybe three HTML templates. Then you run *freeze.py* and in seconds you have 535 individual files, which you just upload as one folder, and you're done.

Similar apps might produce pages for:

* 190 pages for each dog breed in the American Kennel Club
* 318 pages for each character in all the Harry Potter novels
* 3,144 counties and county equivalents in the United States
* 6,909 living languages in the world

When there are changes to the data, you update the data source, re-freeze and re-deploy.

### Freezer errors

**If freezing did not work:** This may happen because your app uses dynamic routes similar to this:

```python
@app.route('/actor/<id>')
```

You might need to add [a URL generator](http://pythonhosted.org/Frozen-Flask/#url-generators) to the *freeze.py* file.

For example:

```python
from data import ACTORS

@freezer.register_generator
def actor():
    for item in ACTORS:
        yield { 'id': item['id'] }
```

You can definitely freeze an app with dynamic route information, but you might need to play around with it awhile before you get it to work.

Some apps *cannot* work via freezing. See below for details.

Read the [full documentation](http://pythonhosted.org/Frozen-Flask/) for Frozen-Flask.

## When freezing will not work, cannot work

If your app depends on dynamic activity &mdash; for example, if you are using **Flask-WTF** to process a form &mdash; you will not get a fully functioning app if you freeze it.

In that case, you will need to run Python on a web server, where people are accessing your pages (and NOT freeze the app).

There are ways to do this if you use a cloud service such as [Amazon's AWS](https://aws.amazon.com/) or [Heroku](https://www.heroku.com/), but you don't necessarily need to go that way if you're a student and your app is not going to attract thousands of users.

### The hosted website solution

Most hosted web server accounts from companies such as [Reclaim Hosting](https://reclaimhosting.com/) provide **cPanel** &mdash; a set of services that you access from a simple dashboard.

<img src="../images/setup_python_cpanel.png" alt="Set up Python cPanel icon" width="40%">

If you find the icon above in the **cPanel** at your hosting provider, you're probably good to go. I've written [detailed instructions](http://bit.ly/flask-deploy) for how to install a Python app at Reclaim Hosting, but it's probably the same or very nearly so in any **cPanel** instance.

### Using Heroku instead

You can get started on [Heroku](https://www.heroku.com/) for free, and if you find you need more than the free option provides, you can [change your plan](https://www.heroku.com/pricing).

The example app is the same as the final *students* app in the [templates](../../part3_templates) section of this repo. The complete app deployed to Heroku is in the *students-flask-app* folder here.
