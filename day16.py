from util import init, load_day, load_file, result
import math
import numpy as np
init()

array = load_day(16)
part_2 = False
total = 0

#     1
#  4     2
#     3
#
points = set()
def move_beam(x, y, direction):
    pos = (x,y,direction)
    # print(pos)
    if pos in points:
        return
    if pos[0] < 0 or pos[1] < 0 or pos[1] > len(array[0])-1 or pos[0] > len(array)-1:
        return
    points.add(pos)
    if array[pos[1]][pos[0]] == '|':
        if direction == 1 or direction == 3:
            if direction == 1:
                move_beam(pos[0], pos[1]-1, 1)
            if direction == 3:
                move_beam(pos[0], pos[1]+1, 3)
        else:
            move_beam(pos[0], pos[1]-1, 1)
            move_beam(pos[0], pos[1]+1, 3)
    if array[pos[1]][pos[0]] == '-':
        if direction == 4 or direction == 2:
            if direction == 2:
                move_beam(pos[0]+1, pos[1], 2)
            if direction == 4:
                move_beam(pos[0]-1, pos[1], 4)
        else:
            move_beam(pos[0]+1, pos[1], 2)
            move_beam(pos[0]-1, pos[1], 4)
    if array[pos[1]][pos[0]] == '\\':
        if direction == 1:#
            move_beam(pos[0]-1, pos[1], 4)
        if direction == 2:#
            move_beam(pos[0], pos[1]+1, 3)
        if direction == 3:
            move_beam(pos[0]+1, pos[1], 2)
        if direction == 4:
            move_beam(pos[0], pos[1]-1, 1)
    if array[pos[1]][pos[0]] == '/':
        if direction == 1:#
            move_beam(pos[0]+1, pos[1], 2)
        if direction == 2:#
            move_beam(pos[0], pos[1]-1, 1)
        if direction == 3:
            move_beam(pos[0]-1, pos[1], 4)
        if direction == 4:
            move_beam(pos[0], pos[1]+1, 3)
    if array[pos[1]][pos[0]] == '.':
        if direction == 1:
            move_beam(pos[0], pos[1]-1, 1)
        if direction == 2:
            move_beam(pos[0]+1, pos[1], 2)
        if direction == 3:
            move_beam(pos[0], pos[1]+1, 3)
        if direction == 4:
            move_beam(pos[0]-1, pos[1], 4)

for i in range(len(array)):
    move_beam(0,i,2)
    move_beam(len(array[0])-1,i,4)
move_beam(0,0,3)
move_beam(len(array[0])-1,0,3)
for i in range(len(array[0])):
    move_beam(i,0,3)
    move_beam(i,len(array)-1,1)
move_beam(0,len(array)-1,2)
move_beam(len(array[0])-1,len(array)-1,4)
    
a = set()
for p in points:
    a.add((p[0], p[1]))
    
result(len(a))