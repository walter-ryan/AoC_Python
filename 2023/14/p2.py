from functools import cache

def p(lines):
    for line in lines:
        print(''.join(line))

def Up(lines):
    for x in range(len(lines[0])):
        for y in range(1,len(lines)):
            i,j = x,y
            while j > 0 and lines[j][i] == 'O' and lines[j-1][i] == '.':
                lines[j][i] = '.'
                lines[j-1][i] = 'O'
                j -= 1
    return lines

def Right(lines):
    for x in range(len(lines[0])-2, -1, -1):
        for y in range(len(lines)):
            i,j = x,y
            while i < len(lines[0])-1 and lines[j][i] == 'O' and lines[j][i+1] == '.':
                lines[j][i] = '.'
                lines[j][i+1] = 'O'
                i += 1
    return lines
def Down(lines):
    for x in range(len(lines[0])):
        for y in range(len(lines)-2, -1, -1):
            i,j = x,y
            while j < len(lines[0])-1 and lines[j][i] == 'O' and lines[j+1][i] == '.':
                lines[j][i] = '.'
                lines[j+1][i] = 'O'
                j += 1
    return lines

def Left(lines):
    for x in range(1,len(lines[0])):
        for y in range(len(lines)):
            i,j = x,y
            while i > 0  and lines[j][i] == 'O' and lines[j][i-1] == '.':
                lines[j][i] = '.'
                lines[j][i-1] = 'O'
                i -= 1
    return lines

@cache
def Spin(lines):
    lines = Up(lines)
    lines = Left(lines)
    lines = Down(lines)
    lines = Right(lines)
    return lines

with open('2023/14/test.txt') as file:
    lines = [[c for c in x.strip()] for x in file.readlines()]

p(lines)

seen = dict()
for i in range(1,100001):
    lines = Spin(lines)
    if lines in seen.values():
        print('Seen already, current step:', i, 'seen at,', seen[lines])
        break
    else:
        seen[lines] = i


print()

p(lines)

load = 0

for i in range(len(lines),0,-1):
    load += i * lines[len(lines)-i].count('O')

print(load)