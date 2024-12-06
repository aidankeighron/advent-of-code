import sys
sys.path.append("../advent-of-code")
from util import *
import numpy as np, math, itertools, hashlib
from functools import reduce

init()

array = load_day(6, 2024)
part_2 = False
total = 0
total2 = 0

grid = []
start = (0,0)
for i, line in enumerate(array):
    grid.append(list(line))
    if "^" in line:
        start = (i, list(line).index("^"))

direction = 0
# U R D L
directions = [[-1, 0], [0,1], [1, 0], [0, -1]]
while True:
    # print(start)
    if grid[start[0]][start[1]] == "X":
        grid[start[0]][start[1]] = "O"
    else: 
        grid[start[0]][start[1]] = "X"

    next_start = [start[0]+directions[direction][0], start[1]+directions[direction][1]]

    if next_start[0] not in range(len(grid)) or next_start[1] not in range(len(grid[0])):
        break

    if grid[next_start[0]][next_start[1]] == "#":
        direction += 1
        direction %= 4
        start = [start[0]+directions[direction][0], start[1]+directions[direction][1]]
    else:
        start = next_start


for row in grid:
    for col in row:
        if col == "X" or col == "O":
            total += 1
        if col == "O":
            total2 += 1
result(total)
result(total2)