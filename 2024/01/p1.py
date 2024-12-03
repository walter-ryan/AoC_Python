with open('2024/01/input.txt') as file:
    lines = file.readlines()

list1 = []
list2 = []
diff = []

for line in lines:
    a,b = line.split()
    list1.append(int(a))
    list2.append(int(b))

list1.sort()
list2.sort()

for i in range(len(list1)):
    diff.append(abs(list1[i] - list2[i]))
print(sum(diff))