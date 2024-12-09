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

blocks = []
id_ = 0
for line in array:
    free = False
    for char in line:
        if free:
            blocks.append(['.', int(char)])
        else:
            blocks.append([str(id_), int(char)])
            id_ += 1
        free = not free

j = 0
for i in range(len(blocks)):
    if i % 10 == 0:
        print(i, len(blocks))
    if blocks[~i][0] == ".":
        continue
    p = ""
    for b in blocks:
        p += b[0]*b[1]
    # print(p, j, ~i, blocks[~i][0])

    while j in range(len(blocks)) and blocks[j][0] != ".":
        j += 1

    if j in range(len(blocks)):
        for k in range(j, ~i+len(blocks)):
            if blocks[k][0] == "." and blocks[k][1] >= blocks[~i][1]:
                # match
                if blocks[k][1] == blocks[~i][1]: # equal
                    blocks[k], blocks[~i] = blocks[~i], blocks[k]
                else:
                    diff = blocks[k][1] - blocks[~i][1]
                    blocks[k] = blocks[~i]
                    blocks[~i] = [".", blocks[k][1]]
                    blocks.insert(k+1, [".", diff])
                    # j = 0
                break

i = 0
for block in blocks:
    if block[0] == ".":
        i += block[1]
        continue
    for _ in range(block[1]):
        total += int(block[0])*i
        i += 1

result(total)


# import sys
# sys.path.append("../advent-of-code")
# from util import *
# import numpy as np, math, itertools, hashlib
# from functools import reduce
# from collections import defaultdict

# init()

# array = load_day(9, 2024)
# part_2 = False
# total = 0

# blocks = []
# id_ = 0
# for line in array:
#     free = False
#     for char in line:
#         if free:
#             blocks.extend(['.']*int(char))
#         else:
#             blocks.extend([str(id_)]*int(char))
#             id_ += 1
#         free = not free

# j = 0
# blocks = list(blocks)
# a = 0
# for i in range(len(blocks)):
#     # print(''.join(blocks[:~i]))
#     # print(''.join(blocks[:~i]).count("."))
#     if i % 1000 == 0:
#         print(''.join(blocks[:~i]).count("."))
#         print(i, len(blocks))
#     # if ''.join(blocks[:~i]).count(".") == 0:
#     if i > 44000 and ''.join(blocks[:~i]).count(".") == 0:
#         # print(j+1, ~i+len(blocks))
#         break
#     while j in range(len(blocks)) and blocks[j] != ".":
#         j += 1
#     if j in range(len(blocks)):
#         blocks[j], blocks[~i] = blocks[~i], blocks[j]
#         # print(blocks[~i], blocks[j])


# # print(''.join(blocks))
# # for i, char in enumerate(blocks):
# #     if blocks[i] == "." and blocks[i+1] == "8":
# #         blocks[i], blocks[i+1] = blocks[i+1], blocks[i]
# #         break 
# # print(''.join(blocks))

# for i, char in enumerate(blocks):
#     if char == ".":
#         continue
#     # print(char, i)
#     total += int(char)*i


# result(total)