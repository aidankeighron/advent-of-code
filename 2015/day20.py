import sys
sys.path.append("../advent-of-code-2023")
from util import *
import numpy as np, math
init()

array = 33100000
part_2 = False
total = 0

from functools import reduce

def factors(n):    
    return sum(set(reduce(list.__add__,([i*10, (n//i)*10] for i in range(1, int(n**0.5) + 1) if n % i == 0))))

# print(factors(4))
# quit()
house = 0
while True:
    house += 1
    total = factors(house)
    
    if total == array:
        result(total)
        break