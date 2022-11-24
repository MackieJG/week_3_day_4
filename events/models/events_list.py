from models.event import Event
from datetime import datetime

event1 = Event("30:12:2022", "Birthday Party", 60, "Castle Manor", "Party for an 30th", False)
event2 = Event("04:10:2022", "Halloween Party", 25, "Claremont Rugby Club", "A fancy dress party for a family", False)
event3 = Event("03:02:2022", "Race Night", 100, "Blantyre Miners Welfare Club", "Fundraiser for the Blantyre Miners welfare fund", True)

events = [event1 , event2, event3]

def find_event(event_index):
    return events[event_index]

def add_event(event):
    events.append(event)