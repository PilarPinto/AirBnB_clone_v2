#!/usr/bin/python3
from flask import Flask, escape, render_template
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


@app.route('/python/', defaults={'text': 'is cool'})
@app.route('/python/<text>')
def display_default(text):
    return 'Python %s' % escape(text.replace('_', ' '))


@app.route('/number/<int:n>')
def display_integer(n):
    return '%i is a number' % (n)


@app.route('/number_template/<int:n>')
def display_Template(n):
    '''display template from flask'''
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>')
def display_OddEven(n):
    '''display template from flask number is odd or even'''
    return render_template('6-number_odd_or_even.html', n=n)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
