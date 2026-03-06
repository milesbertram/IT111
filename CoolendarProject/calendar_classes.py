import requests

class Event:
    def __init__(self, title, date, time, location, description):
        self.title = title
        self.date = date
        self.time = time
        self.location = location
        self.description = description

    def display_event(self):
        """Returns a formatted string describing the event."""
        return (
            f"Title: {self.title}\n"
            f"Date: {self.date}\n"
            f"Time: {self.time}\n"
            f"Location: {self.location}\n"
            f"Description: {self.description}"
        )

    def update_event(self, title=None, date=None, time=None, location=None, description=None):
        """Update one or more fields of the event."""
        if title:
            self.title = title
        if date:
            self.date = date
        if time:
            self.time = time
        if location:
            self.location = location
        if description:
            self.description = description


class Calendar:
    def __init__(self):
        self.events = []

    def add_event(self, event):
        self.events.append(event)

    def remove_event(self, event):
        self.events.remove(event)

    def get_events(self):
        """Returns a list of formatted event strings."""
        return [event.display_event() for event in self.events]


class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.calendar = Calendar()

    def create_event(self, title, date, time, location, description):
        event = Event(title, date, time, location, description)
        self.calendar.add_event(event)

    def delete_event(self, event):
        self.calendar.remove_event(event)

    def view_my_events(self):
        """Returns a list of formatted event strings for display."""
        return self.calendar.get_events()


# API function
def get_activity():
    """Fetches a random activity suggestion from the Bored API."""
    url = "https://randomfox.ca/floof"
    response = requests.get(url)
    data = response.json()
    return data["image"]