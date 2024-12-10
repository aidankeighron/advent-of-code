import sys
sys.path.append("../advent-of-code")
from util import *
import numpy as np, math, itertools, hashlib
from functools import reduce
from collections import defaultdict

init()

array = load_day(10, 2024)
part_2 = True
total = 0

trailheads = []
grid = []
for i, line in enumerate(array):
    grid.append([int(x) if x != '.' else -1 for x in line])
    for j, x in enumerate(line):
        if x == "0":
            trailheads.append([i,j, 0])

# for g in grid:
#     print(''.join([str(x) if x != -1 else "." for x in g]))

for t in trailheads:
    path = [t]
    score = 0
    visited = set()
    while path:
        i, j, k = path.pop(0)
        if not part_2 and (i, j) in visited:
            continue

        if k == 9:
            visited.add((i,j))
            score += 1
            continue

        directions = [[0,1], [1,0], [-1, 0], [0, -1]]

        for dx, dy in directions:
            x = i+dx
            y = j+dy
            if x not in range(len(grid)) or y not in range(len(grid[0])):
                continue

            if grid[x][y] == k+1:
                path.append([x, y, k+1])
    total += score

result(total)