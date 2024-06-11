import sys
sys.path.append("../advent-of-code")
from util import *
import numpy as np, math, itertools
from functools import reduce

init()

array = load_day(10, 2016)
part_2 = False
total = 0

bots = {}
values = []

for line in array:
    if line.startswith("bot"):
        bot_num, low, high = parse_line(line, "{} gives low to {} and high to {}")
        bots[bot_num] = {"low": low, "high": high, "current": set()}
        if low.startswith("output"):
            bots[low] = {"current": set()}
        if high.startswith("output"):
            bots[high] = {"current": set()}
    else:
        value, bot_num = parse_line(line, "value {} goes to {}")
        values.append([value, bot_num])

for val, num in values:
    bots[num]["current"].add(int(val))

while True:
    done = 0
    for bot_num, bot in bots.items():
        if bot_num.startswith("output"):
            continue
        if len(bot["current"]) == 2:
            current = list(bot["current"])
            low, high = (current[0], current[1]) if current[0] < current[1] else (current[1], current[0])
            bots[bot["low"]]["current"].add(low)
            bots[bot["high"]]["current"].add(high)
            if low == 17 and high == 61:
                print(bot_num)
                done += 1

    if done:
        print(bots["output 0"])
        print(bots["output 1"])
        print(bots["output 2"])
        # break

result(total)