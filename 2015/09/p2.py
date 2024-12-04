# --- Day 9: All in a Single Night ---
import itertools

with open("2015/09/input.txt") as file:
    lines = [line.strip() for line in file.readlines()]

distances = dict()
for line in lines:
    a = line.split()
    distances[(a[0], a[2])] = int(a[-1])
    distances[(a[2], a[0])] = int(a[-1])


locations = set()
for pair in distances.keys():
    locations.add(pair[0])
    locations.add(pair[1])

possibleRoutes = list(itertools.permutations(locations))
print('Total possible routes:', len(possibleRoutes))

longestDistance = 0

for route in possibleRoutes:
    distance = 0
    visited = 0
    while visited < len(route) - 1:
        distance += distances[route[visited:visited+2]]
        visited += 1
    if distance > longestDistance:
        longestDistance = distance
        longestRoute = route
print(longestDistance)
print(longestRoute)