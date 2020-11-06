"""
Find the trip length. Cow Bessie follows Farmer
John’s instructions to the field, e.g. N( North 1 mile) E (
East 3miles) S (South 3 miles) , but when she comes
back, Bessie takes a shortcut in a direct line from the field to
the farm. Find the length of the back trip.
e.g.
N 1
E 3
S 3
N 3
"""

import math

distances = {
    "N" : 0,
    "S" : 0,
    "E" : 0,
    "W" : 0
}

def get_trip_data():
    with open("trip.txt", 'r') as f:
        for line in f:
            parts = line.split()
            if len(parts) != 2:
                raise ValueError("Was expecting two parts, but got {} from line {}".format(str(len(parts)), line))
            elif parts[0] not in distances.keys():
                raise ValueError("Was expecting one of {}, but got {} from line {}".format(distances.keys(), parts[0], line))
            elif parts[1].isdigit() is False:
                raise ValueError("Was expecting an integer, but got {} from line {}".format(parts[1], line))
            else:
                distances[parts[0]] += int(parts[1])

def calculate_shortcut():
    NS = distances["N"] - distances["S"]
    EW = distances["E"] - distances["W"]
    return math.sqrt(NS**2 + EW**2)

get_trip_data()
print(calculate_shortcut())