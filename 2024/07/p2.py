from itertools import product
from tqdm import tqdm

with open('2024/07/input.txt') as file:
    lines = file.readlines()

l = []
for line in lines:
    l.append((int(line.split(':')[0]),[int(x) for x in line.split()[1:]]))

def isSafe(line):
    for x in product('012', repeat=len(line[1])-1):
        sum = line[1][0]
        for i in range(len(line[1])-1):
            if x[i] == '0':
                sum += line[1][i+1]
            elif x[i] == '1':
                sum *= line[1][i+1]
            else:
                sum = int(str(sum) + str(line[1][i+1]))
            if sum > line[0]:
                continue
        if sum == line[0]:
            return line[0]
    return 0
safeSum = 0
for line in tqdm(l):
    safeSum += isSafe(line)

print(safeSum)
