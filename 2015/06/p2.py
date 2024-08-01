# You just finish implementing your winning light pattern when you realize you mistranslated Santa's message from Ancient Nordic Elvish.

# The light grid you bought actually has individual brightness controls; each light can have a brightness of zero or more. The lights all start at zero.

# The phrase turn on actually means that you should increase the brightness of those lights by 1.

# The phrase turn off actually means that you should decrease the brightness of those lights by 1, to a minimum of zero.

# The phrase toggle actually means that you should increase the brightness of those lights by 2.

# What is the total brightness of all lights combined after following Santa's instructions?

# For example:

#     turn on 0,0 through 0,0 would increase the total brightness by 1.
#     toggle 0,0 through 999,999 would increase the total brightness by 2000000.




with open("./2015/06/input.txt") as file:
    lines = file.readlines()
    lines = [line.strip().split() for line in lines]

grid = [[0 for i in range(1000)] for j in range(1000)]

def toggle(start, end):
    for i in range(start[0],end[0]+1):
        for j in range(start[1],end[1]+1):
            grid[i][j] = grid[i][j] + 2

def turnOn(start, end):
    for i in range(start[0],end[0]+1):
        for j in range(start[1],end[1]+1):
            grid[i][j] = grid[i][j] + 1

def turnOff(start, end):
    for i in range(start[0],end[0]+1):
        for j in range(start[1],end[1]+1):
            if grid[i][j] > 0:
                grid[i][j] = grid[i][j] - 1

for line in lines:
    if line[0] == "toggle":
        start = [int(num) for num in line[1].split(",")]
        end = [int(num) for num in line[3].split(",")]
        toggle(start, end)
    elif line[1] == "on":
        start = [int(num) for num in line[2].split(",")]
        end = [int(num) for num in line[4].split(",")]
        turnOn(start, end)
    else:
        start = [int(num) for num in line[2].split(",")]
        end = [int(num) for num in line[4].split(",")]
        turnOff(start, end)


count = 0
for row in grid:
    for item in row:
        count += item

print("The total brightness is", count)