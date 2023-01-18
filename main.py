# This algorithm uses optimal stopping theory to find matches and checks if the theory works by running it 1000 times
import random

def ost(freq, searchVal):
    counter = 0
    values = []
    turnPoint = int(0.37*freq)
    closest = -1
    found = -1
    while True:
        values.append(random.randint(0, 100))

        if closest == -1:
            closest = values[len(values) - 1]
        elif closest >= abs(searchVal - values[len(values) - 1]):
            closest = values[len(values) -1]

        counter += 1
        if turnPoint == counter:
            counter = 0
            break

    while True:
        values.append(random.randint(0, 100))

        if closest >= abs(searchVal - values[len(values) - 1]):
             found = values[len(values) - 1]

        counter += 1
        if turnPoint == counter:
            break

    if found == -1:
        return ["not found"]
    else:
        return [found, closest, abs(closest - searchVal) - abs(found - searchVal)]


notFound = 0
found = 0
betterFound = 0
for i in range(1000):
    val = ost(30, 10)
    if val[0] == "not found":
        notFound += 1
    elif int(val[2]) >= 0:
        betterFound += 1
    else:
        found += 1

print("Number of times the algorithm didn't find any matches: ", notFound, "\nNumber of times the algorithm found a worse match: ", found, "\nNumber of times the algorithm found a better match: ", betterFound)