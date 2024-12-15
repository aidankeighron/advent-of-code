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

array = load_day(15, 2024)
part_2 = False
total = 0

grid = []
is_action = False
actions = ''
start = (0,0)
for i, line in enumerate(array):
    if line == '!':
        is_action = True
        continue
    if is_action:
        actions += line
    else:
        for j, char in enumerate(line):
            if char == "@":
                start = (i, j)
        to_g(grid, line, False)

# p_a(grid)
a = {
    "<": [0, -1],
    ">": [0, 1],
    "^": [-1, 0],
    "v": [1, 0],
}
for action in actions:
    # p_a(grid)
    dx, dy = a[action]
    next_ = [start[0]+dx, start[1]+dy]
    if next_[0] not in range(len(grid)) or next_[1] not in range(len(grid[1])):
        continue

    if grid[next_[0]][next_[1]] == ".":
        grid[start[0]][start[1]] = "."
        start = next_
        grid[start[0]][start[1]] = "@"
    elif grid[next_[0]][next_[1]] == "#":
        continue
    else:
        # Wall
        next_ = [next_[0]+dx, next_[1]+dy]
        to_check = [[next_[0]+dx, next_[1]]]
        wrong = False
        while grid[next_[0]][next_[1]] != "." and grid[next_[0]][next_[1]] != "#":
            if grid[next_[0]][next_[1]] == "]" and grid[next_[0]+dx][next_[1]] == "[":
                to_check.append([next_[0]+dx, next_[1]])
            elif grid[next_[0]][next_[1]] == "]" and grid[next_[0]+dx][next_[1]] == "#":
                wrong = True
            if grid[next_[0]][next_[1]] == "[" and grid[next_[0]+dx][next_[1]] == "]":
                to_check.append([next_[0]+dx, next_[1]])
            elif grid[next_[0]][next_[1]] == "[" and grid[next_[0]+dx][next_[1]] == "#":
                wrong = True
            for check in to_check:
                x, y = check
                if grid[x][y] == "]" and grid[x+dx][y] == "[":
                    to_check.append([x+dx, y])
                elif grid[x][y] == "]" and grid[x+dx][y] == "#":
                    wrong = True
                if grid[x][y] == "[" and grid[x+dx][y] == "]":
                    to_check.append([x+dx, y])
                elif grid[x][y] == "[" and grid[x+dx][y] == "#":
                    wrong = True
            next_ = [next_[0]+dx, next_[1]+dy]
        if wrong or grid[next_[0]][next_[1]] == "#":
            continue
        if action == "^" or action == "v":
            # Wall and not blocking
            while grid[next_[0]][next_[1]] != "@":
                prev = grid[next_[0]-dx][next_[1]-dy] 
                if prev == "[":
                    grid[next_[0]][next_[1]] = "["
                    grid[next_[0]-dx][next_[1]-dy] = "."
                    right_box = [next_[0], next_[1]+1]
                    while grid[right_box[0]][right_box[1]] == "[" and grid[right_box[0]+dx][right_box[1]+1] != "#":
                        grid[right_box[0]+dx][right_box[1]] = "["
                        grid[right_box[0]+dx-1][right_box[1]+1] = "."
                        grid[right_box[0]+dx][right_box[1]+1] = "]"
                        right_box = [right_box[0]+dx, right_box[1]+1]
                    grid[next_[0]][next_[1]+1] = "]"
                    grid[next_[0]-dx][next_[1]-dy+1] = "."
                elif prev == "]":
                    grid[next_[0]][next_[1]] = "]"
                    grid[next_[0]-dx][next_[1]-dy] = "."
                    right_box = [next_[0], next_[1]+1]
                    while grid[right_box[0]][right_box[1]] == "]" and grid[right_box[0]+dx][right_box[1]-1] != "#":
                        grid[right_box[0]+dx][right_box[1]] = "]"
                        grid[right_box[0]+dx-1][right_box[1]-1] = "."
                        grid[right_box[0]+dx][right_box[1]-1] = "["
                        right_box = [right_box[0]+dx, right_box[1]-1]
                    grid[next_[0]][next_[1]-1] = "["
                    grid[next_[0]-dx][next_[1]-dy-1] = "."
                next_ = [next_[0]-dx, next_[1]-dy]
            grid[next_[0]][next_[1]] = "."
            next_ = [next_[0]+dx, next_[1]+dy]
            start = next_
            grid[start[0]][start[1]] = "@"
            
        else:
            # Wall and not blocking
            start = True
            while grid[next_[0]][next_[1]] != "@":
                grid[next_[0]][next_[1]] = "[" if start and action == "<" or not start and action == ">"  else "]"
                start = not start
                next_ = [next_[0]-dx, next_[1]-dy]
            grid[next_[0]][next_[1]] = "."
            next_ = [next_[0]+dx, next_[1]+dy]
            start = next_
            grid[start[0]][start[1]] = "@"

for i, row in enumerate(grid):
    for j, col in enumerate(row):
        if col == "[":
            total += (i * 100) + j
    
p_a(grid)

result(total)