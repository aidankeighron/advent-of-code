import sys
sys.path.append("../advent-of-code")
from util import *
import numpy as np, math, itertools
from functools import reduce
from collections import Counter

init()

array = load_day(6, 2016)
part_2 = False
total = ''

for i in range(len(array)):
    array[i] = list(array[i])

array = np.rot90(array)

for col in array:
    print(Counter(col).most_common()[-1])
    total += Counter(col).most_common()[-1][0]
    

result(total[::-1])