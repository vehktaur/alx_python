"""
module documentation for task 2 file
"""

from flask import Flask
from markupsafe import escape

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def index():
    """
    mandatory docs
    """
    return "Hello HBNB"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """
    mandatory docs
    """
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def ctext(text):
    """
    mandatory docs
    """
    text = text.replace("_"," ")
    return f"C {escape(text)}"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
