#!/usr/bin/python3
""" a Flask web application.

The application listens on 0.0.0.0, port 5000.
Routes:
    /: Displays 'Hello HBNB!'
    /hbnb: Display 'Hello HBNB!'

    hello_world: is function that returns Hello HBNB
    home: is function that returns HBNB
    loving_c: is function that returns C and sometext
"""

from flask import Flask


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

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
