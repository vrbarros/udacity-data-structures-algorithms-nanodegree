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
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""

import re
from functools import reduce

# (080) is the area code for fixed line telephones in Bangalore
bangalore_list = list(filter(lambda x: x[0][:5] == "(080)", calls))

stats = {}

for call in bangalore_list:
    # Fixed lines start with an area code enclosed in brackets. The area
    # codes vary in length but always begin with 0.
    destination = call[1]

    if destination[0] == "(":
        input = re.match(r"\(([0-9]+)\)", destination).group(0)[1:-1]

        if input in stats:
            stats[input] += 1
        else:
            stats[input] = 1

    # Telemarketers' numbers have no parentheses or space,
    # but they start with the area code 140.
    elif destination[:3] == "140":
        if "140" in stats:
            stats["140"] += 1
        else:
            stats["140"] = 1
    # Mobile numbers have no parentheses, but have a space in the middle
    # of the number to help readability. The prefix of a mobile number
    # is its first four digits, and they always start with 7, 8 or 9.
    else:
        if destination[:4] in stats:
            stats[destination[:4]] += 1
        else:
            stats[destination[:4]] = 1

codes = ", ".join(sorted(stats.keys()))
print("The numbers called by people in Bangalore have codes:")
print(codes)

only_fixed_lines = stats["080"]

all_lines = reduce(lambda acc, current: acc + current, stats.values(), 0)

percent_of_calls = round(only_fixed_lines * 100 / all_lines, 2)

print(
    "{}% percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.".format(
        percent_of_calls
    )
)
