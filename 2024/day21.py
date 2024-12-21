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

array = load_day(21, 2024)
part_2 = False
total = 0

door = [["7", "8", "9"],
        ["4", "5", "6"],
        ["1", "2", "3"],
        ["#", "0", "A"],]
pad = [["#", "^", "A"],
        ["<", "v", ">"],]

directions = {"^": [-1, 0], "v": [1, 0], ">": [0, 1], "<": [0, -1]}
# directions = {">": [0, 1], "^": [-1, 0], "v": [1, 0], "<": [0, -1]}

@cache
def bfs(node):
    return False

def get_path(start, end, arr, d):
    nodes = [[start, 0, ""]]
    best = [(0,0), float("inf"), ""]
    seen = set()
    while nodes:
        start, distance, path = nodes.pop(0)

        if arr[start[0]][start[1]] == end:
            if distance < best[1]:
                best = [start, distance, path+"A"]
            continue

        if start in seen:
            continue
        seen.add(start)

        # for direction, (dx, dy) in directions.items(): 
        for direction, (dx, dy) in d: 
            x = start[0]+dx
            y = start[1]+dy

            if x not in range(len(arr)) or y not in range(len(arr[0])):
                continue
            if arr[x][y] == "#":
                continue

            nodes.append([(x, y), distance+1, path+direction])
    return best

for line in array:
    other = []
    min_score = float("inf")
    for d in list(itertools.permutations(directions.items())):
        start = (3, 2)
        code_1 = ""
        for end in line:
            p = get_path(start, end, door, d)
            start = p[0]
            code_1 += p[2]
        # print(code_1)
        old_code = code_1
        new_code = ""
        for i in range(25):
            print(i, len(old_code))
            start = (0, 2)
            new_code = ""
            for end in old_code:
                p = get_path(start, end, pad, d)
                start = p[0]
                new_code += p[2]
            old_code = new_code
            # print(code_2)
        # print(code_3)
        # code_2 = ""
        # for end in code_1:
        #     p = get_path(start, end, pad, d)
        #     start = p[0]
        #     code_2 += p[2]
        # # print(code_2)
        # start = (0, 2)
        # code_3 = ""
        # for end in code_2:
        #     p = get_path(start, end, pad, d)
        #     start = p[0]
        #     code_3 += p[2]
        # # print(code_3)

        score = len(new_code) * int(''.join([ch for ch in line if ch.isnumeric()]))
        # print(len(code_3), int(''.join([ch for ch in line if ch.isnumeric()])))
        if score < min_score:
            min_score = score
            other = [len(new_code), int(''.join([ch for ch in line if ch.isnumeric()]))]
            print(min_score, other)
    total += min_score

result(total)