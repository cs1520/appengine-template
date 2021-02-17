from flask import Flask


app = Flask(__name__)


app.route("/")
def home():
    """Return a simple HTML page."""
    return render_template("index.html")


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8080, debug=True) 