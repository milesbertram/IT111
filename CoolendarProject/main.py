import tkinter as tk
from calendar_classes import User, get_activity

# Create a default user
user = User("Hawen", "huyleln@email.com")


def add_event():
    """Read fields from the GUI and add a new event to the user's calendar."""
    title = title_entry.get()
    date = date_entry.get()
    time = time_entry.get()
    location = location_entry.get()
    description = description_entry.get()

    if not title or not date:
        result_label.config(text="Please enter at least a title and date.")
        return

    user.create_event(title, date, time, location, description)

    # Clear the input fields after adding
    for entry in [title_entry, date_entry, time_entry, location_entry, description_entry]:
        entry.delete(0, tk.END)

    result_label.config(text="✅ Event Added!")


def show_events():
    """Fetch and display all events in the result label."""
    events = user.view_my_events()  # Returns a list of formatted strings

    if not events:
        result_label.config(text="No events yet. Add one above!")
        return

    text = ""
    for event_str in events:
        text += event_str + "\n-----------------\n"

    result_label.config(text=text)


def suggest_activity():
    """Call the Bored API and display a suggested activity."""
    try:
        activity = get_activity()
        result_label.config(text="💡 Suggested Activity: " + activity)
    except Exception as e:
        result_label.config(text="Could not fetch activity. Check your connection.")


# --- Build the GUI window ---
window = tk.Tk()
window.title("Event Calendar App")
window.geometry("420x480")
window.configure(bg="#f0f4f8")

# Title header
tk.Label(window, text="📅 Event Calendar", font=("Helvetica", 16, "bold"), bg="#f0f4f8").pack(pady=10)

# Input fields
fields = [("Title", None), ("Date (MM/DD/YYYY)", None), ("Time (HH:MM)", None), ("Location", None), ("Description", None)]
entries = []

for label_text, _ in fields:
    tk.Label(window, text=label_text, bg="#f0f4f8", anchor="w").pack(fill="x", padx=30)
    entry = tk.Entry(window, width=40)
    entry.pack(padx=30, pady=2)
    entries.append(entry)

title_entry, date_entry, time_entry, location_entry, description_entry = entries

# Buttons
btn_frame = tk.Frame(window, bg="#f0f4f8")
btn_frame.pack(pady=10)

tk.Button(btn_frame, text="Add Event", command=add_event, bg="#4a90d9", fg="white", width=14).grid(row=0, column=0, padx=5)
tk.Button(btn_frame, text="View Events", command=show_events, bg="#5cb85c", fg="white", width=14).grid(row=0, column=1, padx=5)
tk.Button(btn_frame, text="Suggest Activity", command=suggest_activity, bg="#f0ad4e", fg="white", width=14).grid(row=0, column=2, padx=5)

# Result display
result_label = tk.Label(window, text="", bg="#f0f4f8", justify="left", wraplength=380, font=("Courier", 9))
result_label.pack(padx=20, pady=10)

window.mainloop()