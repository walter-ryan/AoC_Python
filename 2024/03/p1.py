import re

with open('2024/03/input.txt') as file:
    line = file.read()

list = [x[4:-1] for x in re.findall(r"mul\(\d+,\d+\)", line)]

tot = 0
for pair in list:
    t = [int(a) for a in pair.split(',')]
    tot += t[0]*t[1]
print(tot)