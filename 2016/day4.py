import string
import sys
sys.path.append("../advent-of-code")
from util import *
import numpy as np, math, itertools
from functools import reduce
from collections import Counter

init()

array = load_day(4, 2016)
part_2 = False
total = 0

def caesar(plaintext, shift): 

    shift %= 26 # Values greater than 26 will wrap around

    alphabet_lower = string.ascii_lowercase
    alphabet_upper = string.ascii_uppercase

    shifted_alphabet_lower = alphabet_lower[shift:] + alphabet_lower[:shift]
    shifted_alphabet_upper = alphabet_upper[shift:] + alphabet_upper[:shift]

    alphabet = alphabet_lower + alphabet_upper 
    shifted_alphabet = shifted_alphabet_lower + shifted_alphabet_upper

    table = str.maketrans(alphabet, shifted_alphabet) 

    return plaintext.translate(table)

for line in array:
    line = line.split('-')
    name = line[:-1]
    name = ''.join(name)
    code = line[-1]
    sec_id = code.split("[")[0]
    name = caesar(name, int(sec_id))
    if 'north' in name:
        print(name, sec_id)
    checksum = code.split('[')[1].replace("]", '')
    count = dict(Counter(name))
    count = dict(sorted(count.items(), key=lambda x: x[1], reverse=True))
    last_amm = len(name)+1
    for check in checksum:
        if check not in count:
            break
        cur_amm = count[check]
        if cur_amm > last_amm:
            break
        del count[check]
        if not all(cur_amm >= amm for amm in count.values()):
            break
        last_amm = cur_amm
    else:
        total += int(sec_id)
        
    

result(total)