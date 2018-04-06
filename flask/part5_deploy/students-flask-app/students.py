from flask import Flask, render_template
from data import PEOPLE
from modules import get_all_students, get_student

app = Flask(__name__)

# line below for dev only
# make sure cache does not retain templates
# app.config['TEMPLATES_AUTO_RELOAD'] = True

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
