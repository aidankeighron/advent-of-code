import sys
sys.path.append("../advent-of-code")
from util import *
import numpy as np, math, itertools
from functools import reduce

# init()

array = load_day(15, 2016)
part_2 = False
total = 0

disks = []
positions = []
for line in array:
    parsed = parse_line(line, 'Disc #{} has {} positions; at time=0, it is at position {}.')
    disks.append({"positions": int(parsed[1]), "start": int(parsed[2])})
    positions.append(int(parsed[1]))
# print("Start", disks)

t = 0
while True:
    a = 0
    for i, disk in enumerate(disks):
        if (t+i+1+disk["start"]) % disk["positions"] != 0:
            break
    else:
        break
    t += 1

result(t)