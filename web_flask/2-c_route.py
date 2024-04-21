#!/usr/bin/python3
"""RUN AN APP with flask"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """ Function that return Hello HBNB """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbhb():
    """ Function that returns HBNB"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def hello_c(text):
    """Function that returns about c"""
    message = text.replace('_', ' ')
    return f"C {message}"


if __name__ == "__main__":
    app.run(debug=True, port=5000)
