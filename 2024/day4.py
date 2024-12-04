import sys
sys.path.append("../advent-of-code")
from util import *
import numpy as np, math, itertools, hashlib, re
from functools import reduce

init()

array = load_day(4, 2024)
part_2 = False
total = 0
numpy = []
for line in array:
    numpy.append(list(line))
array = np.array(numpy)

for i in range(1, len(array)-1):
    for j in range(1, len(array[0])-1):
        if array[i,j] == "A":
            if array[i-1, j-1] == "M":
                if array[i+1, j-1] == "M":
                    if array[i+1, j+1] == "S":
                        if array[i-1, j+1] == "S":
                            total += 1
            if array[i-1, j-1] == "S":
                if array[i+1, j-1] == "S":
                    if array[i+1, j+1] == "M":
                        if array[i-1, j+1] == "M":
                            total += 1
            if array[i-1, j-1] == "M":
                if array[i+1, j-1] == "S":
                    if array[i+1, j+1] == "S":
                        if array[i-1, j+1] == "M":
                            total += 1
            if array[i-1, j-1] == "S":
                if array[i+1, j-1] == "M":
                    if array[i+1, j+1] == "M":
                        if array[i-1, j+1] == "S":
                            total += 1

# for i in range(-len(array), len(array)):
#     line = ''.join(np.diag(array, k=i))

#     start = line.find('MAS')
#     while start != -1:
#         if i+2 < len(array) and i-2 > -len(array):
#             top = ''.join(np.diag(array, k=i+2))
#             bottom = ''.join(np.diag(array, k=i-2))
#             if top[start] == "S" and bottom[start] == "M":
#                 total += 1
#             print(top, top[start])
#             print(line, start)
#             print(bottom, bottom[start])

#         start = line.find("MAS", start+1)


result(total)