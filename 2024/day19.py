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

array = load_day(19, 2024)
part_2 = False
total = 0

towels = array[0].split(", ")
patterns = []
for line in array[2:]:
    if len(line.strip()) > 0:
        patterns.append(line)

@cache
def found(pattern):
    currs = [pattern[:]]
    out = 0
    if pattern == "":
        return 1

    for o in towels:
        if pattern.startswith(o):
            out += found(pattern[len(o):])

    return out

# @cache
# def found(pattern):
#     currs = [pattern[:]]
#     seen = set()
#     out = 0
#     while currs:
#         c = currs.pop(0)
#         if c == "":
#             out += 1
#             continue
#         if c in seen:
#             continue
#         seen.add(c)
#         options = [o for o in towels if c.startswith(o)]
#         for o in options:
#             currs.append(c[len(o):])
#     return out

for pattern in patterns:
    f = found(pattern)

    total += f

result(total)