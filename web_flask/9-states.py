#!/usr/bin/python3
from flask import Flask, escape, render_template
from models import storage
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def close_sess(error):
    ''''Closes the session'''
    storage.close()


@app.route('/states')
def dis_states():
    '''display states list'''
    states = storage.all('State')
    return render_template('9-states.html', states=states)


@app.route('/states/<id>')
def dis_statesId(id):
    '''display states by id list'''
    states = storage.all('State')
    return render_template('9-states.html', id=id, states=states)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
