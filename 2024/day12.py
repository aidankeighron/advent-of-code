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

array = load_day(12, 2024)
part_2 = True
total = 0

# Find the number of covered side for mat[i][j].
def numofneighbour(mat, i, j, target, history1, history2, border: set):
    R = len(mat)
    C = len(mat[0])
    count = 0
    # print(i, j, history1, history2)
    # UP
    if (i > 0 and mat[i - 1][j] == target):
        count+= 1
        # history1.add(i-1)
    else:
        border.add(((i, j), (-1, 0)))
 
    # LEFT
    if (j > 0 and mat[i][j - 1] == target):
        count+= 1
    else:
        border.add(((i, j), (0, -1)))
 
    # DOWN
    if (i < R-1 and mat[i + 1][j] == target):
        count+= 1
    else:
        border.add(((i, j), (1, 0)))
 
    # RIGHT
    if (j < C-1 and mat[i][j + 1] == target):
        count+= 1
    else:
        border.add(((i, j), (0, 1)))
 
    return count

def num_sides(pairs:set):
    out = 0
    while pairs:
        (x, y), (i, j) = pairs.pop()
        r = (x+j, y-i)
        while (r, (i, j)) in pairs:
            pairs.remove((r, (i, j)))
            r = (r[0]+j, r[1]-i)
        l = (x-j, y+i)
        while (l, (i, j)) in pairs:
            pairs.remove((l, (i, j)))
            l = (l[0]-j, l[1]+i)
        out += 1
    return out

# Returns sum of perimeter of shapes formed with 1s
def find_perimeter(mat, target):
 
    perimeter = 0
 
    # Traversing the matrix and finding ones to
    # calculate their contribution.
    history1 = set()
    history2 = set()
    border = set()
    for i in range(0, len(mat)):
        for j in range(0, len(mat[0])):
            if (mat[i][j]) == target: # and i not in history1 and j not in history2:
                perimeter += (4 - numofneighbour(mat, i, j, target, history1, history2, border))
                history1.add(i)
                history2.add(j)
    
    return perimeter if not part_2 else num_sides(border)

# def perimeter_of_shape(array, target):

#   perimeter = 0
#   for i in range(len(array)):
#     for j in range(len(array[0])):
#       if array[i][j] == target:
#         # Check if the cell is on the edge
#         if i == 0 or i == len(array) - 1 or j == 0 or j == len(array[0]) - 1:
#           perimeter += 1
#         # Check if the cell has a 0 neighbor
#         if i > 0 and array[i - 1][j] != target:
#           perimeter += 1
#         if i < len(array) - 1 and array[i + 1][j] != target:
#           perimeter += 1
#         if j > 0 and array[i][j - 1] != target:
#           perimeter += 1
#         if j < len(array[0]) - 1 and array[i][j + 1] != target:
#           perimeter += 1

#   return perimeter

grid = []
counts = defaultdict(int)
chars = []
for line in array:
    to_g(grid, line, False)
    for char in line:
        if char not in chars:
            chars.append(char)
grid = np.array(grid, dtype='<U10')

from skimage.measure import label

i = 0
# print(chars)
for char in chars:
    labels, count = label(grid == char, return_num=True, connectivity=1)
    groups = [np.argwhere(labels == x) for x in range(1, count + 1)]
    # print("dupe", i)
    if len(groups) > 1:
        for group in groups:
            for x, y in group:
                # print(grid[x,y], x, y, str(i))
                grid[x, y] = str(i*i)
                # print(grid[x,y], x, y, str(i))
            i += 1
            # if i > 10:
            #     quit()

# print(grid[14, 114])
# print(grid[114, 14])
for row in grid:
    for char in row:
    #    print(char)
       counts[char] += 1
# print(counts)
for key, count in counts.items():
    p = find_perimeter(grid.tolist(), key)
    total += count * p
    # print(p, key)
    # print(key, p)
# a = "R"
# print(counts[a])
# print(find_perimeter(array, a))
# a = "M"
# print(counts[a])
# print(find_perimeter(array, a))
# print(grid)
# p_a(grid)

result(total)
# 838988