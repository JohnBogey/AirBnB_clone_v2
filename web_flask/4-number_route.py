#!/usr/bin/python3
''' starts flask app and runs routes '''

from flask import Flask
app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello_world():
    ''' simple hello world '''
    return 'Hello, HBNB!'

@app.route('/hbnb', strict_slashes=False)
def print_HBNB():
    ''' prints HBNB '''
    return 'HBNB'

@app.route('/c/<text>', strict_slashes=False)
def print_c(text):
    ''' prints c/text '''
    return 'C ' + '%s' % text.replace('_', ' ')

@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def print_python(text = 'is cool'):
    ''' prints python/text '''
    return 'Python ' + '%s' % text.replace('_', ' ')

@app.route('/number/<int:n>', strict_slashes=False)
def print_num(n):
    ''' prints if n is a num '''
    return '{} is a number'.format(n)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
