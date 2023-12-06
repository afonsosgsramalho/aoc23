import itertools
import math
import re
from collections import defaultdict

with open("day3.txt") as f:
    ls = f.read().strip().split("\n")

box = list(itertools.product((-1, 0, 1), (-1, 0, 1)))

symbols = set()
for i, l in enumerate(ls):
    for j, x in enumerate(l):
        if x != '.' and not x.isdigit():
            symbols.add((i, j))

part_sum = 0
parts_by_symbol = defaultdict(list)

for i, l in enumerate(ls):
    for match in re.finditer(r"\d+", l):
        n = int(match.group())
        
        boundary = set()
        for j in range(match.start(), match.end()):
            for di, dj in box:
                boundary.add((i + di, j + dj))
        if symbols & boundary:
            part_sum += n
        for symbol in symbols & boundary:
            parts_by_symbol[symbol].append(n)

# Part 1
print(part_sum)

# Part 2
print(sum(math.prod(v) for v in parts_by_symbol.values() if len(v) == 2))
