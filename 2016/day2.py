import sys
sys.path.append("../advent-of-code")
from util import *
import numpy as np, math, itertools
from functools import reduce

init()

array = load_day(2, 2016)
part_2 = False
total = ""
code = [[0,0,1,0,0],[0,2,3,4,0],[5,6,7,8,9],[0,'A','B','C',0],[0,0,'D',0,0]]
start = (2,0)
for line in array:
    #        y,x
    for char in line:
        if char == "U" and start[0]-1 in range(5) and code[start[0]-1][start[1]] != 0:
            start = (start[0]-1, start[1])
        if char == "D" and start[0]+1 in range(5) and code[start[0]+1][start[1]] != 0:
            start = (start[0]+1, start[1])
        if char == "R" and start[1]+1 in range(5) and code[start[0]][start[1]+1] != 0:
            start = (start[0], start[1]+1)
        if char == "L" and start[1]-1 in range(5) and code[start[0]][start[1]-1] != 0:
            start = (start[0], start[1]-1)

    total += f"{code[start[0]][start[1]]}"

result(total)