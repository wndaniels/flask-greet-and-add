from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)


@app.route("/add")
def add_math():
    """Add a and b."""

    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = add(a, b)

    return str(result)


@app.route("/sub")
def sub_math():
    """Subtract b from a."""

    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = sub(b, a)

    return str(result)


@app.route("/mult")
def mult_math():
    """Multiply a and b."""

    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = mult(a, b)

    return str(result)


@app.route("/div")
def div_math():
    """Divide a and b."""

    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = div(a, b)

    return str(result)


operators = {
    "add": add,
    "sub": sub,
    "mult": mult,
    "div": div,
}


@app.route("/math/<operator>")
def any_math(operator):
    """Do the math of any operator on a and b."""

    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = operators[operator](a, b)

    return str(result)
