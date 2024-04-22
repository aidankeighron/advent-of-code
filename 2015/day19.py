import sys
sys.path.append("../advent-of-code")
from util import *
import numpy as np, math
init()
def n_upper_chars(string):
    return sum([int(c.isupper()) for c in string])
print(n_upper_chars("CRnCaCaCaSiRnBPTiMgArSiRnSiRnMgArSiRnCaFArTiTiBSiThFYCaFArCaCaSiThCaPBSiThSiThCaCaPTiRnPBSiThRnFArArCaCaSiThCaSiThSiRnMgArCaPTiBPRnFArSiThCaSiRnFArBCaSiRnCaPRnFArPMgYCaFArCaPTiTiTiBPBSiThCaPTiBPBSiRnFArBPBSiRnCaFArBPRnSiRnFArRnSiRnBFArCaFArCaCaCaSiThSiThCaCaPBPTiTiRnFArCaPTiBSiAlArPBCaCaCaCaCaSiRnMgArCaSiThFArThCaSiThCaSiRnCaFYCaSiRnFYFArFArCaSiRnFYFArCaSiRnBPMgArSiThPRnFArCaSiRnFArTiRnSiRnFYFArCaSiRnBFArCaSiRnTiMgArSiThCaSiThCaFArPRnFArSiRnFArTiTiTiTiBCaCaSiRnCaCaFYFArSiThCaPTiBPTiBCaSiThSiRnMgArCaF"))
# part 2
# elements - count(Ar) - count(Rn) - count(Y)*2 - 1    
quit()

array = load_day(19, 2015)
part_2 = False
total = 0

options = {}
string = ""
for line in array:
    if "=>" in line:
        right, left = line.split(" => ")
        if right not in options:
            options[right] = []
        options[right].append(left)
    else:
        string = line

steps_list = []
seen = set()
def dfs(i, cur, steps):
    if cur == string:
        steps_list.append(steps)
        print(steps)
        return
    if len(cur) >= len(string):
        return
    if cur in seen:
        return
    if i >= len(cur):
        dfs(0, cur, steps)
    
    for o in options:
        if i+len(o) > len(cur):
            continue
        if cur[i:i+len(o)] == o:
            for option in options[o]:
                seen.add(cur)
                dfs(i+len(option), cur[:i] + option + cur[i+len(o):], steps+1)
    seen.add(cur)
    dfs(i+1, cur, steps+1)

# res = set()
# def dfs(i, cur):
#     if i >= len(cur):
#         res.add(cur)
#         return
    
#     for o in options:
#         if cur[i:i+len(o)] == o:
#             for option in options[o]:
#                 res.add(cur[:i] + option + cur[i+len(o):])
#                 # dfs(i+len(option), cur[:i] + option + cur[i+len(o):])
#     dfs(i+1, cur)

dfs(0, "e", 0)

result(min(steps_list))
