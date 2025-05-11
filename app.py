from flask import Flask, render_template, request, redirect
import json

app = Flask(__name__)

# Function to load events from JSON
def load_events():
    try:
        with open("events.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

@app.route('/')
def index():
    events = load_events()  # Load events data
    return render_template("index.html", events=events)  # Pass events to template

@app.route('/get_ticket', methods=['POST'])
def get_ticket():
    email = request.form.get("email")
    event_url = request.form.get("event_url")
    print(f"User {email} wants to attend {event_url}")  # You can log or store this information
    return redirect(event_url)  # Redirect to event URL

if __name__ == '__main__':
    app.run(debug=True)
