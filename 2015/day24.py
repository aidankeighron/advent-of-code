import sys
sys.path.append("../advent-of-code")
from util import *
import numpy as np, math, itertools, operator
from functools import reduce
init()

a = load_day(24, 2015)
array = []
for i in a:
    array.append(int(i))
part_2 = False
total = 0

smallest = []
tot = sum(array)/4

def func(lst, sub):
    for i in range(1, len(lst)):
        for j in (k for k in itertools.combinations(lst, i) if sum(k) == tot):
            if sub == 2:
                return True
            elif sub < 4:
                return func(list(set(lst)-set(j)), sub-1)
            elif func(list(set(lst)-set(j)), sub-1):
                return reduce(operator.mul, j, 1) 

# for iteration in list(itertools.permutations(array)):
#     for i in range(len(iteration)-2):
#         for j in range(i+1, len(iteration)-1):
#             # k = len(iteration)-i-j
#             if sum(iteration[:i]) == sum(iteration[i+1:j]) and sum(iteration[i+1:j]) == sum(iteration[j+1:]):
#                 if i <= j-1 and i <= len(iteration)-i-j:
#                     smallest.append([i, reduce((lambda x, y: x * y), iteration[:i])])
#                 if j-1 <= i and j-1 <= len(iteration)-i-j:
#                     smallest.append([j-1, reduce((lambda x, y: x * y), iteration[i+1:j])])
#                 if len(iteration)-i-j <= j-1 and len(iteration)-i-j <= i:
#                     smallest.append([len(iteration)-i-j, reduce((lambda x, y: x * y), iteration[j+1:])])

result(func(array, 4))