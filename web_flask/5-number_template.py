#!/usr/bin/python3
'''starts flask'''
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_world():
    '''hello hbnb'''
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def start():
    '''hello hbnb'''
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def print_t(text):
    '''hello hbnb'''
    return "C {}".format(text.replace('_', ' '))


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def print_text(text='is cool'):
    '''hello hbnb'''
    return "Python {}".format(text.replace('_', ' '))


@app.route('/number/<int:n>', strict_slashes=False)
def is_num(n):
    '''hello hbnb'''
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def is_num_html(n):
    '''html hbnb'''
    return render_template('5-number.html', n=n)

if __name__ == "__main__":
    app.run(host="0.0.0.0")
