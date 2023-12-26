import sys
sys.path.append("../advent-of-code-2023")
from util import init, load_day, load_file, result
import math
import numpy as np
init()

array = load_day(1, 2015)
part_2 = False
total = 0

# open_bracket = array[0].count("(")
# closed_bracket = array[0].count(")")
# total = open_bracket-closed_bracket

for i, char in enumerate(array[0]):
    if char == "(":
        total += 1
    else:
        total -= 1
    if total < 0:
        total = i+1
        break

result(total)