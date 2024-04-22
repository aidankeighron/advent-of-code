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
    re.split(r"(?:: )| ", line)
    for line in open("./txt/day25.txt").read().rstrip().split("\n")
]

G = nx.Graph()
for node, *nodes in data:
    for node2 in nodes:
        G.add_edge(node, node2)

# Uncomment the following two lines to see what edges are to be removed
nx.draw(G, with_labels=True)
plt.show()
# quit()

# Seen surprisingly easily from graph
G.remove_edge("brd", "clb")
G.remove_edge("bbz", "jxd")
G.remove_edge("mxd", "glz")

print(
    "Part 1:",
    functools.reduce(operator.mul, (len(g) for g in nx.connected_components(G)), 1),
)
# cables = {}
# for line in array:
#     one, others = line.split(":")
#     if " " in others[1:]:
#         others = others.split(" ")[1:]
#     else:
#         others = [others[1:]]
#     if one not in cables:
#         cables[one] = []

#     cables[one].extend(others)
#     for other in others:
#         if other not in cables:
#             cables[other] = []
#         cables[other].append(one)
        
# def check_loop():
#     start = list(cables.keys())[0]
#     nodes = [start]
#     seen = set()
#     while nodes:
#         node = nodes.pop(0)
#         if node in seen:
#             continue
#         seen.add(node)
#         nodes.extend(cables[node])
    
# print(seen)
    
        

result(total)