# no templates in this app - see students2.py 

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
