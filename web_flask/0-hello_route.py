#!/usr/bin/python3
'''hello hbnb'''
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_world():
    '''hello hbnb'''
    return 'Hello HBNB!'

if __name__ == "__main__":
    app.run(host="0.0.0.0")
