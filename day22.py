from util import init, load_day, load_file, result
import math
from copy import deepcopy
import numpy as np
init()

array = load_day(22)
part_2 = False
total = 0

bricks = []
for line in array:
    start, end = line.split("~")
    start = start.split(",")
    start = list(map(int, start))
    end = end.split(",")
    end = list(map(int, end))
    brick = []
    if start[0] != end[0]:
        for i in range(start[0], end[0]+1):
            brick.append([i, start[1], start[2]])
    elif start[1] != end[1]:
        for i in range(start[1], end[1]+1):
            brick.append([start[0], i, start[2]])
    else:
        for i in range(start[2], end[2]+1):
            brick.append([start[0], start[1], i])
    bricks.append(brick)
    
# bricks = sorted(bricks, key=lambda brick: brick[0][2])

seen = set()
for brick in bricks:
  for (x,y,z) in brick:
    seen.add((x,y,z))

while True:
  movement = False
  for i, brick in enumerate(bricks):
    can_move = True
    for (x,y,z) in brick:
      if z == 1:
        can_move = False
      if (x,y,z-1) in seen and (x,y,z-1) not in brick:
        can_move = False
    if can_move:
      movement = True
      for (x,y,z) in brick:
        seen.discard((x,y,z))
        seen.add((x,y,z-1))
      bricks[i] = [(x,y,z-1) for (x,y,z) in brick]
  if not movement:
    break

old_seen = deepcopy(seen)
old_bricks = deepcopy(bricks)

for i, brick in enumerate(bricks):
    seen = deepcopy(old_seen)
    bricks = deepcopy(old_bricks)

    for (x,y,z) in brick:
        seen.discard((x,y,z))

    fall = set()
    while True:
        movement = False
        for j, other_brick in enumerate(bricks):
            if j == i:
                continue
            can_move = True
            for (x,y,z) in other_brick:
                if z == 1:
                    can_move = False
                if (x,y,z-1) in seen and (x,y,z-1) not in other_brick:
                    can_move = False
            if can_move:
                fall.add(j)
                for (x,y,z) in other_brick:
                    seen.discard((x,y,z))
                    seen.add((x,y,z-1))
                bricks[j] = [(x,y,z-1) for (x,y,z) in other_brick]
                movement = True
        if not movement:
            break
        # if len(fall)==0:
            # total += 1
        total += len(fall)


result(total)