# Event anouncement
events = []
def add_event(event_name, time="not decide"):
    event = {
        "Name": event_name,
        "Time": time
    }
    events.append(event)

def show_events(events):
    return events


while True:
    start = input("Add the upcoming events now !!!(q to quit)")
    
    

    if start.lower() == "q":
        break



    event_name = input("Enter the event's name: ")
    time_input = input("Enter the time: ")
    

    if time_input:
        time = time_input
    else:
        time = "not decide"


    add_event(event_name, time)

print("Event list")
for i, event in enumerate(events, 1):
    print(f"{i}. Name: {event['Name']} | Time: {event['Time']}")
    


    

