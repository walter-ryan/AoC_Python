with open('2024/04/input.txt') as file:
    lines = file.readlines()

widthRange = range(len(lines[0].strip()))
heightRange = range(len(lines))
print(widthRange)
print(heightRange)
xmasCount = 0
# Find X
for x in widthRange:
    for y in heightRange:
        if lines[y][x] == 'A':
            i, j = x, y
            print('Testing ',i,j)
            # test \ MAS
            if ((
                  i-1 in heightRange
                  and j + 1 in widthRange
                  and lines[j+1][i-1] == 'M'
                ) and (
                  i+1 in heightRange
                  and j - 1 in widthRange
                  and lines[j-1][i+1] == 'S'
                )) or ((
                  i-1 in heightRange
                  and j + 1 in widthRange
                  and lines[j+1][i-1] == 'S'
                ) and (
                  i+1 in heightRange
                  and j - 1 in widthRange
                  and lines[j-1][i+1] == 'M'
                )):
                if ((
                        i-1 in heightRange
                        and j - 1 in widthRange
                        and lines[j-1][i-1] == 'M'
                    ) and (
                        i+1 in heightRange
                        and j + 1 in widthRange
                        and lines[j+1][i+1] == 'S'
                    )) or ((
                        i-1 in heightRange
                        and j - 1 in widthRange
                        and lines[j-1][i-1] == 'S'
                    ) and (
                        i+1 in heightRange
                        and j + 1 in widthRange
                        and lines[j+1][i+1] == 'M'
                    )):
                    xmasCount += 1

print(xmasCount)