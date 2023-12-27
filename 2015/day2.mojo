# from util import init, load_day, load_file, result
from math import max
from python import Python

def main():
    Python.add_to_path("/home/aidan/advent-of-code-2023")
    let util = Python.import_module("util")
    util.init()

    var part1 = 0
    var part2 = 0
    let file = open('./2015/txt/day2.txt', 'r').read().split('\n')
    for i in range(len(file)):
        let dim = file[i].split('x')
        let l: Int = atol(dim[0])
        let w: Int = atol(dim[1])
        let h: Int = atol(dim[2])
        extra = l*w*h//max(max(l,w), h)
        part1 += 2*l*w + 2*w*h + 2*h*l + extra
        part2 += l*w*h + 2*l+2*w+2*h-2*max(max(l,w), h)

    util.result(part1)
    util.result(part2)