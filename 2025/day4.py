import sys
sys.path.append("../advent-of-code")
from util import *
import numpy as np, math, itertools, hashlib
from functools import reduce, cache
from collections import defaultdict

# https://docs.python.org/3/library/collections.html
# https://docs.python.org/3/library/itertools.html
# Itertools Functions:
# product('ABCD', repeat=2)                   AA AB AC AD BA BB BC BD CA CB CC CD DA DB DC DD
# permutations('ABCD', 2)                     AB AC AD BA BC BD CA CB CD DA DB DC
# combinations('ABCD', 2)                     AB AC AD BC BD CD
# combinations_with_replacement('ABCD', 2)    AA AB AC AD BB BC BD CC CD DD

init()

def p_a(arr):
    for line in arr:
        print(''.join(str(x) for x in line))

def to_g(grid, arr, integer):
    grid.append([int(x) if integer else x for x in arr])

array = load_day(4, 2025)
part_2 = False
total = 0

@cache
def bfs(node):
    return False

grid = []
for line in array:
    to_g(grid, line, False)

removed = 1
while removed != 0:
    removed = 0
    for i, row in enumerate(grid):
        for j, col in enumerate(row):
            if col == "@":
                num = 0
                for x in [-1, 0, 1]:
                    for y in [-1, 0, 1]:
                        if (x == 0 and y == 0) or (i+x not in range(len(grid[0]))) or (j+y not in range(len(grid))):
                            continue
                        num += 1 if grid[i+x][j+y] == "@" else 0
                if num < 4:
                    total += 1
                    removed += 1
                    grid[i][j] = "."

# p_a(grid)

result(total)