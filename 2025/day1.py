import sys
sys.path.append("../advent-of-code")
from util import *

init()


array = load_day(1, 2025)
part_2 = False
total = 0

grid = []

pointer = 50
for line in array:
    if line[0] == "L":
        line = line.replace("L", "")
        line = int(line)
        for _ in range(line):
            if pointer % 100 == 0:
                total += 1
            pointer -= 1
    else:
        line = line.replace("R", "")
        line = int(line)
        for _ in range(line):
            if pointer % 100 == 0:
                total += 1
            pointer += 1
        # pointer += line

    # print(pointer)

result(total)