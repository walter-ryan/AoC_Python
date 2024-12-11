from functools import cache

with open('2024/11/input.txt') as file:
    nums = file.read().split()

print(nums)

@cache
def handleNum(num: str) -> list:
    if num == '0':
        return ['1']
    elif len(num) % 2 == 0:
        return [str(int(num[:len(num)//2])),str(int(num[len(num)//2:]))]
    else:
        return [str(int(num)*2024)]



def blink(l: list) -> list:
    nl = []
    for num in l:
        nl = nl + handleNum(num)
    return nl

for i in range(25):
    nums = blink(nums)
    print('Step', i)
    print('Length:',len(nums))

print(len(nums))