import sys
sys.path.append("../advent-of-code")
from util import *
import numpy as np, math, itertools
from functools import reduce

init()

array = load_day(1, 2016)
part_2 = False
total = [0, 0]

direction = 0

locations = set((0,0))
for distance in array[0].split(", "):
    if distance[0] == "R":
        direction += 1
    else:
        direction -= 1
    direction %= 4
    
    if direction == 0:
        for i in range(int(distance[1:])):
            if (total[0], total[1]) in locations:
                result(abs(total[0]+total[1]))
                break
            total[1] += 1
            locations.add((total[0], total[1]))
    elif direction == 1:
        for i in range(int(distance[1:])):
            if (total[0], total[1]) in locations:
                result(abs(total[0]+total[1]))
                break
            total[0] += 1
            locations.add((total[0], total[1]))
        # total[0] += int(distance[1:])
    elif direction == 2:
        for i in range(int(distance[1:])):
            if (total[0], total[1]) in locations:
                result(abs(total[0]+total[1]))
                break
            total[1] -= 1
            locations.add((total[0], total[1]))
        # total[1] -= int(distance[1:])
    elif direction == 3:
        for i in range(int(distance[1:])):
            if (total[0], total[1]) in locations:
                result(abs(total[0]+total[1]))
                break
            total[0] -= 1
            locations.add((total[0], total[1]))
        # total[0] -= int(distance[1:])

    



result(abs(total[0]+total[1]))