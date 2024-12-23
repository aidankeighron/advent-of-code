import sys
sys.path.append("../advent-of-code")
from util import *
import numpy as np, math, itertools, hashlib
from functools import reduce, cache
from collections import defaultdict

a = ["tw", "wo", "zk", "gb", "di", "ht", "xz", "ch", "lu", "cz", "vt", "ku", "vf"]
a.sort()
print(",".join(a))

init()

def p_a(arr):
    for line in arr:
        print(''.join(str(x) for x in line))

def to_g(grid, arr, integer):
    grid.append([int(x) if integer else x for x in arr])

array = load_day(23, 2024)
part_2 = False
total = 0

@cache
def bfs(node):
    return False

grid = []
for line in array:
    line = parse_line(line, "{}-{}")
    grid.append(line)

graph = defaultdict(list)

for left, right in grid:
    graph[left].append(right)
    graph[right].append(left)

threes = set()
for key, nodes in dict(graph).items():
    one = key
    bad = False
    connected = set()
    connected.add(key)
    for two, three in itertools.permutations(nodes, 2):
        if three in graph[two]:
            connected.add(three)
            connected.add(two)
            # three = [one, two, three]
            # three.sort()
            # threes.add(','.join(three))
    print(key, list(connected))

# for three in threes:
#     # print(three)
#     t = False
#     for thr in three.split(","):
#         if thr.startswith("t"):
#             t = True
#     if t:
#         total += 1

result(total)


import sys
sys.path.append("../advent-of-code")
from util import init, load_day, load_file, result
import math
import numpy as np
init()

array = load_day(25, 2023)
part_2 = False
total = 0


import functools
import matplotlib.pyplot as plt
import networkx as nx
import operator
import re


data = [
    re.split(r"-", line)
    for line in open("./2024/txt/day23.txt").read().rstrip().split("\n")
]

G = nx.Graph()
for node, node2 in data:
    G.add_edge(node, node2)

# Uncomment the following two lines to see what edges are to be removed
nx.draw(G, with_labels=True)
plt.show()
# quit()

# Seen surprisingly easily from graph
# G.remove_edge("brd", "clb")
# G.remove_edge("bbz", "jxd")
# G.remove_edge("mxd", "glz")

print(
    "Part 1:",
    functools.reduce(operator.mul, (len(g) for g in nx.connected_components(G)), 1),
)