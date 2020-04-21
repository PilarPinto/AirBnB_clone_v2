#!/usr/bin/python3
from flask import Flask, escape
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello_flask():
    return 'Hello HBNB!'


@app.route('/hbnb')
def display_hbnb():
    return "HBNB"


@app.route('/c/<text>')
def display_cisfun(text):
    return 'C %s' % escape(text.replace('_', ' '))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
