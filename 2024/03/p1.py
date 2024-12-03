import re

with open('2024/03/input.txt') as file:
    line = file.read()

list = [x[4:-1].split(',') for x in re.findall(r"mul\(\d+,\d+\)", line)]

tot = 0
for pair in list:
    tot += int(pair[0])*int(pair[1])
print(tot)
