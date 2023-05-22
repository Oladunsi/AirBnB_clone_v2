#!/usr/bin/python3
""" a Flask web application.

The application listens on 0.0.0.0, port 5000.
Routes:
    /: Displays 'Hello HBNB!'
    /hbnb: Display 'Hello HBNB!'

    hello_world: is function that returns Hello HBNB
    home: is function that returns HBNB
    loving_c: is function that returns C and sometext
    loving_py: is function that returns Python and sometext
    num_route: is function that return a number and sometext
    num_template: is function that renders a page base on numeric path
"""

from flask import Flask
from flask import render_template


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_world():
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def home():
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def loving_c(text):
    return "C {}".format(text.replace("_", " "))


@app.route("/python/", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def loving_py(text="is cool"):
    return "Python {}".format(text.replace("_", " "))


@app.route("/number/<int:n>", strict_slashes=False)
def num_route(n):
    return "{} is a number".format(n)


@app.route("/number_template/<int:n>", strict_slashes=False)
def num_template(n):
    return render_template("5-number.html", n=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
