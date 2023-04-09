#!/usr/bin/python3
"""
Returns string upon request
"""
from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return "Hello HBNB!"


@app.route('/hbnb')
def hbnb():
    return "HBNB"


@app.route('/c/<text>')
def c_is_fun(text):
    return 'C ' + text.replace('_', ' ')


@app.route('/python/', defaults={'text': 'is cool'})
@app.route('/python/<text>')
def python_is_cool(text):
    return 'Python ' + text.replace('_', ' ')


@app.route('/number/<int:n>')
def if_n_is_number(n):
    if isinstance(n, int):
        return str(n) + ' is a number'


@app.route('/number_template/<int:n>')
def n_is_number_return_template(n):
    if isinstance(n, int):
        return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>')
def n_is_int_return_odd_or_even(n):
    if isinstance(n, int):
        return render_template('6-number_odd_or_even.html', n=n)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
