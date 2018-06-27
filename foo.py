from flask import Blueprint

foo = Blueprint('foo', __name__, url_prefix="/foo")


@foo.route("/")
def index():
    return "The root of foo"


@foo.route("/bar")
def users():
    return "Hello there!"

