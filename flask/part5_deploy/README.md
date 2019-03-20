# Part 5: Deploy a Flask app

When professionals deploy their Python web apps, nowadays they commonly deploy to a cloud service such as [Amazon's AWS](https://aws.amazon.com/) or [Heroku](https://www.heroku.com/).

One thing to understand, though, is that often they do not deploy a Python executable. That is, the site they upload to a web server is not the Flask app and its associated templates, etc., but rather a traditional website with hard-coded HTML files that has been *“baked out”* from Flask.

In this document, we'll learn how to do that. Then we will also learn how to install a Flask app (one that has not been “baked out”) on:

* A typical web hosting service such as [Reclaim Hosting](https://reclaimhosting.com/), using a simple **cPanel** service there.
* Heroku, via `git` commands, and using the Gunicorn server.

## Contents

* [“Baking it out” with Frozen-Flask](#baking-it-out-with-frozen-flask)
  * [The benefits of freezing](#the-benefits-of-freezing)
  * [Freezer errors](#freezer-errors)
* [When freezing will not work, cannot work](#when-freezing-will-not-work-cannot-work)
  * [The hosted website solution](#the-hosted-website-solution)
  * [Using Heroku instead](#using-heroku-instead)
     * [Preliminary steps](#preliminary-steps)
     * [Deploy to Heroku](#deploy-to-heroku)
     * [The Heroku dashboard](#the-heroku-dashboard)
* [Conclusion](#conclusion)

## “Baking it out” with Frozen-Flask

**Frozen-Flask** is a Flask extension, so we'll need to install it. In Terminal, change into your Flask projects folder and activate your virtualenv there. Then install at the bash prompt (`$`):

```bash
pip3 install Frozen-Flask
```

After installing the extension, create **a new file** inside the folder containing the Flask app you want to "freeze." Name the new file *freeze.py* and copy/paste this script into it:

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

**If freezing worked:** Inside your Flask app folder, you’ll now see a new folder named *build*. Open it. Inside *build*, you’ll see all the files created by Frozen-Flask.

For an example, open the *pres_app* folder in this repo, find the *build* folder, and look inside. You'll see *index.html* and two folders, *static* and *president.* Inside *president,* you'll see 45 fully coded `.html` files.

The entire *build* folder can be uploaded to a web server, and the folder name can be changed (from *build* to anything), and all the pages will work. (Just don't change or rename anythng inside the *build* folder.)

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

If your app depends on dynamic activity &mdash; for example, if you are using **Flask-WTF** to process a form &mdash; you will not get a fully functioning app if you freeze it. Similarly, if you're accessing an API to get data that changes frequently (such as currency rates or weather), you cannot freeze that app.

In those cases, you will need to run Python on a web server, where people are accessing your pages (and NOT freeze the app).

There are ways to do this if you use a cloud service such as [Amazon's AWS](https://aws.amazon.com/) or [Heroku](https://www.heroku.com/), but you don't necessarily need to go that way if you're a student and your app is not going to attract thousands of users.

### The hosted website solution

Most hosted web server accounts from companies such as [Reclaim Hosting](https://reclaimhosting.com/) provide **cPanel** &mdash; a set of services that you access from a simple dashboard.

<img src="../images/setup_python_cpanel.png" alt="Set up Python cPanel icon" width=212>

If you find the icon above in the **cPanel** at your hosting provider, you're probably good to go. I've written [detailed instructions](http://bit.ly/flask-deploy) for how to install a Python app at Reclaim Hosting, but it's probably the same or very nearly so in any **cPanel** instance.

### Using Heroku instead

You can get started on [Heroku](https://www.heroku.com/) for free, and if you find you need more than the free option provides, you can [change your plan](https://www.heroku.com/pricing).

The example app for deployment to Heroku here is the same as the final *students* app in the [templates](../part3_templates) section of this repo. The complete app deployed to Heroku is in the *students-flask-app* folder here. The app is running at this URL:

https://students-flask.herokuapp.com/

Once you have a Heroku account, download the [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli), a command-line tool. Use the appropriate installer for your operating system. Test that it was installed successfully by entering this in Terminal at the bash prompt (`$`):

```bash
heroku --version
```

Follow the **login** instructions under [Getting Started](https://devcenter.heroku.com/articles/heroku-cli#getting-started).

You will log in this way *each time* you use the Heroku CLI. You can log out &mdash; `heroku logout` &mdash; or just quit Terminal.

You can [read more](https://devcenter.heroku.com/categories/command-line) about the Heroku CLI if you like.

#### Preliminary steps

If you use the [GitHub Desktop app](https://desktop.github.com/), you already have command-line `git`. This is not part of Heroku, but **you will need to use** command-line `git` to *deploy to* Heroku.

Before proceeding with command-line `git`, your Flask app should be ready to deploy (all code completed and tested). You must also complete these steps:

1. Install **Gunicorn**: You need to add a production-level web server to your web app. Heroku recommends [Gunicorn](https://gunicorn.org/) for Python applications. Activate the virtualenv for your app and install it with `pip3 install gunicorn`.

2. Create or update *requirements.txt*: Instructions are [here](http://bit.ly/python-reqs). Even if you created a *requirements.txt* file earlier, you must re-create it to add **Gunicorn** to the list. **This is absolutely necessary.**

3. Make sure there is a *.gitignore* file in your repo and it excludes your *env/* or *venv/* folder. **You must NOT commit virtual environment files** &mdash; the *requirements.txt* file lists all the contents of your virtualenv so that it can be re-created on Heroku.

4. Create *Procfile*: This is a plain-text file that must be named exactly `Procfile` (uppercase P, and no file extension). Its contents declare which commands are run by the application's dynos on Heroku. Read more about *Procfile* [here](https://devcenter.heroku.com/articles/procfile).

To run a simple Python web app (such as our example app, *students.py* in *students-flask-app*), the complete contents of *Procfile* are:

```
web: gunicorn students:app
```

**Database:** Note that Heroku prefers PostgreSQL and not MySQL or MariaDB. If your app includes a MySQL database, [read this](https://devcenter.heroku.com/articles/heroku-mysql). Our example app, *students-flask-app*, does not use any SQL database, so we can deploy it simply.

#### Deploy to Heroku

To *register* a new application with Heroku, use the `apps:create` command. **You must be in the root directory of your app.** So at the bash prompt (`$`), I am *inside* the *students-flask-app* directory, and my virtualenv is **not active.**

```bash
heroku apps:create students-flask
```

Heroku applications must have a unique name, so if yours is taken, you will need to choose another name. It does not need to match your app folder name.

The command will return the **web address** of your app: https://students-flask.herokuapp.com/

You'll *register* the app only *once.*

Before you *push to Heroku,* make sure all changes are *committed* (in the GitHub Desktop app).

Then at the bash prompt (`$`), type:

```bash
git push heroku master
```

Many lines of messages from the *remote* branch on Heroku will be printed to the Terminal. Wait until you see `Verifying deploy... done.` And then ... you're back at the bash prompt (`$`).

Use your web browser to go to the web address given above to view the active app.

You'll find you have a new *branch* in your local repo.

<img src="../images/heroku_branch.png" alt="Branch in GitHub app" width=308>

If you *make changes* to the app, you'll need to **push to Heroku again.** Save files and commit locally. Log into Heroku (if not already logged in), and:

```bash
git push heroku master
```

#### The Heroku dashboard

When you are logged in at Heroku.com, you'll see your Heroku dashboard. All your registered apps are listed here. To manage an app, click its name.

**To delete an app** from Heroku, once you've clicked its name, click *Settings.* Then click the **Delete app** button at the bottom of the page. You will be asked to confirm your choice.

You can also manage other aspects of your app, such as config variables, on the *Settings* page. You can also [add a custom domain name](https://devcenter.heroku.com/articles/custom-domains) for your app.

## Conclusion

We've learned about three different options for deploying a Flask app:

* Use Frozen-Flask
* Deploy to a hosted web account
* Deploy to Heroku, a free cloud service

Depending on the characteristics of your Flask app, one of these options might be much better than the others, or they might all be equally suitable.

See [more options for deploying](http://flask.pocoo.org/docs/1.0/deploying/) in the Flask documentation.
