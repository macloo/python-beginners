from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/student/<idnum>')
def student(idnum):
    return render_template('student.html', id=idnum)

if __name__ == '__main__':
    app.run(debug=True)
