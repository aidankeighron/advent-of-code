import sys
sys.path.append("../advent-of-code")
from util import *
import numpy as np, math, itertools, hashlib
from functools import reduce

init()

array = load_day(2, 2024)
part_2 = False
total = 0

levels= []
for line in array:
    levels.append(line.split(" "))

asdasdasd = []
for la in levels:
    works = False
    options = []
    for sub in la:
        tmp = la[:]
        tmp.remove(sub)
        options.append(tmp)

    for l in options:
        valid = False
        d = []
        for a, b in zip(l[:-1], l[1:]):
            diff = int(b)-int(a)
            d.append(diff)
            if not (1 <= abs(diff) <= 3):
                break
        else:
            valid = True
        if valid:
        #     all_positive = True 
        #     for element in d:
        #         if element < 0:
        #             all_positive = False 
        #             break
        #     all_neg = True 
        #     for element in d:
        #         if element > 0: 
        #             all_neg = False 
        #             break
        #     if all_positive or all_neg:
            asdasdasd.append(l)
            works = True
            break

    # print(works)
    if works:
        total += 1
    # quit()

result(total)
asdadsaddas = []
