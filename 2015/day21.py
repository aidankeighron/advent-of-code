import sys
sys.path.append("../advent-of-code-2023")
from util import *
import numpy as np, math
init()

array = load_day(21, 2015)
part_2 = False
total = 0

weapons = []
armor = []
rings = []

c = 0
for i in array:
    if i == '':
        c += 1
        continue
    p = i.split()
    p = p[-3:]
    p = np.vectorize(int)(p)
    if c == 0:
        weapons.append(p)
    if c == 1:
        armor.append(p)
    if c == 2:
        rings.append(p)

armor.append([0, 0, 0]) # making not wearing armor possible
rings.append([0, 0, 0]) # same for rings
rings.append([0, 0, 0])  

result(total)