import sys
sys.path.append("../advent-of-code")
from util import *
import numpy as np, math, itertools, hashlib
from functools import reduce

init()

array = load_day(7, 2024)
part_2 = False
total = 0

operators = {"*": lambda a, b: a*b,
            "+": lambda a, b: a+b,
            "||": lambda a, b: int(str(a)+str(b))
            # "/": lambda a, b: a/b,
            # "-": lambda a, b: a-b,
}

values = []
for line in array:
    line = line.split(":")
    values.append([int(line[0]), [int(a) for a in line[1].split(" ") if a != ""]])

i = 0
for target, nums in values:
    x = list(operators.keys())
    options = [p for p in itertools.product(x, repeat=len(nums)-1)]

    for o in options:
        tmp = nums[:]
        for operator in o:
            num1 = tmp.pop(0)
            num2 = tmp.pop(0)
            res = operators[operator](num1, num2)
            tmp.insert(0, res)
            # print(num1, operator,  num2, res, tmp[:])

        if tmp[0] == target:
            total += tmp[0]
            # print(nums, target, total)
            break
    i += 1
    if i % 100 == 0:
        print(i, len(values))
    # quit()

result(total)