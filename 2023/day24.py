from util import *
import math
import numpy as np
init()

array = load_day(24, 2023)
part_2 = False
total = 0

lines = []
for line in array:
    x_coords, y_coords, z, vx, vy, vz = parse_line(line, '{}, {}, {} @ {}, {}, {}')
    x_coords, y_coords, z, vx, vy, vz = int(x_coords), int(y_coords), int(z), int(vx), int(vy), int(vz)
    y_init = (vy/vx)*(-x_coords)+y_coords
    lines.append((y_init, (vy/vx), x_coords, y_coords, vx, vy))
    
for i, line in enumerate(lines):
    for j, other_line in enumerate(lines[i:]):
        if i == j:
            continue
        if line[1] == other_line[1]:
            continue
        x_pos = -(line[0]-other_line[0])/(line[1]-other_line[1])
        # print(f'{line[2]} {line[3]}')
        # print(f'{other_line[2]} {other_line[3]}')
        y_pos = line[0]+line[1]*x_pos
        if line[4] < 0 and x_pos > line[2]:
            continue
        if other_line[4] < 0 and x_pos > other_line[2]:
            continue
        if line[4] > 0 and x_pos < line[2]:
            continue
        if other_line[4] > 0 and x_pos < other_line[2]:
            continue
        # 15318
        if line[5] < 0 and y_pos > line[3]:
            continue
        if other_line[5] < 0 and y_pos > other_line[3]:
            continue
        if line[5] > 0 and y_pos < line[3]:
            continue
        if other_line[5] > 0 and y_pos < other_line[3]:
            continue
        # if vx > 0
        if 200000000000000 < x_pos < 400000000000000 and 200000000000000 < y_pos < 400000000000000:
        # if 7 < x_pos < 27 and 7 < y_pos < 27:
            total += 1
        
    

result(total)