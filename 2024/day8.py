from collections import defaultdict
import sys
sys.path.append("../advent-of-code")
from util import *
import numpy as np, math, itertools, hashlib
from functools import reduce

init()

array = load_day(8, 2024)
part_2 = False
total = 0

grid = []
nodes = defaultdict(list)
for i, line in enumerate(array):
    grid.append(list(line))
    for j, ch in enumerate(line):
        if ch != ".":
            nodes[ch].append([i,j])

antinodes = grid[:]
for ch, node in nodes.items():
    # print(ch, node)
    for pair in list(itertools.combinations(node, 2)):
        dx = abs(pair[0][0] - pair[1][0])
        dy = abs(pair[0][1] - pair[1][1])
    
        #  1
        y = 0
        x = 0
        i = 0
        while True:
            if pair[0][0] < pair[1][0]:
                # 0
                x = (pair[0][0] if x == 0 else x) - dx
                y = pair[0][1] if y == 0 else y
            else:
                # 1
                x = (pair[1][0] if x == 0 else x) - dx
                y = pair[1][1] if y == 0 else y
            if pair[0][1] > pair[1][1]:
                # 0
                y += dy 
            else:
                # 1
                y -= dy
            # print(x, y)
            i += 1
            if i > len(grid)*len(grid[0])*2:
                break
            if x in range(len(antinodes)) and y in range(len(antinodes[0])):
                antinodes[x][y] = "#"
            else:
                break
        #  2
        y = 0
        x = 0
        i = 0
        while True:
            if pair[0][0] > pair[1][0]:
                # 0
                x = (pair[0][0] if x == 0 else x) + dx
                y = pair[1][1] if y == 0 else y
            else:
                # 1
                x = (pair[1][0] if x == 0 else x) + dx
                y = pair[1][1] if y == 0 else y
            if pair[0][1] > pair[1][1]:
                # 0
                y -= dy 
            else:
                # 1
                y += dy
            
            i += 1
            if i > len(grid)*len(grid[0])*2:
                break
            if x in range(len(antinodes)) and y in range(len(antinodes[0])):
                antinodes[x][y] = "#"
            else:
                break

# for row in grid:
#     print(''.join(row))

# print('***')
for row in antinodes:
    print(''.join(row))
    for col in row:
        if col != ".":
            total += 1

result(total)