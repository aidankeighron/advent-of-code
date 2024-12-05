from collections import defaultdict
import functools
import sys
sys.path.append("../advent-of-code")
from util import *
import numpy as np, math, itertools, hashlib
from functools import reduce

init()

array = load_day(5, 2024)
part_2 = False
total = 0

rules = defaultdict(list)
updates = []
update = False
for line in array:
    if line == "@":
        update = True
        continue

    if not update:
        a, b = line.split("|")
        rules[int(a)].append(int(b))
    else:
        updates.append([int(a) for a in line.split(",")])

for u in updates:
    wrong = False
    for i, option in enumerate(u):
        for other in u[i+1:]:
            if option in rules[other]:
                wrong = True
                break
        if wrong:
            break
    
    if not wrong and not part_2:
        total += u[len(u)//2]

    if wrong and part_2:
        def sort(a, b):
            if b in rules[a]:
                return -1
            return 1
        cmp = functools.cmp_to_key(sort)
        u.sort(key=cmp)
        total += u[len(u)//2]

result(total)