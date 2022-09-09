from flask import Flask
app = Flask(__name__)

def make_bold(func):
    def wrapper(*args, **kwargs):
        return f'<b><em><strong>{func(*args, **kwargs)}</strong></em></b>'
    return wrapper

@app.route('/')
@make_bold
def hello_world():
    return '<p>MAIN PAGE</p>' \
           '<img src="https://flask.palletsprojects.com/en/1.1.x/_static/flask-icon.png">'

@app.route('/bye')
def bye():
    return 'Bye!'

@app.route('/<name>/<int:val>')
def username(name,val):
    return f'Hello, {name} {val}'

if __name__=='__main__':
    app.run(debug=True)