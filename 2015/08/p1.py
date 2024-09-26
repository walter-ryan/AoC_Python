# --- Day 8: Matchsticks ---

import re

with open("./2015/08/input.txt") as file:
    lines = [line.strip() for line in file.readlines()]

tot_str = 0 
tot_cha = 0
for line in lines:
    print(line)
    print("Code: ", len(line))
    tot_cha += len(line)
    s = 0
    i = 1
    while i < len(line) - 1:
        s += 1
        if line[i] == '\\':
            if line[i+1] in ['\\','"']:
                i += 1
            elif  i + 4 < len(line) and re.search(r"\\x[0-9a-fA-F]{2}", line[i:i+4]):
                i += 3
        i += 1
    print("Str: ", s)
    tot_str += s


print(f'{tot_cha} - {tot_str} = {tot_cha - tot_str}')