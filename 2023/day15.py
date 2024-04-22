import sys
sys.path.append("../advent-of-code")
from util import init, load_day, load_file, result
import math
import numpy as np
init()

array = load_day(15, 2023)
part_2 = False
total = 0

# box = {}
boxes = [{} for n in range(1, 257)]
for line in array:
    
    line = line.split(",")
    for chars in line:
        current = 0
        for char in chars:
            current += ord(char)
            current *= 17
            current %= 256

        if "=" in chars:
            current = 0
            for char in chars.split("=")[0]:
                current += ord(char)
                current *= 17
                current %= 256
            
            # if chars.split("=")[0] not in boxes[int(current)]:
            boxes[int(current)][chars.split("=")[0]] = chars.split("=")[1]
        if "-" in chars:
            current = 0
            for char in chars.split("-")[0]:
                current += ord(char)
                current *= 17
                current %= 256
            try:
                del boxes[int(current)][chars.split("-")[0]]
            except:
                ...
        # print(boxes)
for i, box in enumerate(boxes):
    if box:
        for j, b in enumerate(box.values()):
            total += (i+1)*(j+1)*(int(b))
        
result(total)