from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    greet = '<h1>Hello, Gators!</h1>'
    link = '<p><a href="user/Albert">Click me!</a></p>'
    return greet + link

@app.route('/user/<name>')
def user(name):
    personal = f'<h1>Hello, {name}!</h1>'
    instruc = '<p>Change the name in the <em>browser address bar</em> and reload the page.</p>'
    return personal + instruc

if __name__ == '__main__':
    app.run(debug=True)
