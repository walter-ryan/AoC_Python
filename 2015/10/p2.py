with open('2015/10/input.txt') as file:
    line = file.read()


def LookAndSay(input: str) -> str:
    oldDigit = 'X'
    currentCount = 0
    newString = ''
    for digit in input:
        if digit == oldDigit:
            currentCount += 1
        elif oldDigit != 'X':
            newString += str(currentCount) + oldDigit
            currentCount = 1
            oldDigit = digit
        else:
            currentCount = 1
            oldDigit = digit
            
    newString += str(currentCount) + oldDigit

    return newString

for i in range(50):
    line = LookAndSay(line)
print('Length:',len(line))