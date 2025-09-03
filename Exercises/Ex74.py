def event_anounce(event_name, time = "not decide"):
    return event_name, time

event_name = input()
time_input = input()
if time_input:
    time = time_input
else:
    time = "not decide"

print(event_anounce(event_name, time))

