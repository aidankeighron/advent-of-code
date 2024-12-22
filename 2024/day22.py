import sys
sys.path.append("../advent-of-code")
from util import *
import numpy as np, math, itertools, hashlib
from functools import reduce, cache
from collections import defaultdict

init()

def p_a(arr):
    for line in arr:
        print(''.join(str(x) for x in line))

def to_g(grid, arr, integer):
    grid.append([int(x) if integer else x for x in arr])

array = load_day(22, 2024)
part_2 = False
total = 0

@cache
def bfs(node):
    return False

numbers = []
for line in array:
    # to_g(grid, line, False)
    numbers.append(int(line))

def mix(a, b):
    return a ^ b
def prune(a):
    return a % 16777216

sequences = defaultdict(int)

for n in numbers:
    number = n
    past_price = int(str(number)[-1])
    window = []
    changes = set()
    # for _ in range(10):
    for _ in range(2000):
        number = mix(number*64, number)
        number = prune(number)
        number = mix(number//32, number)
        number = prune(number)
        number = mix(number*2048, number)
        number = prune(number)

        price = int(str(number)[-1])
        price_difference = price - past_price
        window.append(str(price_difference))
        if len(window) >= 4:
            if ''.join(window) not in changes:
                sequences[''.join(window)] += price
                changes.add(''.join(window))
            window.pop(0)
        past_price = price
    # print(dict(sequences))
    # print(number)

    total += number

# p_a(grid)

result(total)
# for key, value in sequences.items():
#     if key == "-21-13":
#         print(value)
#     if value == 30:
#         print(key)
result(max(dict(sequences).values()))