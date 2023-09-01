"""Module documentation"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """Display a greeting message."""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Display 'HBNB'."""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_route(text):
    """Display 'C' followed by the value of the text variable."""
    return f"C {text.replace('_', ' ')}"


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_route(text="is cool"):
    """Display 'Python' followed by the value of the text variable (default is 'is cool')."""
    return f"Python {text.replace('_', ' ')}"


@app.route('/number/<int:n>', strict_slashes=False)
def number_route(n):
    """Display whether n is a number or not."""
    if isinstance(n, int):
        return f"{n} is a number"
    else:
        return "Invalid input."


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """Render an HTML template to display 'Number: n'."""
    if isinstance(n, int):
        return render_template('5-number.html', number=n)
    else:
        return "Invalid input."


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    """Render an HTML template to display 'Number: n'."""
    chance = "odd"
    if n % 2 == 0:
        chance = "even"
    if isinstance(n, int):
        return render_template('6-number_odd_or_even.html', number=n, chance=chance)
    else:
        return "Invalid input."


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
