import sys
sys.path.append("../advent-of-code")
from util import *
import numpy as np, math, itertools
from functools import reduce

init()

array = load_day(7, 2016)
part_2 = False
total = 0

for line in array:
    i = 0
    outside = True
    valid = False
    # print(line)
    search = set()
    while i < len(line)-2:
        if line[i] == "[":
            outside = False
            i += 1
            continue
        if line[i] == "]":
            outside = True
            i += 1
            continue

        if outside:
            if line[i] == line[i+2] and line[i] != line[i+1]:
                # print(line[i:i+3])
                search.add(tuple([line[i+1],line[i],line[i+1]]))
        i += 1

    i = 0
    outside = True
    while i < len(line)-2:
        if line[i] == "[":
            outside = False
            i += 1
            continue
        if line[i] == "]":
            outside = True
            i += 1
            continue
        if not outside:
            if tuple(line[i:i+3]) in search:
                # print("valid")
                valid = True
                break 
        i += 1

    # print(search)
    if valid:
        total += 1
        

result(total) # 22
# import sys
# sys.path.append("../advent-of-code")
# from util import *
# import numpy as np, math, itertools
# from functools import reduce

# init()

# array = load_day(7, 2016)
# part_2 = False
# total = 0

# for line in array:
#     i = 0
#     outside = True
#     valid = False
#     # print(line)
#     while i < len(line)-3:
#         if line[i] == "[":
#             outside = False
#             i += 1
#             continue
#         if line[i] == "]":
#             outside = True
#             i += 1
#             continue

#         # print(line[i:i+2], line[i+3:i+1:-1])
#         if line[i:i+2] == line[i+3:i+1:-1] and line[i] != line[i+1]:
#             # print("valid", outside)
#             if outside:
#                 valid = True
#             else:
#                 valid = False
#                 break
#         i += 1
#     if valid:
#         total += 1
        

# result(total)