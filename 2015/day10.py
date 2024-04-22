import sys
sys.path.append("../advent-of-code")
from util import *
import numpy as np, math
init()

array = load_day(10, 2015)
part_2 = False
total = 0

inp = array[0]

def expand(string):
    current = string[0]
    current_count = 1
    new_string = ''
    if len(string) > 1:
        for char in string[1:]:
            if char == current:
                current_count += 1
            else:
                new_string += str(current_count) + current
                current = char
                current_count = 1
    if current_count != 0:
        new_string += str(current_count) + current
    
    return new_string

i = 0
total = expand(inp)
while i < 49:
    i += 1
    total = expand(total)

result(len(total))