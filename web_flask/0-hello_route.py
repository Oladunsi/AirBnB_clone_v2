#!/usr/bin/python3
# creating an airbnb web clone using flask

from flask import Flask


app = Flask(__name__)

app.route("/")
def hello_world():
    return "Hello HBNB!$")
