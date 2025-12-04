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

array = load_day(3, 2025)
part_2 = False
total = 0

@cache
def bfs(node):
    return False

grid = []
for line in array:
    line = [int(i) for i in line]
    num = ""
    offset = 0
    for n in range(11, -1, -1):
        line_1 = line[offset:-n] if n != 0 else line[offset:]
        m = max(line_1)
        num += str(m)
        m_i = line_1.index(m)

        if m_i == len(line_1)-1:
            line_1 = line[:-1]
            num += "".join([str(a) for a in line[m_i+offset+1:]])
            break
        else:
            offset += m_i+1
        
    total += int(num)

result(total)