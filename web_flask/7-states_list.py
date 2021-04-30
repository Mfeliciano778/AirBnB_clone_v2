#!/usr/bin/python3
'''starts flask'''
from flask import Flask, render_template
from models import storage
from models.state import State
app = Flask(__name__)


@app.teardown_appcontext
def close_session(self):
    '''closes session'''
    storage.close()


@app.route('/states_list', strict_slashes=False)
def html_display():
    allstate = storage.all(State)
    return render_template('7-states_list.html', allstate=allstate)

if __name__ == "__main__":
    app.run(host="0.0.0.0")