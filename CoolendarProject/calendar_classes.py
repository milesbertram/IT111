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

    def to_dict(self):
        """Return event data in a JSON-serializable form."""
        return {
            "title": self.title,
            "date": self.date,
            "time": self.time,
            "location": self.location,
            "description": self.description,
        }


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

    def get_event_dicts(self):
        """Return all events as a list of dictionaries."""
        return [event.to_dict() for event in self.events]

    def remove_event_by_index(self, index):
        """Remove an event by its position in the list."""
        if index < 0 or index >= len(self.events):
            raise IndexError("Event index out of range")
        self.events.pop(index)


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

    def delete_event_by_index(self, index):
        self.calendar.remove_event_by_index(index)

    def view_my_events(self):
        """Returns a list of formatted event strings for display."""
        return self.calendar.get_events()

    def view_my_events_data(self):
        """Returns events in dictionary format for API responses."""
        return self.calendar.get_event_dicts()