import sys
sys.path.append("../advent-of-code-2023")
from util import init, load_day, load_file, result
import math
import numpy as np
from copy import deepcopy
init()

array = load_day(19, 2023)
part_2 = False
total = 0

is_parts = False
workflows = {}
# parts = []
for line in array:
    if line == '':
        is_parts = True
        continue
    if not is_parts:
        key, rule = line.split("{")
        workflows[key] = rule
    # else:
    #     parts.append(line)

all_rules = ["in"]
requirements = [{'x':[1, 4000], 'm':[1, 4000], 'a':[1, 4000], 's':[1, 4000]}]
ending = []
while all_rules:
    rules = workflows[all_rules.pop()]
    requirement = requirements.pop()
    rules = rules.split(",")
    rules[-1] = rules[-1][:-1]
    for i, rule in enumerate(rules):
        if rule[-1] == 'R':
            continue
        if i == len(rules)-1:
            if rule[-1] == 'A':
                ending.append(requirement)
                continue
            all_rules.append(rule)
            requirements.append(requirement)
            continue
        rule, next_ = rule.split(":")
        r = deepcopy(requirement)
        if rule[1] == '<':
            r[rule[0]] = [r[rule[0]][0], min(r[rule[0]][1], int(rule[2:])-1)]
        if rule[1] == '>':
            r[rule[0]] = [max(int(rule[2:])+1, r[rule[0]][0]), r[rule[0]][1]]
            # r[rule[0]] = 4000-int(rule[2:])-1
        if next_ == 'A':
            ending.append(r)
            continue
        all_rules.append(next_)
        requirements.append(r)
    # print(requirements)
for e in ending:
    print(e)
for end in ending:
    m = 1
    for v in end.values():
        m*=v[1]-v[0]+1
    total += m
    # print(e)
        
            
    # print(rules)
    
# quit()
      
# accepted = []
# for part in parts:
#     values = part.split(",")
#     values[0] = values[0][1:]
#     values[-1] = values[-1][:-1]
#     rule = workflows["in"]
#     leave = False
#     while not leave:
#         rules = rule.split(",")
#         rules[-1] = rules[-1][:-1]
#         for rule in rules:
#             if rule == rules[-1]:
#                 next_rule = rules[-1]
#                 break
#                 # quit()
#             next_rule = ''
#             if ":" in rule:
#                 rule, next_ = rule.split(":")
#                 for value in values:
#                     if rule[0] == value[0]:
#                         if rule[1] == "<" and int(rule[2:]) > int(value[2:]):
#                             next_rule = next_
#                         if rule[1] == ">" and int(rule[2:]) < int(value[2:]):
#                             next_rule = next_
#                 if next_rule != '':
#                     break
#         if next_rule == 'A':
#             total += sum([int(value[2:]) for value in values])
#             leave = True
#             break
#         elif next_rule == 'R':
#             leave = True
#             break
#         # print(next_rule)
#         rule = workflows[next_rule]
#     # quit()
        
            
            
                        
        

result(total)