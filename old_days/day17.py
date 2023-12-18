from util import init, load_day, load_file, result
import math
import numpy as np
init()

array = load_day(17)
part_2 = False
total = 0
#          x,y,moves in same dir, dir, heat
points = [(0,0,0,0,0)]
#     0
#  3     1
#     2
existing_points = {}
ending = []
while points:
    point = points.pop()
    if f'{point[0]}-{point[1]}-{point[3]}' in existing_points:
        if existing_points[f'{point[0]}-{point[1]}-{point[3]}'] < point[4]:
            continue
    if point[0] == len(array[0])-1 and point[1] == len(array)-1:
        ending.append(point)
        continue
    existing_points[f'{point[0]}-{point[1]}-{point[3]}'] = point[4]
    new_points = []
    if point[0]+1 <= len(array[0])-1 and (point[2] >= 4 or point[3] == 1):
        new_points.append((point[0]+1, point[1], (point[2]+1) if point[3] == 1 else 0, 1, int(array[point[1]][point[0]+1])+point[4]))
    if point[0]-1 >= 0 and (point[2] >= 4 or point[3] == 3):
        new_points.append((point[0]-1, point[1], (point[2]+1) if point[3] == 3 else 0, 3, int(array[point[1]][point[0]-1])+point[4]))
    if point[1]+1 <= len(array)-1 and (point[2] >= 4 or point[3] == 2):
        new_points.append((point[0], point[1]+1, (point[2]+1) if point[3] == 2 else 0, 2, int(array[point[1]+1][point[0]])+point[4]))
    if point[1]-1 >= 0 and (point[2] >= 4 or point[3] == 0):
        new_points.append((point[0], point[1]-1, (point[2]+1) if point[3] == 0 else 0, 0, int(array[point[1]-1][point[0]])+point[4]))
    
    for p in new_points:
        if p[3] == point[3] and p[2] > 10:
            continue
        if point[3] == 0 and p[3] == 2:
            continue
        if point[3] == 1 and p[3] == 3:
            continue
        if point[3] == 2 and p[3] == 0:
            continue
        if point[3] == 3 and p[3] == 1:
            continue
        points.append(p)
ending = sorted(ending, key=lambda x: x[-1])
result(ending[0][-1]+int(array[-1][-1]))