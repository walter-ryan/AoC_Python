with open('2015/11/test.txt') as file:
    line = file.read()

def toOrdList(password: str) -> list:
    ordList = []
    for ch in password:
        ordList.append(ord(ch))
    return ordList

def toPassword(ordList: list) -> str:
    password = ''
    for num in ordList:
        password += chr(num)
    return password

def increment(ordList: list) -> list:
    # ORD range: 97-122
    ordList[-1] += 1
    if ordList[-1] == 123:
        for i in range(len(ordList)-2,-1,-1):
            if ordList[i+1] == 123:
                ordList[i+1] = 97
                ordList[i] += 1
        if ordList[0] == 123:
            ordList[0] = 97
    return ordList

def isSafe(ordList: list) -> bool:
    # must not contain i, l, o (105, 108, 111)
    if 105 in ordList:
        return False
    if 108 in ordList:
        return False
    if 111 in ordList:
        return False
    # must contain two sets of pairs
    if not containsConseqPairs(ordList):
        return False
    # must contain increasing set of 3
    if not containsIncTrio(ordList):
        return False
    return True

def containsConseqPairs(ordList: list) -> bool:
    for i in range(len(ordList)-4):
        if ord
        pass
    return False

def containsIncTrio(ordList: list) -> bool:
    return False

print(line)

l = toOrdList(line)
itt = 0
while not isSafe(l):
    l = increment(l)
    itt += 1


print(toPassword(l))
print('itt', itt)
