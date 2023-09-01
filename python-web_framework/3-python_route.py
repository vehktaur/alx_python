"""
mandatory module documentation
"""

from flask import Flask
from markupsafe import escape

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def index():
    """
    mandatory function docs
    """
    return "Hello HBNB"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """
    mandatory function docs
    """
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def ctext(text):
    """
    mandatory function docs
    """
    return f"C {escape(text)}"


@app.route('/python/', strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_text(text="is cool"):
    """
    mandatory function docs
    """
    text = text.replace("_", " ")
    return f"Python {escape(text)}"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
