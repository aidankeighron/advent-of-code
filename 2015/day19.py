import sys
sys.path.append("../advent-of-code-2023")
from util import *
import numpy as np, math
init()

array = load_day(19, 2015)
part_2 = False
total = 0

options = {}
string = ""
for line in array:
    if "=>" in line:
        right, left = line.split(" => ")
        if right not in options:
            options[right] = []
        options[right].append(left)
    else:
        string = line

res = set()
def dfs(i, cur):
    if i >= len(cur):
        res.add(cur)
        return
    
    for o in options:
        if cur[i:i+len(o)] == o:
            for option in options[o]:
                res.add(cur[:i] + option + cur[i+len(o):])
                # dfs(i+len(option), cur[:i] + option + cur[i+len(o):])
    dfs(i+1, cur)

dfs(0, string)

result(len(res)-1)
