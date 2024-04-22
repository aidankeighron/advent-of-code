import sys
sys.path.append("../advent-of-code")
from util import init, load_day, load_file, result
import math
import numpy as np
init()

array = load_day(11, 2023)
part_2 = False
total = 0


indexes = []
for i, line in enumerate(array):
    same = True
    for char in line:
        if char != ".":
            same = False
    if same:
        indexes.append(i)

for i, index in enumerate(indexes):
    for j in range(1000000-1):
        array.insert(index+i*(1000000-1), "."*len(array[0]))    

array = np.array([np.array(list(l)) for l in array])
array = np.rot90(array)
array = list([list(l) for l in array])

indexes = []
for i, line in enumerate(array):
    same = True
    for char in line:
        if char != ".":
            same = False
    if same:
        indexes.append(i)

for i, index in enumerate(indexes):
    for j in range(1000000-1):
        array.insert(index+i*(1000000-1), "."*len(array[0]))  
    
array = np.array([np.array(list(l)) for l in array])
np.rot90(array)
np.rot90(array)
np.rot90(array)
array = list([list(l) for l in array])

coords = []
for i in range(len(array)):
    for j in range(len(array[i])):
        if array[i][j] == '#':
            coords.append((i,j))
            
combos = []
for i in range(len(coords) - 1) : 
    c = [(coords[i], x) for x in coords[i+1:]]
    combos.extend(c)


for a, b in combos:
    dist = abs(b[0]-a[0]) + abs(b[1]-a[1])
    total += dist
    
result(total)