import sys
sys.path.append("../advent-of-code")
from util import *
import numpy as np, math, itertools
from functools import reduce
import hashlib

init()

array = "cxdnnyjw"
total = ['_','_','_','_','_','_','_','_']

i = 0
while True:
    i += 1
    out = hashlib.md5((array+str(i)).encode('utf-8')).hexdigest()

    if out.startswith('00000'):
        if 48 <= ord(out[5]) <= 55 and total[int(out[5])] == "_":
            total[int(out[5])] = out[6]
    if all(t != "_" for t in total):
        break

result(''.join(total))