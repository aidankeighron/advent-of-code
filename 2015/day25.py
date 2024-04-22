import sys
sys.path.append("../advent-of-code")
from util import *
import numpy as np, math, itertools
from functools import reduce

init()

total = 20151125
count = sum(range(3010 + 3019 - 1)) + 3019
for _ in range(count - 1):
    total = (total * 252533) % 33554393

result(total)