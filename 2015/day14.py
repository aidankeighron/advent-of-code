import sys
sys.path.append("../advent-of-code-2023")
from util import *
import numpy as np, math
init()

array = load_day(14, 2015)
part_2 = True
total = 0

# Vixen can fly 8 km/s for 8 seconds, but then must rest for 53 seconds.
reindeer = {}
for line in array:
    name, speed, speed_length, rest_length = parse_line(line, '{} can fly {} km/s for {} seconds, but then must rest for {} seconds.', True)
    total_time = 2503
    if not part_2:
        distance = 0
        while total_time > 0:
            distance += speed * speed_length
            total_time -= speed_length
            if total_time < 0:
                break
            total_time -= rest_length
            total = max(total, distance)
    else:               #   0          1            2
        reindeer[name] = [speed, speed_length, rest_length]
        
                #        0                1           2          3
                # Current Distance, Distance Time, Rest Time, Points
current_stats = {r:[0,0,0,0] for r in reindeer.keys()}        
while total_time > 0:
    for name, stats in reindeer.items():
        if current_stats[name][2] <= 0 and current_stats[name][1] <= 0:
            current_stats[name][0] += stats[0]
            if name == 'Dancer':
                current_stats[name][1] = stats[1]
            else:
                current_stats[name][1] = stats[1]-1
        elif current_stats[name][1] == 1:
            if name != 'Dancer':
                current_stats[name][0] += stats[0]
            current_stats[name][1] = 0
            current_stats[name][2] = stats[2]
        elif current_stats[name][1] > 1:
            current_stats[name][0] += stats[0]
            current_stats[name][1] -= 1
        elif current_stats[name][2] > 0:
            current_stats[name][2] -= 1
            
    max_r = []
    distance_max = 0
    for name, stats in current_stats.items():
        if stats[0] > distance_max:
            distance_max = stats[0]
            max_r = [name]
        elif stats[0] == distance_max:
            max_r.append(name)
    for n in max_r:
        current_stats[n][3] += 1
        
    total_time -= 1
    
result(max(current_stats.values(), key=lambda x: x[3])[3])