from functools import cache
from math import floor, log10
from tqdm import tqdm

with open('2024/11/input.txt') as file:
    nums = file.read().split()


counts = dict()
for num in nums:
    if num not in counts.keys():
        counts[int(num)] = 1
    else:
        counts[int(num)] += 1


@cache
def dupeRocks(num: int) -> list:
    if num == 0:
        return [1]
    l = floor(log10(num))+1

    if l % 2 == 0:
        return[num // 10**(l//2),num %  10**(l//2)]
    else:
        return [num*2024]


def blink(counts: dict) -> dict:
    nd = dict()
    for n in counts.keys():
        for m in dupeRocks(n):
            if m in nd.keys():
                nd[m] += counts[n]
            else:
                nd[m] = counts[n]
    return nd


for i in tqdm(range(75)):
    counts = blink(counts)
print('Length:',sum(counts.values()))

