import sys
sys.path.append("../advent-of-code")
from util import *
import numpy as np, math, itertools
from functools import reduce

init()

array = 1362
# array = 10
part_2 = False
total = 0

start = [1,1]
end = [39,31]
# end = [4,7]

def decimal_to_binary(n):  
    return bin(n).replace("0b", "") 

def func(x, y):
    return x*x + 3*x + 2*x*y + y + y*y + array

def is_open(x, y):
    f = func(x, y)
    binary = decimal_to_binary(f)
    return sum(int(i) for i in str(binary)) % 2 == 0

# dim = [7, 10]
dim = [60, 60]
maze = [[" " if is_open(x, y) else "#" for x in range(0, dim[1])] for y in range(dim[0])]
for m in maze:
    print(' '.join(m))
# quit()
# print(maze[31][39])
# maze[31][39] = " "
length = float("inf")
queue = [[*start, 0]]
seen = set()
while queue:
    x, y, l = queue.pop(0)
    if l > 50 or (x, y) in seen:
        continue
    if [x, y] == end:
        print(l)
        length = min(length, l)
        continue

    seen.add((x, y))
    directions = [[1,0], [0,1], [-1, 0], [0, -1]]

    for a, b in directions:
        t, r = x+a, b+y
        if t not in range(0, dim[0]) or r not in range(0, dim[1]):
            continue
        if maze[t][r] == "#":
            continue
        queue.append([t, r, l+1])


# result(length)
result(len(seen))