from flask import Flask, render_template, jsonify, request
from calendar_classes import User

app = Flask(__name__)

web_user = User("Web User", "web@example.com")


@app.route("/")
def home():
    return render_template("index.html")


# -----------------------
# Event routes
# -----------------------

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
    return jsonify({
        "message": "Event created.",
        "events": web_user.view_my_events_data()
    }), 201


@app.route("/api/events/<int:index>", methods=["DELETE"])
def delete_event(index):
    try:
        web_user.delete_event_by_index(index)
    except IndexError:
        return jsonify({"error": "Event not found."}), 404

    return jsonify({
        "message": "Event deleted.",
        "events": web_user.view_my_events_data()
    })


# -----------------------
# Task routes
# -----------------------

@app.route("/api/tasks", methods=["GET"])
def get_tasks():
    return jsonify({"tasks": web_user.view_my_tasks_data()})


@app.route("/api/tasks", methods=["POST"])
def create_task():
    payload = request.get_json(silent=True) or {}

    title = (payload.get("title") or "").strip()
    due_date = (payload.get("due_date") or "").strip()

    if not title:
        return jsonify({"error": "Task title is required."}), 400

    web_user.create_task(title, due_date)
    return jsonify({
        "message": "Task created.",
        "tasks": web_user.view_my_tasks_data()
    }), 201


@app.route("/api/tasks/<int:index>", methods=["DELETE"])
def delete_task(index):
    try:
        web_user.delete_task_by_index(index)
    except IndexError:
        return jsonify({"error": "Task not found."}), 404

    return jsonify({
        "message": "Task deleted.",
        "tasks": web_user.view_my_tasks_data()
    })


@app.route("/api/tasks/<int:index>/complete", methods=["PATCH"])
def complete_task(index):
    try:
        web_user.complete_task_by_index(index)
    except IndexError:
        return jsonify({"error": "Task not found."}), 404

    return jsonify({
        "message": "Task completed.",
        "tasks": web_user.view_my_tasks_data()
    })


if __name__ == "__main__":
    app.run(debug=True)