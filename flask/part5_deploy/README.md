# Part 5: Deploy a Flask app

When professionals deploy their Python web apps, nowadays they commonly deploy to a cloud service such as [Amazon's AWS](https://aws.amazon.com/) or [Heroku](https://www.heroku.com/).

One thing to understand, though, is that they often do not deploy a Python executable. That is, the site they upload to a web server is not the Flask app and its associated templates, etc., but rather a traditional website with hard-coded HTML files that has been *“baked out”* from Flask.

In this document, we'll learn how to do that. Then we will also learn how to install a Flask app (one that has not been “baked out”) on a typical web hosting service such as [Reclaim Hosting](https://reclaimhosting.com/), using a simple cPanel service there.

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

Inside your Flask app folder, you’ll now see a new folder named *build*. Open it. Inside, you’ll see a folder that has the same name used in your Flask route (for example, song). Open that folder.

There are all your files.

For an example, open the *pres_app* folder in this repo, find the *build* folder, and look inside.

The entire *build* folder can be uploaded to a web server, and the folder name can be changed (from *build* to anything), and all the pages will work.

Need to update the site? Make your edits, run *freeze.py* again, and re-deploy.

### Freezer errors

If your app uses dynamic routes similar to this:

```python
@app.route('/actor/<id>')
```

You might need to add [a URL generator](http://pythonhosted.org/Frozen-Flask/#url-generators) to *freeze.py*.

For example:

```python
from data import ACTORS

@freezer.register_generator
def actor():
    for item in ACTORS:
        yield { 'id': item['id'] }
```

You can definitely freeze the app with dynamic route information, but you might need to play around with it awhile before you get it to work.
