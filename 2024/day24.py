import sys
sys.path.append("../advent-of-code")
from util import *
import numpy as np, math, itertools, hashlib
from functools import reduce, cache
from collections import defaultdict

init()

def p_a(arr):
    for line in arr:
        print(''.join(str(x) for x in line))

def to_g(grid, arr, integer):
    grid.append([int(x) if integer else x for x in arr])

array = load_day(24, 2024)
part_2 = False
total = 0

gate_fn = {
    "AND": lambda a, b: int(a == 1 and b == 1),
    "OR": lambda a, b: int(a == 1 or b == 1),
    "XOR": lambda a, b: int(a + b == 1),
}
w = True
wires = {}
gates = []
for line in array:
    if line == "":
        w = False
        continue

    if w:
        line = parse_line(line, "{}: {}")
        wires[line[0]] = int(line[1])
    else:
        i1, gate, i2, res = parse_line(line, "{} {} {} -> {}")
        gates.append([i1, gate, i2, res])

# print(wires)
# print(gates)

while gates:
    i1, gate, i2, res = gates.pop(0)

    # Skip
    if i1 not in wires or i2 not in wires:
        gates.append([i1, gate, i2, res])
        continue

    i1 = wires[i1]
    i2 = wires[i2]
    out = gate_fn[gate](i1, i2)
    wires[res] = out

z = {int(w.replace("z", "")): val for w, val in wires.items() if w.startswith("z")}
z = dict(sorted(z.items(), key=lambda item: item[0], reverse=True))
z_out = ''.join(map(str, z.values()))
print(z_out)

x = {int(w.replace("x", "")): val for w, val in wires.items() if w.startswith("x")}
x = dict(sorted(x.items(), key=lambda item: item[0], reverse=True))
x_out = ''.join(map(str, x.values()))

y = {int(w.replace("y", "")): val for w, val in wires.items() if w.startswith("y")}
y = dict(sorted(y.items(), key=lambda item: item[0], reverse=True))
y_out = ''.join(map(str, y.values()))
# 7, 8, 11, 18, 19, 35
xy = bin(int(x_out, 2) + int(y_out, 2))[2:]
print(xy)
for i, (z_b, xy_b) in enumerate(zip(str(z_out), str(xy))):
    if z_b != xy_b:
        print(z_b, xy_b, len(str(z_out))+~i)

# z07, z08
# z18, z19
# z40, z41
result(int(z_out, 2))