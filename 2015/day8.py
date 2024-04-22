import sys
sys.path.append("../advent-of-code")
from util import *
import numpy as np, math, re
init()

array = load_day(8, 2015)
part_2 = False
total = 0

def parse_line(line):
    literal = len(line)
    # line = line.replace('\\\\', 'a')
    # line = line.replace(r'\"', 'a')
    # line = re.sub(r'\\x[0-9a-f]{2}', 'a', line)
    # memory = len(line) - 2
    memory = literal + line.count('\\') + line.count('"') + 2
    return literal, memory

if __name__ == '__main__':
    for line in array:
        literal, memory = parse_line(line)
        total += literal - memory

    result(total)