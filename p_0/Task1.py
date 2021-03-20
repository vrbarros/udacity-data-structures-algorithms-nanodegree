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
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""

# sets are a mutable collection of distinct (unique) immutable values that are unordered.
unique_numbers = set()


def save(obj):
    # add first number
    unique_numbers.add(obj[0])
    # add second number
    unique_numbers.add(obj[1])


for text in texts:
    save(text)

for call in calls:
    save(call)

print(
    "There are {} different telephone numbers in the records.".format(
        len(unique_numbers)
    )
)
