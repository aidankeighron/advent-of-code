import re
import sys
sys.path.append("../advent-of-code")
from util import *
import numpy as np, math, itertools, hashlib
from functools import reduce

init()

array = load_day(3, 2024)
part_2 = False
total = 0

tot = ""
for line in array:
    tot += line

mul = tot.find("mul(")
start = 0
next_dont = tot.find("don't()")
enabled = True
while mul != -1:
    mul = tot.find("mul(", start+1)

    while next_dont < mul:
        # print("here")
        next_do = tot.find("do()", next_dont+1)
        next_dont = tot.find("don't()", next_do+1)
        start = next_do+1
        mul = tot.find("mul(", start+1)

    comma = tot.find(",", mul+1)
    end = tot.find(")", comma+1)

    num1 = tot[mul+4:comma]
    num2 = tot[comma+1:end]

    # print(tot[mul:end+1], mul)
    try:
        # if len(str(int(num1))) == comma-(mul+4):
        #     if len(str(int(num2))) == end-(comma+1):
        # if num1 != "4":
        if enabled:
            total += int(num1) * int(num2)
            print(tot[mul:end+1], mul)
            # print(num1, num2)
    except:
        ...
    # print(tot[comma+1:end])

    start = mul
    if num1 == "118" and num2 == "135":
        break
    # quit()

result(total)