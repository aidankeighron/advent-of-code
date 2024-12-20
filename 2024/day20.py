import sys
sys.path.append("../advent-of-code")
from util import *
import numpy as np, math, itertools, hashlib
from functools import reduce, cache
from collections import defaultdict

sys.setrecursionlimit(2000)

init()

def p_a(arr):
    for line in arr:
        new = line[:]
        new = ["#" if x == "#" else x for x in new]
        new = ["." if x == "." else x for x in new]
        new = [x[0] if x.isnumeric() else x for x in new]
        print(''.join(str(x) for x in new))

def to_g(grid, arr, integer):
    grid.append([int(x) if integer else x for x in arr])

array = load_day(20, 2024)
part_2 = False
total = 0

grid = []
start = (0, 0)
end = (0, 0)
for i, line in enumerate(array):
    to_g(grid, line, False)
    for j, char in enumerate(line):
        if char == "S":
            start = (i, j)
        elif char == "E":
            end = (i, j)

paths = [[start, 0]]
# paths = 0
seen = set()
directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]
walls = set()
walls2 = set()
end_distance = 0
i = 0
while paths:
    path, distance = paths.pop(0)

    if path == end:
        end_distance = distance
        print(distance)
        break

    for dx, dy in directions:
        x, y = path[0]+dx, path[1]+dy

        if x not in range(len(grid)) or y not in range(len(grid[0])):
            continue

        if grid[x][y] == "#":
            continue
        if (x, y) in seen:
            continue
        seen.add(path)

        paths.append([(x, y), distance+1])
# while paths:
#     path, distance, walls, passThrough, enteredWall = paths.pop(0)

#     grid[path[0]][path[1]] = str(distance)
#     i += 1
#     if i % 10000 == 0:
#         print(i, len(paths))
#     if path == end:
#         walls2.add((distance, walls))
#         print(distance)
#         break

#     for dx, dy in directions:
#         x, y = path[0]+dx, path[1]+dy

#         if x not in range(len(grid)) or y not in range(len(grid[0])):
#             continue

#         if grid[x][y] != "#" and enteredWall:
#             passThrough = False
#         if grid[x][y] == "#" and not enteredWall:
#             enteredWall = True
#         if grid[x][y] == "#" and not passThrough:
#             continue
#         #     walls.add((x,y))
#         #     continue
#         if (x, y) in seen:
#             continue
#         seen.add(path)

#         paths.append([(x, y), distance+1, walls + 1 if grid[x][y] == "#" else 0])
paths = 0
seen = set()
directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]
walls = set()
walls2 = set()
i = 0
@cache
def bfs(node): # NOSONAR
    global paths, i
    path, distance, walls, pass_through, entered_wall = node
    # paths -= 1
    if distance > end_distance-100 or walls > 20:
        return
    grid[path[0]][path[1]] = str(distance)
    i += 1
    print(i, paths, distance, walls, pass_through, entered_wall, path)
    if i % 10000 == 0:
        print(i, paths)
    if path == end:
        walls2.add((distance, walls))
        print(distance)
        return

    for dx, dy in directions:
        x, y = path[0]+dx, path[1]+dy

        if x not in range(len(grid)) or y not in range(len(grid[0])):
            continue

        if grid[x][y] != "#" and entered_wall:
            pass_through = False
        if grid[x][y] == "#" and not entered_wall:
            entered_wall = True
        if grid[x][y] == "#" and not pass_through:
            continue
        #     walls.add((x,y))
        #     continue
        if (x, y) in seen:
            continue
        seen.add(path)

        # paths.append([(x, y), distance+1, walls + 1 if grid[x][y] == "#" else 0])
        paths += 1
        bfs(((x, y), distance+1, walls + (1 if grid[x][y] == "#" else 0), pass_through, entered_wall))

bfs((start, 0, 0, True, False))

# p_a(grid)

# sides = [[[0,1],[0,-1]], [[1,0],[-1,0]]]
# shortcuts = defaultdict(int)
# for x, y in walls:
#     for d1, d2 in sides:
#         x1, y1 = x+d1[0], y+d1[1]
#         x2, y2 = x+d2[0], y+d2[1]
#         if x1 not in range(len(grid)) or y1 not in range(len(grid[0])):
#             continue
#         if x2 not in range(len(grid)) or y2 not in range(len(grid[0])):
#             continue
#         if not grid[x1][y1].isnumeric() or not grid[x2][y2].isnumeric():
#             continue

#         shortcuts[abs(int(grid[x1][y1]) - int(grid[x2][y2]))-2] += 1
#         if abs(int(grid[x1][y1]) - int(grid[x2][y2]))-2 >= 100:
#             total += 1

# print(dict(shortcuts))
# print(sorted(list(dict(shortcuts).keys())))
# print(sorted(list(dict(shortcuts).values())))
result(total)