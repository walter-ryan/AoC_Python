with open('2024/04/input.txt') as file:
    lines = file.readlines()

widthRange = range(len(lines[0].strip()))
heightRange = range(len(lines))
xmasCount = 0
# Find X
for x in widthRange:
    for y in heightRange:
        if lines[y][x] == 'X':
            i, j = x, y
            # test up
            if i in heightRange and j - 1 in widthRange and lines[j-1][i] == 'M':
                if i in heightRange and j - 2 in widthRange and lines[j-2][i] == 'A':
                    if i in heightRange and j - 3 in widthRange and lines[j-3][i] == 'S':
                        xmasCount += 1
            # test down
            if i in heightRange and j + 1 in widthRange and lines[j+1][i] == 'M':
                if i in heightRange and j + 2 in widthRange and lines[j+2][i] == 'A':
                    if i in heightRange and j + 3 in widthRange and lines[j+3][i] == 'S':
                        xmasCount += 1
            # test right
            if i + 1 in heightRange and j in widthRange and lines[j][i+1] == 'M':
                if i + 2 in heightRange and j in widthRange and lines[j][i+2] == 'A':
                    if i + 3 in heightRange and j in widthRange and lines[j][i+3] == 'S':
                        xmasCount += 1
            # test right
            if i - 1 in heightRange and j in widthRange and lines[j][i-1] == 'M':
                if i - 2 in heightRange and j in widthRange and lines[j][i-2] == 'A':
                    if i - 3 in heightRange and j in widthRange and lines[j][i-3] == 'S':
                        xmasCount += 1
            # test upright
            if i + 1 in heightRange and j - 1 in widthRange and lines[j-1][i+1] == 'M':
                if i + 2 in heightRange and j - 2 in widthRange and lines[j-2][i+2] == 'A':
                    if i + 3 in heightRange and j - 3 in widthRange and lines[j-3][i+3] == 'S':
                        xmasCount += 1
            # test downright
            if i + 1 in heightRange and j + 1 in widthRange and lines[j+1][i+1] == 'M':
                if i + 2 in heightRange and j + 2 in widthRange and lines[j+2][i+2] == 'A':
                    if i + 3 in heightRange and j + 3 in widthRange and lines[j+3][i+3] == 'S':
                        xmasCount += 1
            # test upleft
            if i - 1 in heightRange and j - 1 in widthRange and lines[j-1][i-1] == 'M':
                if i - 2 in heightRange and j - 2 in widthRange and lines[j-2][i-2] == 'A':
                    if i - 3 in heightRange and j - 3 in widthRange and lines[j-3][i-3] == 'S':
                        xmasCount += 1
            # test downleft
            if i - 1 in heightRange and j + 1 in widthRange and lines[j+1][i-1] == 'M':
                if i - 2 in heightRange and j + 2 in widthRange and lines[j+2][i-2] == 'A':
                    if i - 3 in heightRange and j + 3 in widthRange and lines[j+3][i-3] == 'S':
                        xmasCount += 1
print(xmasCount)