with open('./2015/01/input.txt','r') as file:
    line = file.read()

level = 0

for character in line:
    if character == "(":
        level += 1
    elif character == ")":
        level -= 1
print("Final level:", level)