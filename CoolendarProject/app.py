from flask import Flask, render_template, jsonify, request
from calendar_classes import User

app = Flask(__name__)

# Simple in-memory user store for the demo web app.
web_user = User("Web User", "web@example.com")

# App metadata
APP_NAME = "A Calendar App"
APP_VERSION = "0.1"
APP_DESCRIPTION = "A basic calendar app"


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/api/events", methods=["GET"])
def get_events():
    return jsonify({"events": web_user.view_my_events_data()})


@app.route("/api/events", methods=["POST"])
def create_event():
    payload = request.get_json(silent=True) or {}

    title = (payload.get("title") or "").strip()
    date = (payload.get("date") or "").strip()
    time = (payload.get("time") or "").strip()
    location = (payload.get("location") or "").strip()
    description = (payload.get("description") or "").strip()

    if not title or not date:
        return jsonify({"error": "Title and date are required."}), 400

    web_user.create_event(title, date, time, location, description)
    return jsonify({"message": "Event created.", "events": web_user.view_my_events_data()}), 201


@app.route("/api/events/<int:index>", methods=["DELETE"])
def delete_event(index):
    try:
        web_user.delete_event_by_index(index)
    except IndexError:
        return jsonify({"error": "Event not found."}), 404

    return jsonify({"message": "Event deleted.", "events": web_user.view_my_events_data()})


if __name__ == "__main__":
    app.run(debug=True)