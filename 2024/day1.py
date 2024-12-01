import sys
sys.path.append("../advent-of-code")
from util import *
import numpy as np, math, itertools, hashlib
from functools import reduce

init()

array = load_day(1, 2024)
part_2 = False
total = 0
n, a = [], []
for line in array:
    num1, num2 = line.split("   ")
    n.append(int(num1))
    a.append(int(num2))

z = {}
x = {}

# n.sort()
# a.sort()

for q in n:
    # print(a.count(q)*q)
    total += a.count(q)*q

# for b, c in zip(n[::-1], a[::-1]):
#     total += abs(b-c)

result(total)
# print(z)
# result(sum(i for i in z.values()))