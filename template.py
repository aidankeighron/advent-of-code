import sys
sys.path.append("../advent-of-code")
from util import *
import numpy as np, math, itertools, hashlib
from functools import reduce
from collections import defaultdict

init()

array = load_day(9, 2024)
part_2 = False
total = 0

for line in array:
    

result(total)