from flask import Flask

app = Flask(__name__)

# App metadata
APP_NAME = "A Calendar App"
APP_VERSION = "0.1"
APP_DESCRIPTION = "A basic calendar app"

@app.route("/")
def home():
    return "Flask is running!"
def mainCalendar():
    return "This is the basepage for the calendar. Content coming soon!"

if __name__ == "__main__":
    app.run(debug=True)