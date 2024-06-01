import sys
sys.path.append("../advent-of-code")
from util import *
import numpy as np, math, itertools
from functools import reduce

init()

array = load_day(9, 2016)
part_2 = False
total = ''

i = 0
for line in array:
    i = 0
    while i < len(line):
        if line[i] == '(':
            i += 1
            number = ''
            while line[i] != 'x':
                number += line[i]
                i += 1
            number = int(number)
            i += 1
            iterations = ''
            while line[i] != ')':
                iterations += line[i]
                i += 1
            iterations = int(iterations)
            i += 1
            # line = line[:i+1] + line[i:i+number]*iterations + line[i+number:]
            # i += number-1
        else: 
            total += line[i]
        i += 1
        if i % 100000 == 0:
            print(i, len(line), len(line)-i)
    # print(total)
    result(len(total))
    total = ''
