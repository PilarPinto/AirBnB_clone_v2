#!/usr/bin/python3
from flask import Flask, escape, render_template
from models import storage

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def close_sess(error):
    ''''Closes the session'''
    storage.close()


@app.route('/hbnb')
def display_all_hbnb():
    '''display all the information'''
    states = storage.all('State')
    amenities = storage.all('Amenity')
    places = storage.all('Place')
    return render_template('100-hbnb.html', places=places,
                           amenities=amenities, states=states)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
