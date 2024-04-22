import sys
sys.path.append("../advent-of-code")
from util import init, load_day, load_file, result
import math
import numpy as np
init()

array = load_day(23 2023)
part_2 = False
total = 0

def check_point(y, x, points):
    if y < 0 or x < 0 or y > len(array)-1 or x > len(array[0])-1:
        return None
    if (y,x) in points:
        return None
    if array[y][x] == '#':
        return None
    if array[y][x] == '.':
        return (y,x, 0)
    # if array[y][x] == 'v':
    #     if (y+1,) in points:
    #         return None
    #     return (y+1, x, 1)
    # if array[y][x] == '<' and x-1 >= 0:
    #     if (y,x-1) in points:
    #         return None
    #     return (y, x-1, 1)
    # if array[y][x] == '>' and x+1 <= len(array[0])-1:
    #     if (y,x+1) in points:
    #         return None
    #     return (y, x+1, 1)

# def print_points(points):
#     grid = [['.' for _ in range(len(array[0])-1)] for _ in range(len(array)-1)]
#     for p in points:
#         grid[p[0]][p[1]] = '#'
#     for g in grid:
#         print(''.join(g))
#     print("**********")

start = (0, 1, 0, []) # y, x
points = [start]
# seen = set()
endings = []
while points:
    point = points.pop(0)
    if point[0] == len(array)-1 and point[1] == len(array[0])-2:
        endings.append(point[2])
        continue

    new_points = [check_point(point[0]+1, point[1], point[3]), check_point(point[0]-1, point[1], point[3])
                  ,check_point(point[0], point[1]+1, point[3]), check_point(point[0], point[1]-1, point[3])]
    # new_points.append(check_point(point[0]+1, point[1], point[3]))
    # new_points.append(check_point(point[0]-1, point[1], point[3]))
    # new_points.append(check_point(point[0], point[1]+1, point[3]))
    # new_points.append(check_point(point[0], point[1]-1, point[3]))
    point[3].append(tuple(list(point[:2]).copy()))
    # if new_points == [None]*4:
    #     print_points(point[3])
    for p in new_points:
        if p == None:
            continue
        if p[0] == point[0] and p[1] == point[1]:
            continue
        points.append((p[0], p[1], point[2]+1+p[2], point[3].copy()))
    
print(endings)
result(max(endings))