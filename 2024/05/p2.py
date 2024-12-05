import re

with open('2024/05/input.txt') as file:
    lines = [line.strip() for line in file.readlines()]


# print(lines)

rules = dict()

lists = []

for line in lines:
    if re.match(r"\d+\|\d+",line):
        a,b = line.split('|')
        if a in rules.keys():
            rules[a].append(b)
        else:
            rules[a] = [b]
    elif line == '':
        continue
    else:
        lists.append(line.split(','))

# print(rules)
# print(lists)
sumOfSafe = 0
unsafes = []
def isSafe(pages):
    for i in range(len(pages)):
        if pages[i] in rules.keys() and any([num in pages[:i] for num in rules[pages[i]]]):
            return False
    return True


for pages in lists:
    if not isSafe(pages):
        unsafes.append(pages)
        
print(unsafes)

def customSort(pages: list) -> list:
    newList = pages
    for i in range(len(pages)-1):

        if newList[i+1] in rules.keys() and newList[i] in rules[newList[i+1]]:
            newList[i], newList[i+1] = newList[i+1], newList[i]
    return newList

corrected = []
for pages in unsafes:
    while not isSafe(pages):
        pages = customSort(pages)
    corrected.append(pages)

tot = 0
for pages in corrected:
    tot += int(pages[len(pages)//2])

print(corrected)

print(tot)