from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/user/<username>')
def show_user_profile(username):
    return 'User %s' % username

@app.route('/cube/<int:number>')
def cube(number):
    return 'Number: %d, Cubed: %d' % (number, number**3)

@app.route('/fizzbuzz/<int:number>')
def fizzbuzz(number):

    r = str(number)

    if ((number % 3) == 0) & ((number % 5) == 0):
        r = 'FizzBuzz'
    elif (number % 3) == 0:
        r = 'Fizz'
    elif (number % 5) == 0:
        r = 'Buzz'

    return r

if __name__ == '__main__':
    app.debug = True
    app.run()
