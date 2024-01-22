import sys
sys.path.append("../advent-of-code-2023")
from util import *
import numpy as np, math
from itertools import permutations
init()

array = load_day(13, 2015)
part_2 = False
total = 0

mapping = {}
people = set()
for line in array:
    person1, sign, amount, person2 = format(line, '{} would {} {} happiness units by sitting next to {}.')
    if person1 not in mapping:
        mapping[person1] = {}
    mapping[person1][person2] = int(amount) * (1 if sign == 'gain' else -1)
    people.add(person1)
    people.add(person2)

def validate(order):
    total = 0
    for person1, person2 in zip(order[:-1], order[1:]):
        total += mapping[person1][person2] + mapping[person2][person1]
    return total + mapping[order[-1]][order[0]] + mapping[order[0]][order[-1]]
        
for items in permutations(people):
    validation = validate(items)
    # print(validation)
    # print(items)
    total = max(total, validation)

result(total)