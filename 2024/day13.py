import sys
sys.path.append("../advent-of-code")
from util import *
import numpy as np, math, itertools, hashlib
from functools import reduce
from collections import defaultdict

init()

def p_a(arr):
    for line in arr:
        print(''.join(str(x) for x in line))

def to_g(grid, arr, integer):
    grid.append([int(x) if integer else x for x in arr])

array = load_day(13, 2024)
part_2 = False
total = 0

prizes = []
i = 0
prize = []
for line in array:
    if i == 0:
        x, y = parse_line(line, "Button A: X+{}, Y+{}")
        prize.append([int(x), int(y)])
    elif i == 1:
        x, y = parse_line(line, "Button B: X+{}, Y+{}")
        prize.append([int(x), int(y)])
    elif i == 2:
        x, y = parse_line(line, "Prize: X={}, Y={}")
        prize.append([int(x), int(y)])
    else:
        prizes.append(prize)
        prize = []
        i = -1
    i += 1
prizes.append(prize)

questions = []
for q, prize in enumerate(prizes):
    a, b, target = prize
    target[0] += 10000000000000
    target[1] += 10000000000000
    a_presses = (target[0]*b[1]-target[1]*b[0])/(a[0]*b[1]-a[1]*b[0])
    b_presses = (target[1]*a[0]-target[0]*a[1])/(a[0]*b[1]-a[1]*b[0])
    if a_presses == int(a_presses) and b_presses == int(b_presses):
        total += int(3 * a_presses + b_presses)
    # a, b, target = prize
    # target[0] += 10000000000000
    # target[1] += 10000000000000
    # # max_presses = 500000000000
    # cost = -1
    # a_, b_ = 0,0
    # for i in range(0, max_presses):
    #     x = 0
    #     y = 0
    #     presses_b = 0
    #     for _ in range(i):
    #         x += a[0]
    #         y += a[1]
    #         if x >= target[0] or y >= target[1]:
    #             break
    #     for m in range(0, max_presses):
    #         x += b[0]
    #         y += b[1]
    #         presses_b += 1
    #         if x >= target[0] or y >= target[1]:
    #             break
    #     # print(i, m, x, y, target)
    #     if x == target[0] and y == target[1]:
    #         c = i*3 + presses_b*1
    #         # print(i, presses_b, c, x, y, target)
    #         if cost == -1:
    #             cost = c
    #             a_ = i
    #             b_ = presses_b
    #         else:
    #             if c < cost:
    #                 a_ = i
    #                 b_ = presses_b
    #             cost = min(cost, c)

    # if cost != -1:
    #     total += cost
    #     questions.append([a_, b_, q])
        # print(cost, total)
    # quit()

result(total)