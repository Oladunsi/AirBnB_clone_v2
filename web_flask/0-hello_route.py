#!/usr/bin/python3
""" a Flask web application.

The application listens on 0.0.0.0, port 5000.
Routes:
    /: Displays 'Hello HBNB!'
"""

from flask import Flask


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_world():
    return "Hello HBNB!"

@app.route("/HBNB", strict_slashes=False)
def hello_world2():
    return "Hello HBNB"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
