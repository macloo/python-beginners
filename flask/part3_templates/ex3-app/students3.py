# version 3 of this app, using two templates

from flask import Flask, render_template
app = Flask(__name__)

# a small dataset for testing: a Python list containing 2 Python dictionaries
# each dictionary contains data for 1 student
DATA = [
{"gender":"male","name":{"title":"mr","first":"darrell","last":"ramos"},"location":{"street":"4002 green rd","city":"peoria","state":"new york","postcode":62121},"dob":"1960-03-09 16:44:53","id":{"name":"SSN","value":"778-73-1993"},"picture":{"large":"https://randomuser.me/api/portraits/men/54.jpg","medium":"https://randomuser.me/api/portraits/med/men/54.jpg","thumbnail":"https://randomuser.me/api/portraits/thumb/men/54.jpg"}},
{"gender":"female","name":{"title":"mrs","first":"jeanette","last":"thomas"},"location":{"street":"7446 hickory creek dr","city":"caldwell","state":"wyoming","postcode":73617},"dob":"1959-03-21 14:19:01","id":{"name":"SSN","value":"578-92-7338"},"picture":{"large":"https://randomuser.me/api/portraits/women/56.jpg","medium":"https://randomuser.me/api/portraits/med/women/56.jpg","thumbnail":"https://randomuser.me/api/portraits/thumb/women/56.jpg"}}
]

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
            # address = street + ", " + city + ", " + state + " " + postal
            address = f'{street}, {city}, {state} {postal}'
            return name, photo, address
    # return these if id is not valid
    return "Unknown", "", "Unknown"

# the routes

@app.route('/')
def index():
    all_students = get_all_students(DATA)
    return render_template('index.html', student_list=all_students)

@app.route('/student/<idnum>')
def student(idnum):
    name, photo, address = get_student(DATA, idnum)
    return render_template('student.html', id=idnum, name=name, photo=photo, address=address)

# server startup
if __name__ == '__main__':
    app.run(debug=True)
