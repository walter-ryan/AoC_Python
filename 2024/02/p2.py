with open('2024/02/input.txt') as file:
    lines = file.readlines()

def normalSafe(diffs: list) -> bool:
    dMax = max(diffs)
    dMin = min(diffs)
    if (dMax <= 3 and dMin >= 1) or (dMax <= -1 and dMin >= -3):
        return True
    return False

def problemDampener(line: list) -> bool:
    for n in range(len(line)):
        diffs = []
        nLine = line[:n] + line[n+1:]
        for m in range(len(nLine)-1):
            diffs.append(nLine[m] - nLine[(m+1)])
        if normalSafe(diffs):
            return True
    return False


safes = 0

for line in lines:
    line = [int(n) for n in line.split()]
    diffs = []
    for n in range(len(line)-1):
        diffs.append(line[n] - line[(n+1)])
    if normalSafe(diffs):
        safes += 1
        print(line)
        print(diffs)
    elif problemDampener(line):
        safes += 1
        print('dampened')
        print(line)

print(safes)