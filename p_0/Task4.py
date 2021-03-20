"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open("texts.csv", "r") as f:
    reader = csv.reader(f)
    texts = list(reader)

with open("calls.csv", "r") as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

outgoing_calls = set()
outgoing_texts = set()
incoming_calls = set()
incoming_texts = set()


def save_calls(origin=None, destination=None):
    outgoing_calls.add(origin)
    incoming_calls.add(destination)


def save_texts(origin=None, destination=None):
    outgoing_texts.add(origin)
    incoming_texts.add(destination)


for call in calls:
    save_calls(origin=call[0], destination=call[1])
for text in texts:
    save_texts(origin=text[0], destination=text[1])

# these are numbers that make outgoing calls but never send texts,
# receive texts or receive incoming calls.
telemarketers_numbers = sorted(
    outgoing_calls - (incoming_calls | outgoing_texts | incoming_texts)
)

print("These numbers could be telemarketers:")
print(", ".join(telemarketers_numbers))
