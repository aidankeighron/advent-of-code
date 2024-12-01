import sys
sys.path.append("../advent-of-code")
from util import *
import numpy as np, math, itertools, hashlib
from functools import reduce

init()

array = load_day(1, 2024)
part_1, part_2 = 0, 0
a, b = [], []
for line in array:
    num1, num2 = line.split("   ")
    a.append(int(num1))
    b.append(int(num2))

a.sort()
b.sort()

for c, d in zip(a[::-1], b[::-1]):
    part_1 += abs(c-d)
    part_2 += b.count(c)*c

result(part_1)
result(part_2)