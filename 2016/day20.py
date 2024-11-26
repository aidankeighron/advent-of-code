import sys
sys.path.append("../advent-of-code")
from util import *
import numpy as np, math, itertools, hashlib
from functools import reduce

init()

array = load_day(20, 2016)
part_2 = False
total = 0

ranges = []
for line in array:
    line = line.split("-")
    ranges.append([int(line[0]), int(line[1])])

ranges.sort()

def is_valid(n):
    for start, end in ranges:
        if start <= n <= end:
            break
    else:
        if n < 2**32:
            return True
    return False

total = 0
for ip in [x[1]+1 for x in ranges if is_valid(x[1]+1)]:
    if total == 0:
        result(ip)
    while is_valid(ip):
        total += 1
        ip += 1

result(total)