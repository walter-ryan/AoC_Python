# --- Day 7: Some Assembly Required ---

# This year, Santa brought little Bobby Tables a set of wires and bitwise logic gates! Unfortunately, little Bobby is a little under the recommended age range, and he needs help assembling the circuit.

# Each wire has an identifier (some lowercase letters) and can carry a 16-bit signal (a number from 0 to 65535). A signal is provided to each wire by a gate, another wire, or some specific value. Each wire can only get a signal from one source, but can provide its signal to multiple destinations. A gate provides no signal until all of its inputs have a signal.

# The included instructions booklet describes how to connect the parts together: x AND y -> z means to connect wires x and y to an AND gate, and then connect its output to wire z.

# For example:

#     123 -> x means that the signal 123 is provided to wire x.
#     x AND y -> z means that the bitwise AND of wire x and wire y is provided to wire z.
#     p LSHIFT 2 -> q means that the value from wire p is left-shifted by 2 and then provided to wire q.
#     NOT e -> f means that the bitwise complement of the value from wire e is provided to wire f.

# Other possible gates include OR (bitwise OR) and RSHIFT (right-shift). If, for some reason, you'd like to emulate the circuit instead, almost all programming languages (for example, C, JavaScript, or Python) provide operators for these gates.

# For example, here is a simple circuit:

# 123 -> x
# 456 -> y
# x AND y -> d
# x OR y -> e
# x LSHIFT 2 -> f
# y RSHIFT 2 -> g
# NOT x -> h
# NOT y -> i

# After it is run, these are the signals on the wires:

# d: 72
# e: 507
# f: 492
# g: 114
# h: 65412
# i: 65079
# x: 123
# y: 456

# In little Bobby's kit's instructions booklet (provided as your puzzle input), what signal is ultimately provided to wire a?

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

print(count)


print(store["a"])