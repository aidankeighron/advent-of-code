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

array = load_day(2, 2025)
part_2 = False
total = set()

@cache
def bfs(node):
    return False

grid = []
for line in array:
    to_g(grid, line, False)
    for r in line.split(","):
        start, end = r.split("-")
        for i in range(int(start), int(end)+1):
            s = str(i)
            for j in range(1, len(s)//2+1):
                index = 0
                while s[index:index+j] == s[index+j:index+j*2]:
                    index += j

                if index == len(s)-j:
                    total.add(i)

# p_a(grid)

result(sum(total))