# version 4 of this app, using two templates

from flask import Flask, render_template
from data import PEOPLE
app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True

# from data import PEOPLE - above - imports PEOPLE, a list, from data.py
# PEOPLE is a Python list containing 100 Python dictionaries
# each dictionary contains data for 1 student


# additional functions to handle the data

# get data for all students to use in index and write alpha list there
# see function1_test.py for details
def get_all_students(source):
    students = {}
    for record in source:
        id = record['id']['value']
        lastname = (record['name']['last']).title()
        students.update({id:lastname})
    return sorted(students.items(), key=lambda x: x[1])

# get data from one student based on idnum - use in student
# see function2_test.py for details
def get_student(source, idnum):
    for record in source:
        if idnum == record['id']['value']:
            name = (record['name']['last']).title() + ", " + (record['name']['first']).title()
            photo = record["picture"]["large"]
            street = record["location"]["street"].title()
            city = record["location"]["city"].title()
            state = record["location"]["state"].title()
            postal = str(record["location"]["postcode"])
            address = street + ", " + city + ", " + state + " " + postal
            return name, photo, address
    # return these if id is not valid
    return "Unknown", "", "Unknown"

# the routes

@app.route('/')
def index():
    all_students = get_all_students(PEOPLE)
    return render_template('index.html', student_list=all_students, the_title="List All Students")

@app.route('/student/<idnum>')
def student(idnum):
    name, photo, address = get_student(PEOPLE, idnum)
    return render_template('student.html', id=idnum, name=name, photo=photo, address=address, the_title="Student Detail Page")

# server startup
if __name__ == '__main__':
    app.run(debug=True)
