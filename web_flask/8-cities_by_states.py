#!/usr/bin/python3
from flask import Flask, escape, render_template
from models import storage
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def close_sess(error):
    ''''Closes the session'''
    storage.close()


@app.route('/cities_by_states')
def diplay_cities():
    '''display cities list'''
    states = storage.all('State')
    return render_template('8-cities_by_states.html', states=states)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
