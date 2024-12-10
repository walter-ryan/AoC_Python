import string
from itertools import combinations
from tqdm import tqdm
with open('2024/08/input.txt') as file:
    lines = [line.strip() for line in file.readlines()]


chars = set(string.ascii_letters) | set('1234567890')

antinodes = set()

for a in tqdm(chars):
    letter_positions = []
    for y in range(len(lines)):
        for x in range(len(lines[0])):
            if lines[y][x] == a:
                letter_positions.append(complex(x, y))

    for (x,y) in combinations(letter_positions,2):
        an = 2*x - y
        if an.real in range(len(lines[0])) and an.imag in range(len(lines)):
            antinodes.add(an)
        an = 2*y - x
        if an.real in range(len(lines[0])) and an.imag in range(len(lines)):
            antinodes.add(an)

print(len(antinodes))
