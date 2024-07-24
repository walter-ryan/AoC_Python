with open('./2015/01/input.txt','r') as file:
    line = file.read()


level = 0
pos = 0

for character in line:
    if level == -1:
        print("Level -1 reached at position:", pos)
        break
    if character == "(":
        level += 1
    elif character == ")":
        level -= 1
    pos += 1