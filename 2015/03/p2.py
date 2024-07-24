# The next year, to speed up the process, Santa creates a robot version of himself, Robo-Santa, to deliver presents with him.

# Santa and Robo-Santa start at the same location (delivering two presents to the same starting house), then take turns moving based on instructions from the elf, who is eggnoggedly reading from the same script as the previous year.

# This year, how many houses receive at least one present?

# For example:

#     ^v delivers presents to 3 houses, because Santa goes north, and then Robo-Santa goes south.
#     ^>v< now delivers presents to 3 houses, and Santa and Robo-Santa end up back where they started.
#     ^v^v^v^v^v now delivers presents to 11 houses, with Santa going one direction and Robo-Santa going the other.

with open('./2015/03/input.txt','r') as file:
    line = file.read()

posSanta = (0,0)
posRobot = (0,0)
visited = {(0,0)}

def move(pos,dir):
    if dir == "^":
        return (pos[0],pos[1]+1)
    if dir == ">":
        return (pos[0]+1,pos[1])
    if dir == "v":
        return (pos[0],pos[1]-1)
    if dir == "<":
        return (pos[0]-1,pos[1])

for i in range(len(line)):
    if i % 2 == 0:
        posSanta = move(posSanta,line[i])
        visited.add(posSanta)
    else:
        posRobot = move(posRobot,line[i])
        visited.add(posRobot)

print("The number of visited houses is:", len(visited))