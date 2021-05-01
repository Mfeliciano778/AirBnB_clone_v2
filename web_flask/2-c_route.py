#!/usr/bin/python3
'''starts flask'''
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_world():
    '''hello hbnb'''
    return 'Hello HBNB!'


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    '''hello hbnb'''
    return 'C {}'.format(text.replace('_', ' '))


@app.route('/hbnb', strict_slashes=False)
def start():
    '''hello hbnb'''
    return 'HBNB'

if __name__ == "__main__":
    app.run(host="0.0.0.0")
