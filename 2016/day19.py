import sys
sys.path.append("../advent-of-code")
from util import *
import numpy as np, math, itertools, hashlib
from functools import reduce

init()

# array = 3005290
array = 5
part_2 = False
total = 0

elves = [1]*array
elves_left = len(elves)
while True:
    has_presents = 0
    for i in range(len(elves)):
        j = (i+elves_left//2)%len(elves)
        if elves[i] != 0:
            elves[i], elves[j] = elves[i]+elves[j], 0
            elves_left -= 1
            has_presents += 1
        print(i+1, j+1, elves_left)
    break
    if has_presents == 1:
        # print(elves, elves_map, has_presents)
        for i, elv in enumerate(elves):
            if elv != 0:
                print(i+1, elv)
        break
result(total)