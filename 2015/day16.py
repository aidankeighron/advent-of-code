import sys
sys.path.append("../advent-of-code-2023")
from util import *
import numpy as np, math
init()

array = load_day(16, 2015)
part_2 = False
total = 0

to_find = {
'children': 3,
'cats': 7,
'samoyeds': 2,
'pomeranians': 3,
'akitas': 0,
'vizslas': 0,
'goldfish': 5,
'trees': 3,
'cars': 2,
'perfumes': 1}

def check_item(item, amount):
    if item in ["cats", "trees"]:
        return amount <= to_find[item]
    if item in ["goldfish", "pomeranians"]:
        return amount >= to_find[item]
    return amount != to_find[item]

for line in array:
    number, item1, amount1, item2, amount2, item3, amount3  = parse_line(line, 'Sue {}: {}: {}, {}: {}, {}: {}')
    if check_item(item1, int(amount1)) or check_item(item2, int(amount2)) or check_item(item3, int(amount3)):
        continue

    total = number

result(total)