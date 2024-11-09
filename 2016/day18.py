import sys
sys.path.append("../advent-of-code")
from util import *
import numpy as np, math, itertools, hashlib
from functools import reduce

init()

current_line = list(load_day(18, 2016)[0])
# current_line = list(".^^.^.^^^^")
part_2 = False
total = current_line.count(".")
n = len(current_line)
j = 0
while j < 400000-1: 
    next_line = []
    for i in range(len(current_line)):
        if i != 0 and current_line[i-1] == "^" and current_line[i] == "^" and (i == n-1 or current_line[i+1] == "."):
            next_line.append("^")
        elif current_line[i] == "^" and i != n-1 and current_line[i+1] == "^" and (i == 0 or current_line[i-1] == "."):
            next_line.append("^")
        elif i != 0 and current_line[i-1] == "^" and current_line[i] == "." and (i == n-1 or current_line[i+1] == "."):
            next_line.append("^")
        elif current_line[i] == "." and i != n-1 and current_line[i+1] == "^" and (i == 0 or current_line[i-1] == "."):
            next_line.append("^")
        else:
            total += 1
            next_line.append(".")
    j += 1
    # print(current_line)
    # print(''.join(next_line))
    current_line = list(next_line)

result(total)