import sys
sys.path.append("../advent-of-code-2023")
from util import *
import numpy as np, math
init()

array = load_day(3, 2015)
part_2 = False
total = 0

current = [0,0]
robot = [0,0]
tiles = set()
for i, char in enumerate(array[0]):
    if i % 2 == 0:
        if char == '>':
            current[0] += 1
        if char == '<':
            current[0] -= 1
        if char == '^':
            current[1] += 1
        if char == 'v':
            current[1] -= 1
        tiles.add((current[0], current[1]))
    else:
        if char == '>':
            robot[0] += 1
        if char == '<':
            robot[0] -= 1
        if char == '^':
            robot[1] += 1
        if char == 'v':
            robot[1] -= 1
        tiles.add((robot[0], robot[1]))
    
total = len(tiles)
result(total)