from flask import render_template, request
from models.event import *
from models.events_list import * 
from app import app

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/events/')
def events_page():
    return render_template('events.html', events=events)

@app.route('/events/<int:event_index>')
def event(event_index):
    current_event = find_event(event_index)
    return render_template('event.html', event=current_event)

@app.route('/events/new/')
def new_event():
    return render_template('new_event.html')

@app.route('/events/', methods=['POST'])
def save_event():
    form_data = request.form
    event_date = form_data["event_date"]
    event_name = form_data["event_name"]
    event_guest = form_data["event_guests"]
    event_location = form_data["event_location"]
    event_description = form_data["event_description"]
    event_recurring = form_data['event_recurring']

    new_event = Event(event_date, event_name, event_guest, event_location, event_description, event_recurring)
    add_event(new_event)

    return render_template('events.html', events=events)
