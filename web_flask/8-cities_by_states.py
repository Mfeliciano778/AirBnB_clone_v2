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


@app.route('/cities_by_states', strict_slashes=False)
def html_display():
    allstate = storage.all(State)
    allcities = storage.all(City)
    return render_template("8-cities_by_states.html", allstate=allstate,
                            allcities=allcities)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
