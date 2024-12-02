with open('2024/02/input.txt') as file:
    lines = file.readlines()

safes = 0

for line in lines:
    line = [int(n) for n in line.split()]
    diffs = []
    for n in range(len(line)-1):
        diffs.append(line[n] - line[(n+1)])
    if min(diffs) >= 1 and max(diffs) <= 3:
        safes += 1
        print('a')
        print(line)
        print(diffs)
    elif min(diffs) >= -3 and max(diffs) <= -1:
        safes += 1
        print('b')
        print(line)
        print(diffs)

print(safes)