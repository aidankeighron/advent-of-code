import sys
sys.path.append("../advent-of-code-2023")
from util import *
import numpy as np, math
init()

array = load_day(6, 2015)
part_2 = False
total = 0

grid = np.array([[0 for _ in range(1000)] for _ in range(1000)])
ones = np.array([[1 for _ in range(1000)] for _ in range(1000)])
twos = np.array([[2 for _ in range(1000)] for _ in range(1000)])
zeroes = np.array([[0 for _ in range(1000)] for _ in range(1000)])

for line in array:
    operator, start1, start2, end1, end2 = format(line, '{} {},{} through {},{}')
    start1 = int(start1)
    start2 = int(start2)
    end1 = int(end1)+1
    end2 = int(end2)+1
    
    if operator == 'turnon':
        grid[start1:end1, start2:end2] += ones[start1:end1, start2:end2]
    if operator == 'turnoff':
        grid[start1:end1, start2:end2] -= ones[start1:end1, start2:end2]
        grid[grid == -1] = zeroes[grid == -1]
    if operator == 'toggle':
        grid[start1:end1, start2:end2] += twos[start1:end1, start2:end2]
        
for i in range(len(list)//2):
    list[~i], list[i] = list[i], list[~i]
    

flattened = grid.flatten()
total = sum(flattened)
# toggle 461,550 through 564,900
result(total)