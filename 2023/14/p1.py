def p(lines):
    for line in lines:
        print(''.join(line))

def Up(lines):
    for x in range(len(lines[0])):
        for y in range(1,len(lines)):
            i,j = x,y
            while lines[j][i] == 'O' and lines[j-1][i] == '.'and j > 0:
                lines[j][i] = '.'
                lines[j-1][i] = 'O'
                j -= 1
    return lines

with open('2023/14/input.txt') as file:
    lines = [[c for c in x.strip()] for x in file.readlines()]

p(lines)
lines = Up(lines)

load = 0

for i in range(len(lines),0,-1):
    load += i * lines[len(lines)-i].count('O')


print()
p(lines)

print(load)