from flask import Flask, render_template, jsonify
from calendar_classes import get_activity

app = Flask(__name__)

# App metadata
APP_NAME = "A Calendar App"
APP_VERSION = "0.1"
APP_DESCRIPTION = "A basic calendar app"


@app.route("/")
def home():
    return render_template("index.html")


# API route
@app.route("/api/activity")
def activity():
    activity = get_activity()
    return jsonify({"activity": activity})


if __name__ == "__main__":
    app.run(debug=True)