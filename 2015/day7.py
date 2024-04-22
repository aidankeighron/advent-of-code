import sys
sys.path.append("../advent-of-code")
from util import *
import numpy as np, math
init()

array = load_day(7, 2015)
part_2 = False
total = 0

wires = {}
rules = {}

def find_rule(line):
    inp, out = line.split(" -> ")
    if inp.count(" ") == 0:
        opp = 'SET'
        try:
            inp = int(inp)
            opp = 'SET_N'
        except:
            ...
        return inp, opp, '', out
    if not inp.startswith("NOT"):
        left, opp, right = inp.split(" ")
    else:
        opp, right = inp.split(" ")
        left = ''
    return left, opp, right, out
    
    # lf AND lq -> ls
for line in array:
    left, opp, right, out = find_rule(line)
    rules[out] = (left, opp, right, out)
    
def momoize(func):
    memoized = {}
    def inner(number, rules):
        if number not in memoized:
            memoized[number] = func(number, rules)
        return memoized[number]
    return inner


@momoize
def get_value(wire, local_rules):
    rule = local_rules[wire]
    if rule[1] == 'SET':
        return get_value(rule[0], local_rules)
    if rule[1] == 'SET_N':
        return rule[0]
    if rule[1] == 'AND':
        try:
            int(rule[0])
            return int(rule[0]) & get_value(rule[2], local_rules)
        except:
            ...
        return get_value(rule[0], local_rules) & get_value(rule[2], local_rules)
    if rule[1] == 'OR':
        return get_value(rule[0], local_rules) | get_value(rule[2], local_rules)
    if rule[1] == 'LSHIFT':
        return get_value(rule[0], local_rules) << int(rule[2])
    if rule[1] == 'RSHIFT':
        return get_value(rule[0], local_rules) >> int(rule[2])
    if rule[1] == 'NOT':
        return ~get_value(rule[2], local_rules) & 0xffff
    return 0

if __name__ == '__main__':
    total = get_value('a', rules)

result(total)