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

array = load_day(16, 2024)
part_2 = False
total = float('inf')
total2 = []

grid = []
start = (0,0)
end = (0,0)
for i, line in enumerate(array):
    to_g(grid, line, False)
    for j, char in enumerate(line):
        if char == "S":
            start = (i, j)
        if char == "E":
            end = (i, j)

steps = [[start[0], start[1], 0, 0, [0,0,[]]]]
directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
seen = {}
t = 0
while steps:
    x, y, step, direction, other = steps.pop(0)

    if end[0] == x and end[1] == y:
        if step <= total:
            print(step, other)
            total2.append(len(other[2])+1, step)
        total = min(total, step)

    if f"{x}{y}{direction}" in seen and seen[f"{x}{y}{direction}"] < step:
        continue
    seen[f"{x}{y}{direction}"] = step

    dx, dy = directions[direction]
    new_x, new_y = x+dx, y+dy
    if new_x in range(len(grid)) and new_y in range(len(grid[0])) and grid[new_x][new_y] != "#":
        other[2].append((x,y))
        steps.append([new_x, new_y, step+1, direction, [other[0]+1, other[1], other[2]]])
    steps.append([x, y, step+1000, (direction+1)%4, [other[0], other[1]+1, other[2]]])
    steps.append([x, y, step+1000, (direction-1)%4, [other[0], other[1]+1, other[2]]])
 

    # for i, (dx, dy) in enumerate(directions):
    #     new_x, new_y = x+dx, y+dy

    #     if new_x not in range(len(grid)) or new_y not in range(len(grid[0])):
    #         continue
    #     if grid[new_x][new_y] == "#":
    #         continue
    #     new_steps = step+1
    #     if direction == i:
    #         new_steps += 0*1000
    #         other[1] += 0
    #     elif (direction+1)%4 == i or (direction-1)%4 == i:
    #         new_steps += 1*1000 
    #         other[1] += 1
    #     elif (direction+2)%4 == i or (direction-2)%4 == i:
    #         new_steps += 2*1000
    #         other[1] += 2
    #     else:
    #         print("What?") 
            
    #     steps.append([new_x, new_y, new_steps, i, [other[0]+1, other[1], other[2]]])

    t += 1

p_a(grid)

result(total)
result(sum([x[0] for x in total2 if x[1]==total]))