import re

with open('2024/05/input.txt') as file:
    lines = [line.strip() for line in file.readlines()]


print(lines)

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

for pages in lists:
    pageIsSafe = True
    for i in range(len(pages)):
        if pages[i] in rules.keys() and any([num in pages[:i] for num in rules[pages[i]]]):
            pageIsSafe = False
            break
    if pageIsSafe:
        sumOfSafe += int(pages[len(pages)//2])
        print('this one is good:', pages)
        
print(sumOfSafe)