import sys
sys.path.append("../advent-of-code-2023")
from util import *
import numpy as np, math
init()

array = load_day(5, 2015)
part_2 = False
total = 0

# vowels = ['a', 'e', 'i', 'o', 'u']

for line in array:
    # num_v = 0
    # for v in vowels:
    #     num_v += line.count(v)
    # if num_v < 3 or 'ab' in line or 'cd' in line or 'pq' in line or 'xy' in line:
    #     continue

    match = False
    for i in range(len(line)-1):
        sub = line[i:i+2]
        if sub in line[:i] or sub in line[i+2:]:
            match = True
            break
    if not match:    
        continue

    double = False
    for char, next_char in zip(line[:-2], line[2:]):
        if char == next_char:
            double = True
            break
    if not double:
        continue

    total += 1

result(total)