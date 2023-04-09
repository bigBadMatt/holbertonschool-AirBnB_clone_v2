#!/usr/bin/python3
"""
Returns string upon request
"""
from flask import Flask, request

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


@app.route('/number/<n>')
def if_n_is_number(n):
    if isinstance(n, int):
        return str(n) + ' is a number'

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
