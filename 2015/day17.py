import sys
sys.path.append("../advent-of-code")
from util import *
import numpy as np, math
init()

array = load_day(17, 2015)
part_2 = False
total = 0

containers = []
for line in array:
    containers.append(int(line))
    
capacity = 150

res = []

cur = []
def dfs(i):
    if sum(cur) == capacity:
        res.append(cur.copy())
        return
    elif sum(cur) > capacity or i >= len(containers):
        return
    
    cur.append(containers[i])
    dfs(i+1)
    
    cur.pop()
    dfs(i+1)
    
dfs(0)
smallest = min([len(x) for x in res])
result(sum(1 for x in res if len(x) == smallest))