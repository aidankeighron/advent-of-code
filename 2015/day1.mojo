import sys
# from util import init, load_day, load_file, result
import math
# import numpy as np

def main():
    # init()
    var part1 = 0
    var part2 = 0
    let file = open('./2015/txt/day1.txt', 'r').read()
    for i in range(len(file)):
        if file[i] == '(':
            part1 += 1
        else:
            part1 -= 1
        if not part2 and part1 < 0:
            part2 = i
    print(part1)
    print(part2)
            