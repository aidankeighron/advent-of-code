import sys
sys.path.append("../advent-of-code")
from util import *
import numpy as np, math, itertools
from functools import reduce

init()

a = str(10111011111001111)
part_2 = False
total = 0

while len(a) < 35651584:
    b = a
    b = b[::-1].replace("0", "2").replace("1", "0").replace("2", "1")
    a += "0"+b

a = a[:35651584]

while len(a) % 2 == 0:
    l = ['1' if c == d else '0' for c, d in zip(a[::2], a[1::2])]

    a = ''.join(l)
    print(len(a))

result(a)