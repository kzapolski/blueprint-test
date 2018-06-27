#!/usr/bin/python

from flask import Flask
from foo import foo

app = Flask(__name__)
app.register_blueprint(foo)


@app.route("/")
def index():
    return "This is the main page"


if __name__ == '__main__':
    app.run(debug=True)
