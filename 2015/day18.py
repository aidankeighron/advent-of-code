import sys
sys.path.append("../advent-of-code")
from util import *
from copy import deepcopy
import numpy as np, math
init()

array = load_day(18, 2015)
array = [[char for char in line] for line in array]
part_2 = False
total = 0

def get_neighbors(x, y):
    neighbors = 0
    for i in range(x-1, x+2):
        if i < 0 or i >= len(array):
            continue
        for j in range(y-1, y+2):
            if j < 0 or j >= len(array[i]):
                continue
            if not (i == x and j == y):
                neighbors += 1 if array[i][j] == '#' else 0
    return neighbors

for _ in range(100):
    new_array = deepcopy(array)
    for x, line in enumerate(array):
        for y, char in enumerate(line):
            if (x == 0 or x == len(array)-1) and (y == 0 or y == len(line)-1):
                continue
            neighbors = get_neighbors(x, y)
            if char == "#" and neighbors == 2 or neighbors == 3:
                new_array[x][y] = "#"
            elif char == "#":
                new_array[x][y] = "."
            elif char == "." and neighbors == 3:
                new_array[x][y] = "#"
    array = deepcopy(new_array)
    
    

result(sum(1 for line in array for char in line if char == "#"))