"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv

with open("texts.csv", "r") as f:
    reader = csv.reader(f)
    texts = list(reader)

with open("calls.csv", "r") as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

stats = {}


def save(number, duration):
    if number in stats:
        stats[number] += duration
    else:
        stats[number] = duration


for exchange in calls:
    origin = exchange[0]
    destination = exchange[1]
    duration = int(exchange[3])

    save(origin, duration)
    save(destination, duration)

max_time_number = max(stats, key=lambda x: stats[x])
max_time_duration = stats[max_time_number]

print(
    "{} spent the longest time, {} seconds, on the phone during September 2016".format(
        max_time_number, max_time_duration
    )
)
