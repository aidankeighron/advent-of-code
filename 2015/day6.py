import sys
sys.path.append("../advent-of-code")
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
    operator, start1, start2, end1, end2 = parse_line(line, '{} {},{} through {},{}', True)
    end1 += 1
    end2 += 1
    
    if operator == 'turnon':
        grid[start1:end1, start2:end2] += ones[start1:end1, start2:end2]
    if operator == 'turnoff':
        grid[start1:end1, start2:end2] -= ones[start1:end1, start2:end2]
        grid[grid == -1] = zeroes[grid == -1]
    if operator == 'toggle':
        grid[start1:end1, start2:end2] += twos[start1:end1, start2:end2]
    

flattened = grid.flatten()
total = sum(flattened)
# toggle 461,550 through 564,900
result(total)