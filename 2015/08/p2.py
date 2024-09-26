# --- Day 8: Matchsticks ---

with open("./2015/08/input.txt") as file:
    lines = [line.strip() for line in file.readlines()]

tot_str = 0 
tot_cha = 0
for line in lines:
    tot_cha += len(line)
    s = 6
    i = 1
    while i < len(line) - 1:
        s += 1
        if line[i] in ['\\','"']:
            s+= 1
        i += 1
    tot_str += s


print(f'{tot_str} - {tot_cha} = {tot_str - tot_cha}')