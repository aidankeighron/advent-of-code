import sys
sys.path.append("../advent-of-code")
from util import *
import numpy as np, math, itertools, hashlib
from functools import reduce

init()

# array = "yjjvjgan"
array = "yjjvjgan"
part_2 = False
total = 0

queue = [[0, 0, 0, ""]]

while queue:
    location = queue.pop(0)

    if location[0] == 3 and location[1] == 3:
        print(location)
        total = max(location[2], total)
        continue

    directions = {"U": [-1, 0], "D": [1, 0], "L": [0, -1], "R": [0, 1]}
    hash = hashlib.md5((array+location[3]).encode('utf-8')).hexdigest()
    for i, (direction, difference) in enumerate(directions.items()):
        if (hash[i] not in {"b", "c", "d", "e", "f"} or location[0]+difference[0] not in range(4)
            or location[1]+difference[1] not in range(4)):
            continue

        queue.append([location[0]+difference[0], location[1]+difference[1],
                      location[2]+1, location[3]+direction])

result(total)