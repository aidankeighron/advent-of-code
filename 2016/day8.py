import sys
sys.path.append("../advent-of-code")
from util import *
import numpy as np, math, itertools
from functools import reduce

init()

array = load_day(8, 2016)
part_2 = False
total = 0

out = [["." for _ in range(50)] for _ in range(6)]

out = np.array(out)

for line in array:
    if line.startswith("rect"):
        w,h = parse_line(line, "rect {}x{}", True)
        for i in range(w):
            for j in range(h):
                out[j,i] = "#"
    elif line.startswith("rotate row"):
        row, amm = parse_line(line, "rotate row y={} by {}", True)
        out[row] = np.roll(out[row], amm)
    elif line.startswith("rotate column"):
        row, amm = parse_line(line, "rotate column x={} by {}", True)
        out[:,row] = np.roll(out[:,row], amm)

for line in out:
    for ch in line:
        if ch == "#":
            total += 1
    print(''.join(line))

result(total)