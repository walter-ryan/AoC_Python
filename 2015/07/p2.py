# --- Part Two ---

# Now, take the signal you got on wire a, override wire b to that signal, and reset the other wires (including wire a). What new signal is ultimately provided to wire a?

with open("./2015/07/input.txt") as file:
    lines = [line.strip() for line in file.readlines()]


store = {}

commands = []

for line in lines:
    line = line.split(" -> ")
    line[0] = [int(x) if x[0].isdigit() else x for x in line[0].split()]
    
    commands.append(line)
commands.sort(key=len)
count = 0
while commands:
    line = commands.pop(0)
    dest = line[1]
    com = line[0]
    print(line)
    if len(com) == 1:
        # Deal with SET
        if isinstance(com[0],int):
            store[dest] = com[0]
        elif com[0] in store.keys():
            store[dest] = store.get(com[0])
        else:
            commands.append(line)
    elif len(com) == 2:
        # Deal with NOT
        if com[1][0].isdigit():
            store[dest] = ~com[1] & 65535
        elif com[1] in store.keys():
            store[dest] = ~store[com[1]] & 65535
        else:
            print("line incomplete")
            commands.append(line)
    else:
        # Deal with AND OR LSHIFT RSHIFT
        if isinstance(com[0],int):
            a = com[0]
        elif com[0] in store.keys():
            a = store.get(com[0])
        else:
            a = "no num"
        if isinstance(com[2],int):
            b = com[2]
        elif com[2] in store.keys():
            b = store.get(com[2])
        else:
            b = "no num"
        # print(a, " and ",b)
        if isinstance(a,int) and isinstance(b,int):
            if com[1] == "AND":
                store[dest] = a & b
            elif com[1] == "OR":
                store[dest] = a | b
            elif com[1] == "LSHIFT":
                store[dest] = a << b
            else:
                store[dest] = a >> b
        else:
            print("line incomplete")
            commands.append(line)
    # print(store)
    count += 1
    if "a" in store.keys() or count > 100000:
        break

print("A:",store["a"])

partA = store["a"]
store = {}
for line in lines:
    line = line.split(" -> ")
    line[0] = [int(x) if x[0].isdigit() else x for x in line[0].split()]
    
    commands.append(line)
commands.sort(key=len)
count = 0
while commands:
    store["b"] = partA
    line = commands.pop(0)
    dest = line[1]
    com = line[0]
    print(line)
    if len(com) == 1:
        # Deal with SET
        if isinstance(com[0],int):
            store[dest] = com[0]
        elif com[0] in store.keys():
            store[dest] = store.get(com[0])
        else:
            commands.append(line)
    elif len(com) == 2:
        # Deal with NOT
        if com[1][0].isdigit():
            store[dest] = ~com[1] & 65535
        elif com[1] in store.keys():
            store[dest] = ~store[com[1]] & 65535
        else:
            print("line incomplete")
            commands.append(line)
    else:
        # Deal with AND OR LSHIFT RSHIFT
        if isinstance(com[0],int):
            a = com[0]
        elif com[0] in store.keys():
            a = store.get(com[0])
        else:
            a = "no num"
        if isinstance(com[2],int):
            b = com[2]
        elif com[2] in store.keys():
            b = store.get(com[2])
        else:
            b = "no num"
        # print(a, " and ",b)
        if isinstance(a,int) and isinstance(b,int):
            if com[1] == "AND":
                store[dest] = a & b
            elif com[1] == "OR":
                store[dest] = a | b
            elif com[1] == "LSHIFT":
                store[dest] = a << b
            else:
                store[dest] = a >> b
        else:
            print("line incomplete")
            commands.append(line)
    # print(store)
    count += 1
    if "a" in store.keys() or count > 100000:
        break


print(count)


print(store["a"])