from util import init, load_day, load_file, result
import math, time
import numpy as np
init()

array = load_day(21)
part_2 = False
total = 0

start = []
for i, line in enumerate(array):
    for j, char in enumerate(line):
        # if array[i][j] == '.':
            # total += 1
        if char == "S":
            start = [i,j]
            break
    if start:
        break
start = [65,65]
# print(total)
# quit()
current_options = set()
current_options.add((start[0], start[1]))
next_options = set()
steps = 85+65-130
for i in range(steps):
    while current_options:
        position = current_options.pop()
        try:
            if array[position[0]+1][position[1]] != '#':
                next_options.add((position[0]+1, position[1]))
        except:
            ...
        try:
            if position[0] != 0:
                if array[position[0]-1][position[1]] != '#':
                    next_options.add((position[0]-1, position[1]))
        except:
            ...
        try:
            if array[position[0]][position[1]+1] != '#':
                next_options.add((position[0], position[1]+1))
        except:
            ...
        try:
            if position[1] != 0:
                if array[position[0]][position[1]-1] != '#':
                    next_options.add((position[0], position[1]-1))
        except:
            ...
    current_options = next_options
    next_options = set()

image = [['.' for _ in range(len(array[0]))] for _ in range(len(array))]
for option in current_options:
    image[option[0]][option[1]] = '#'
image[start[0]][start[1]] = 'O'
    
for line in image:
    print(''.join(line))
bottom = (6659+213)
left = (6672+215)
top = (6666+206)
right = (6653+210)
inner = sum([203856-i+2 for i in range(0,203857+2)])
diag_m = (((203856+2)//2)+1)
diag_a = (((203856+2)//2))
A = (15099*((inner*4)+203857//2-203857//38+56)/2+1693*diag_a+1678*diag_a+1668*diag_a+1681*diag_a+bottom+left+right+top+109*diag_m+112*diag_m+108*diag_m+107*diag_m)
print(A)
# 130
print(inner)
# print(26501365%130)
total = len(current_options)
result(total)