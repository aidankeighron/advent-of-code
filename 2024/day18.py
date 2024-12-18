import sys
sys.path.append("../advent-of-code")
from util import *
import numpy as np, math, itertools, hashlib
from functools import reduce
from collections import defaultdict

init()

def p_a(arr):
    for line in arr:
        print(''.join(str(x) for x in line))

def to_g(grid, arr, integer):
    grid.append([int(x) if integer else x for x in arr])

array = load_day(18, 2024)
part_2 = False
total = float('inf')

size = 71
end = 2915 # 2914 - 2915
grid = [['.']*size for _ in range(size)]
for i, line in enumerate(array[:end]):
    # to_g(grid, line, False)
    x, y = line.split(",")
    grid[int(x)][int(y)] = "#"
p_a(grid)
start = (0,0)
path = [[start, 0]]
directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]
seen = set()
while path:
    p, steps = path.pop(0)

    if p == (size-1, size-1):
        print(total)
        total = min(total, steps)

    if p in seen:
        continue
    seen.add(p)

    for dx, dy in directions:
        x = p[0]+dx
        y = p[1]+dy
        if x not in range(size) or y not in range(size):
            continue
        if grid[x][y] == "#":
            continue
        path.append([(x, y), steps+1])

# p_a(grid)

result(total)