import sys
sys.path.append("../advent-of-code")
from util import *
import numpy as np, math, itertools, hashlib
from functools import reduce
from collections import defaultdict

def comp(a):
    partial = (a % 8) ^ 1
    return ((partial ^ 5) ^ (a>>partial) % 8)


O = []
def func(a):
    global B

    partial = (a % 8) ^ 1
    O.append((partial ^ 5) ^ (a>>partial) % 8)
    a = a>>3
    if a != 0:
        func(a)

# from u/Verulean314
def solve():
    program = [int(x) for x in"2,4,1,1,7,5,1,5,4,1,5,5,0,3,3,0".split(",")]
    meta_inputs = { 0 }
    for num in reversed(program):
        new_meta_inputs = set()
        for curr_num in meta_inputs:
            for new_segment in range(8):
                new_num = (curr_num << 3) + new_segment
                if comp(new_num) == num:
                    new_meta_inputs.add(new_num)
        meta_inputs = new_meta_inputs
    return min(meta_inputs)

func(17323786)
print(O)
print(O==[7, 4, 2, 5, 1, 4, 6, 0, 4])

print(solve())
print(solve() == 164278764924605)

# init()

# save = 0
# while True:
#     a, b, c = save, 0, 0
#     # a, b, c = 0, 2024, 43690
#     # program = "0,1,5,4,3,0".split(",")
#     # program = "4,0".split(",")
#     program = "2,4,1,1,7,5,1,5,4,1,5,5,0,3,3,0".split(",")
#     pc = 0

#     out = []
#     while pc < len(program):
#         instruction = int(program[pc])
#         operand = int(program[pc+1])
        
#         combo = operand
#         if combo == 4: #
#             combo = a
#         elif combo == 5:
#             combo = b
#         elif combo == 6: #
#             combo = c
#         elif combo == 7:
#             combo = -1
#             print("Invalid")

#         if instruction == 0: #
#             r = a//(2**combo)
#             a = int(r)
#         elif instruction == 1: #
#             b = b ^ operand
#         elif instruction == 2: #
#             r = combo % 8
#             b = r
#         elif instruction == 3: #
#             if a != 0:
#                 pc = operand
#                 continue
#         elif instruction == 4: #
#             r = b ^ c
#             b = r
#         elif instruction == 5: #
#             r = combo % 8
#             out.append(str(r))
#         elif instruction == 6:
#             r = a//(2**combo)
#             b = int(r)
#         elif instruction == 7:
#             r = a//(2**combo)
#             c = int(r)
        
#         print("a =", a,"b =", b,"c =", c)
#         pc += 2
#     if out == program:
#         break
#     save += 1
# print(out)
# result("".join(out))
# result(save)