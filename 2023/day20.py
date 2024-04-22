import sys
sys.path.append("../advent-of-code")
from util import init, load_day, load_file, result
import math
from math import gcd

import numpy as np
init()

array = load_day(20, 2023)
part_2 = False
total = 0

def lcm(xs):
  ans = 1
  for x in xs:
    ans = (ans*x)//math.gcd(x,ans)
  return ans

# start_modules = array[0].split(",")[1:]
# start_modules = [[s.strip(), 0] for s in start_modules]
# 0 == low 1 == high tl, gd, zb, gc
start_modules = [['tl', 0, ''],['gd', 0, ''],['zb', 0, ''],['gc', 0, '']]

# start_modules = [['a', 0, ''],['b', 0, ''],['c', 0, '']]
modules = {}

ampersand_modules = []
for line in array[1:]:
    name, mapping = line.split(" -> ")
    mapping = mapping.split(",")
    mapping = [m.strip() for m in mapping]
    
    if line[0] == '%':
        modules[name[1:]] = [name[0], mapping, 0]
    if line[0] == '&':
        modules[name[1:]] = [name[0], mapping, {}]
        ampersand_modules.append(name[1:])
    # % 0 == off 1 == on
    # & 0 == low 1 == high
    
for name, module in modules.items():
    for m in module[1]:
        if m in ampersand_modules:
            modules[m][2][name] = 0

low = (len(start_modules)+1)*1000
high = 0
cq = 0
jx = 0
tt = 0
qz = 0
watch = ['cq', 'jx', 'tt', 'qz']
last = {w:0 for w in modules.keys()}
count = {w:0 for w in modules.keys()}
for_lcm = []
for i in range(13000):
    next_modules = start_modules.copy()
    while next_modules:
        name, signal, previous = next_modules.pop(0)
        if signal == 0:
            if count[name] == 2 and name in watch:
                for_lcm.append(i-last[name])
                print(i)
            last[name] = i
            count[name] += 1
        if len(for_lcm) == len(watch):
            print(lcm(for_lcm))
            quit()

        if name == 'rx':
            # print(i)
            continue
        module = modules[name]
        if module[0] == '%' and signal == 0:
            next_module = []
            if module[2] == 0:
                module[2] = 1
                new_signal = 1
            else:
                module[2] = 0
                new_signal = 0
            for m in module[1]:
                if new_signal == 0:
                    low += 1
                else:
                    high += 1
                next_module.append([m, new_signal, name])
                
            next_modules.extend(next_module)
        if module[0] == '&':
            module[2][previous] = signal
            if 0 in module[2].values():
                for m in module[1]:
                    next_modules.append([m, 1, name])
                    high += 1
            else:
                for m in module[1]:
                    next_modules.append([m, 0, name])
                    low += 1
    # print(module)
        # quit()
total = low*high
print(low)
print(high)

result(total)