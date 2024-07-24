# Now find one that starts with six zeroes.

import hashlib

with open('./2015/04/input.txt','r') as file:
    word = file.read()

found = False

i = 0

while not found:
    i += 1
    password = word + str(i)
    hexword = password.encode()
    result = hashlib.md5(hexword).hexdigest()
    if result[0:6] == "000000":
        print("Found! i =",i)
        print("Password:", password)
        print("MD5 Hash:", result)
        break