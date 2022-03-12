from flask import Flask
import random

app = Flask(__name__)

random_number = random.randint(0, 9)
print(random_number)


@app.route('/')
def hello_world():
    return '<h1> Choose a number from 0 to 9 </h1>' \
           '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif">'


@app.route('/<int:number>')
def hello_flask(number):
    if number > random_number:
        return "<h1 style='color: purple'>Number too high</h1>" \
               "<img src='https://media.giphy.com/media/V3Z76ctCO3jG0/giphy.gif'>"
    elif number < random_number:
        return "<h1 style='color: red'>Number too low</h1>" \
               "<img src='https://media.giphy.com/media/ZFFVNwIbjsKtP3lHYK/giphy.gif'>"
    else:
        return "<h1 style='color: green'>That's the number!</h1>" \
               "<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'>"


if __name__ == "__main__":
    app.run(debug=True)
