# --- Day 9: All in a Single Night ---


with open("./2015/09/test.txt") as file:
    lines = [line.strip() for line in file.readlines()]

distances = dict()
for line in lines:
    a = line.split()
    distances[(a[0], a[2])] = int(a[-1])
    distances[(a[2], a[0])] = int(a[-1])

print(distances)

