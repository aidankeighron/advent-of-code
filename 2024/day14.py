import sys
sys.path.append("../advent-of-code")
from util import *
import numpy as np, math, itertools, hashlib
from functools import reduce
from collections import defaultdict

init()

def p_a(arr):
    for line in arr:
        print(''.join(str(x) for x in line))

def to_g(grid, arr, integer):
    grid.append([int(x) if integer else x for x in arr])

array = load_day(14, 2024)
part_2 = False
total = 0

for t in range(0, 10000):

    robots = []
    for line in array:
        x, y, dx, dy = parse_line(line, "p={},{} v={},{}")
        robots.append([int(x), int(y), int(dx), int(dy)])

    wid = 101
    hei = 103
    # wid = 11
    # hei = 7
    grid = [[" "]*wid for _ in range(hei)]
    # grid = [[0]*wid for _ in range(hei)]

    for i, robot in enumerate(robots):
        robot[1] = (robot[1] + robot[3]*t) % hei
        robot[0] = (robot[0] + robot[2]*t) % wid
        grid[robot[1]][robot[0]] = "#"
        # grid[robot[1]][robot[0]] += 1
    # grid = [[" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
    #         [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
    #         [" ", " ", " ", " ", " ", "#", " ", " ", " ", " ", " "],
    #         [" ", " ", " ", " ", "#", "#", "#", " ", " ", " ", " "],
    #         [" ", " ", " ", "#", "#", "#", "#", "#", " ", " ", " "],
    #         [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
    #         [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],]
    # p_a(grid)
    # print("#"*wid)
    starts = []
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "#":
                starts.append([i,j])

    def is_valid(i,j):
        return i in range(hei) and j in range(wid)
    
    for start in starts:
        invalid = False
        for rows in range(1, 3):
            if is_valid(start[0]+rows, start[1]) and grid[start[0]+rows][start[1]] == "#":
                valid = True
                for dy in range(-rows, rows+1):
                    if not is_valid(start[0]+rows, start[1]+dy) or grid[start[0]+rows][start[1]+dy] != "#":
                        valid = False
                        break
                if not valid:
                    invalid = True
                    break
            else:
                invalid = True
                break

        if not invalid:
            print(t)
            p_a(grid)
            print("#"*wid)
    # quads = [0,0,0,0]

    # for i in range(len(grid)):
    #     for j in range(len(grid[0])):
    #         if i > len(grid)//2:
    #             if j > len(grid[0])//2:
    #                 quads[0] += grid[i][j]
    #             elif j < len(grid[0])//2:
    #                 quads[1] += grid[i][j]
    #         elif i < len(grid)//2:
    #             if j > len(grid[0])//2:
    #                 quads[2] += grid[i][j]
    #             elif j < len(grid[0])//2:
    #                 quads[3] += grid[i][j]
    # print(quads)
    # result(quads[0]*quads[1]*quads[2]*quads[3])