with open('2024/01/input.txt') as file:
    lines = file.readlines()

list1 = []
list2 = []

for line in lines:
    a,b = line.split()
    list1.append(int(a))
    list2.append(int(b))

list1.sort()
list2.sort()
occurences = dict()

for n in list2:
    if n in occurences.keys():
        occurences[n] += 1
    else: 
        occurences[n] = 1

tot = 0

for n in list1:
    if n in occurences.keys():
        tot += n * occurences[n]    

print(tot)