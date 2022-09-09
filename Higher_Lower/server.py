from flask import Flask
import random
app = Flask(__name__)

correct_num = random.randint(1, 10)
print(correct_num)

@app.route('/')
def hello_world():
    return '<h1>Guess A Number from 1-9</h1>' \
           '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif">'


@app.route('/<int:num>')
def ver_num(num):
    if num == correct_num:
        return '<h1 style="color: green">You found me!!</h1>' \
               '<img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif" width="200", height="200">'
    elif num < correct_num:
        return '<h1 style="color: red">Low!! Try again</h1>' \
               '<img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif" width="200", height="200">'
    elif num > correct_num:
        return '<h1 style="color: purple">High!! Try again</h1>' \
               '<img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif" width="200", height="200">'

if __name__=='__main__':
    app.run(debug=True)