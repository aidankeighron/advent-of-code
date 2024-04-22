import sys
sys.path.append("../advent-of-code")
from util import *
import numpy as np, math, json
init()

array = load_day(12, 2015)
part_2 = False
total = 0

data = json.loads(array[0])

items = [data]
while items:
    item = items.pop()
    if isinstance(item, dict):
        if 'red' in item.values():
            continue
        items.extend(item.values())
    elif isinstance(item, list):
        items.extend(item)
    elif isinstance(item, int):
        total += item
# negative = False
# skip = 0
# for i in range(len(data)-1):
#     if skip > 0:
#         skip -= 1
#         continue
#     if data[i] == '-':
#         negative = True
#     if data[i].isdigit():
#         index = i+1
#         number = data[i]

#         while index < len(data) and data[index].isdigit():
#             number += data[index]
#             index += 1
#             if index >= len(data):
#                 break
#         skip = index - i
#         total += int(number) * (-1 if negative else 1)
#         if negative:
#             negative = False
    

result(total)