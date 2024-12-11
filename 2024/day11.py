import sys
sys.path.append("../advent-of-code")
from util import *
import numpy as np, math, itertools, hashlib
from functools import reduce, cache
from collections import defaultdict

init()

def p_a(arr):
    for line in arr:
        print(''.join(str(x) for x in line))

def to_g(grid, arr, integer):
    grid.append([int(x) if integer else x for x in arr])

array = load_day(11, 2024)
part_2 = False
total = 0

stones = []
for line in array:
    # to_g(grid, line, False)
    for stone in line.split(" "):
        stones.append(int(stone))

@cache
def c(x, n):
    if n == 75:
        return 1
    s = str(x)
    slen = len(s)
    if x == 0:
        return c(1, n+1)
    elif slen & 1 == 0:
        return c(int(s[slen//2:]), n+1)+c(int(s[:slen//2]), n+1)
    else:
        return c(x*2024, n+1)

result(sum(c(stone, 0) for stone in stones))

print(stones)
for i in range(25):
    new_stones = []
    n = len(stones)
    for i in range(n):
        if stones[i] == 0:
            new_stones.append(1)
        elif len(str(stones[i])) % 2 == 0:
            stones[i] = str(stones[i])
            n = len(stones[i])
            new_stones.append(int(stones[i][:n//2]))
            new_stones.append(int(stones[i][n//2:]))
        else:
            new_stones.append(stones[i]*2024)
    stones = new_stones

result(len(stones))