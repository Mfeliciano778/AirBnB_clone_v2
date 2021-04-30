#!/usr/bin/python3
'''starts flask'''
from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City
app = Flask(__name__)


@app.teardown_appcontext
def teardown(self):
    '''closes session'''
    storage.close()


@app.route('/states', strict_slashes=False)
def states_display():
    '''states display'''
    allstate = storage.all(State)
    return render_template("9-states.html", allstate=allstate,
                           states_only=1)


@app.route('/states/<id>', strict_slashes=False)
def states_id(id=None):
    '''state_id display'''
    allstate = storage.all(State)
    allcities = storage.all(City)
    is_there = 0
    state = None
    for value in allstate.values():
        if value.id == id:
            is_there = 1
            state = value
    return render_template("9-states.html", allstate=allstate,
                           allcities=allcities, is_there=is_there,
                           state=state, states_only=0)

if __name__ == "__main__":
    app.run(host="0.0.0.0")
