import sys
sys.path.append("../advent-of-code")
from util import *
import numpy as np, math, itertools
from functools import reduce

init()

array = load_day(3, 2016)
part_2 = False
total = 0

for i in range(len(array)):
    array[i] = list([i for i in array[i].split(' ') if i != ''])

array = np.rot90(array)

for line in array:
    for i, start in enumerate(line[::3]):
        tri = line[i*3:i*3+3]

        if (int(tri[0]) + int(tri[1])) > int(tri[2]):
            if (int(tri[1]) + int(tri[2])) > int(tri[0]):
                if (int(tri[2]) + int(tri[0])) > int(tri[1]):
                    total += 1

result(total)