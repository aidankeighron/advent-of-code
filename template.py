import sys
sys.path.append("../advent-of-code")
from util import *
import numpy as np, math, itertools, hashlib
from functools import reduce

init()

array = load_day(19, 2016)
part_2 = False
total = 0

for line in array:
    

result(total)