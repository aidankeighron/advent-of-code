from python import Python

def main():
    Python.add_to_path("/home/aidan/advent-of-code-2023")
    let util = Python.import_module("util")
    util.init()

    var part1 = 0
    var part2 = 0
    let file = open('./2015/txt/day1.txt', 'r').read()

    util.result(part1)
    util.result(part2)
            