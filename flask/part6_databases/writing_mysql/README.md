# Writing to a MySQL database

Parts of the app described here are duplicated from the app explained in [reading_mysql](../reading_mysql), so those parts will not be repeated here.

Prerequisites for this tutorial are explained in the README in [part6_databases](../../part6_databases) in this repo. It's essential to get your database connection working without errors before you try doing more with the database and Flask.

## Contents

## Add, update or delete a database record

The purpose of this section (and its Flask app) is to show how to write to a MySQL database using **Flask-SQLAlchemy** commands.

*Writing* to the database can happen in three different ways, and there are different commands for each of these.

1. Add a new record: Create a complete new entry and add it to the database.
2. Update a record: Retrieve an existing record and allow the user to edit any part of it, then write the changes to the database.
3. Delete a selected record.

For option 1, we do not have to find a record in the database. We need an empty form, and the user fills it in and submits it.

For options 2 and 3, we must identify the existing record.

For option 2, we can use the same form used for option 1, but we must fill it in with all the existing data. Then the user changes whichever items need editing and submits the form.

For option 3, after identifying the desired record, we must remove it completely from the database.

# The forms

This Flask app includes four forms. Three of those are Flask-WTF forms as described in [part4_forms](../../part4_forms) in this repo.

The first form we see is actually a table containing all the contents of the MySQL database. Each record row begins with a radio button, allowing the user to select one (and only one) record for editing or deleting. This form is built from the database using Jinja2 template commands in the template file [table.html](flask-db-write/templates/table.html). The value of the radio button control is the record ID from the database.

The other three forms are built with Flask-WTF, and so Python classes are built for them:

* `UpdateChoiceForm()`
* `DeleteChoiceForm()`
* `AddRecord()`

Only `AddRecord()` uses `wtf.quick_form()` in its template, [add.html](flask-db-write/templates/add.html). The other two forms are coded in their respective templates, [update_record.html](flask-db-write/templates/update_record.html) and [delete_record.html](flask-db-write/templates/delete_record.html).

More TK
