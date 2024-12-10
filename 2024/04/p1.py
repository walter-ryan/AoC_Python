with open('2024/04/test.txt') as file:
    lines = file.readlines()

widthRange = range(len(lines[0].strip()))
heightRange = range(len(lines))
xmasCount = 0

def findMAS(xOff: int, yOff: int) -> bool:
    if i+xOff in heightRange and j+yOff in widthRange and lines[j+yOff][i+xOff] == 'M':
        if i+2*xOff in heightRange and j+2*yOff in widthRange and lines[j+2*yOff][i+2*xOff] == 'A':
            if i+3*xOff in heightRange and j+3*yOff in widthRange and lines[j+3*yOff][i+3*xOff] == 'S':
                return True
    return False
directions = [(-1,1), (0,1), (1,1), (-1,0), (1,0), (-1,-1), (0,-1), (1,-1)]
# Find X
for x in widthRange:
    for y in heightRange:
        if lines[y][x] == 'X':
            i, j = x, y
            # test up
            for (a,b) in directions:
                if findMAS(a,b):
                    xmasCount += 1
print(xmasCount)