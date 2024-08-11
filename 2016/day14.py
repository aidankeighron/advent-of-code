import hashlib
import sys
sys.path.append("../advent-of-code")
from util import *
import numpy as np, math, itertools
from functools import reduce

init()

input_ = 'jlmsuwbz'
# input_ = 'abc'

i = 0
possible = []
tot = 0
while True:
    i += 1

    hash = hashlib.md5((input_+str(i)).encode('utf-8')).hexdigest()
    for _ in range(2016):
        hash = hashlib.md5((hash).encode('utf-8')).hexdigest()

    for p in possible:
        if p[1]+1000 < i:
            possible.remove(p)
            continue
        for j in range(len(hash)-5):
            if len(set(hash[j:j+5])) == 1 and hash[j] == p[0]:
                tot += 1
                print(p, hash, i)
                if tot == 64:
                    result(p[1])
                    quit()
                possible.remove(p)
                break 

    for j in range(len(hash)-3):
        if len(set(hash[j:j+3])) == 1:
            possible.append([hash[j], i])
            break