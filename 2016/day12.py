import sys
sys.path.append("../advent-of-code")
from util import *
import numpy as np, math, itertools
from functools import reduce

init()

array = load_day(12, 2016)
part_2 = False
total = 0

reg = {"a": 0, "b": 0, "c": 1, "d": 0}

i = 0
while i < len(array):
    if array[i].startswith("inc"):
        reg[array[i][-1]] += 1
    elif array[i].startswith("dec"):
        reg[array[i][-1]] -= 1
    else:
        cmds = array[i].split()
        if cmds[0] == "cpy":
            reg[cmds[2]] = reg[cmds[1]] if cmds[1] in reg else int(cmds[1])
        elif cmds[0] == "jnz":
            if cmds[1] in reg: 
                if reg[cmds[1]]:
                    i += int(cmds[2])
                    continue
            elif cmds[1]:
                    i += int(cmds[2])
                    continue

    i += 1
    
result(reg["a"])