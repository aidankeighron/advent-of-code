import sys
sys.path.append("../advent-of-code-2023")
from util import *
import numpy as np, math, itertools
init()

array = load_day(23, 2015)
part_2 = False
total = 0

registers = {'a': 524032737, 'b': 0}

i = 0
while i < 8:
    if "jio" in array[i] and registers["a"] == 1:
        break
    if "inc b" in array[i]:
        registers["b"] += 1
        i += 1
        continue
    if "inc a" in array[i]:
        registers["a"] += 1
        i += 1
        continue
    if "jie" in array[i] and registers["a"] % 2 == 0:
        i += 4
        continue
    if "tpl" in array[i]:
        registers["a"] *= 3
        i += 1
        continue
    if "jmp" in array[i]:
        i += int(array[i][-1])
        continue

    if "hlf" in array[i]:
        registers["a"] /= 2
        continue


result(registers["b"])