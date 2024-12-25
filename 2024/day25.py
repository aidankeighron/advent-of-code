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

array = load_day(25, 2024)
part_2 = False
total = 0

@cache
def bfs(node):
    return False

keys = []
locks = []
i = 0
while True:
    if i >= len(array):
        break
    cur = array[i:i+7]
    heights = [0]*(len(cur)-1)

    for chars in cur:
        for j, char in enumerate(chars):
            heights[j] += int(char=="#")
    if "#" in cur[0]:
        locks.append(heights)
    else:
        keys.append(heights)

    i += 8

for lock in locks:
    for key in keys:
        wrong = False
        for i in range(len(key)):
            if key[i] + lock[i] > 7:
                wrong = True
                break
        if not wrong:
            total += 1

result(total)