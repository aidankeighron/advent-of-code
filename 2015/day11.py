import sys
sys.path.append("../advent-of-code")
from util import *
import numpy as np, math
init()

array = load_day(10, 2015)
part_2 = False
total = 0

password = array[0]
password = 'hxbxxyzz'
def increment(passw):
    passw = list(passw)
    passw[-1] = chr(ord(passw[-1]) + 1)
    for i in range(len(passw) - 1, -1, -1):
        if passw[i] == '{':
            passw[i] = 'a'
            if i > 0:
                passw[i - 1] = chr(ord(passw[i - 1]) + 1)
    return ''.join(passw)

def is_valid(password):
    if 'i' in password or 'l' in password or 'o' in password:
        return False
    pair = 0
    pair_chars = []
    for passw, last_passw in zip(password[1:], password[:-1]):
        if passw in pair_chars:
            continue
        if passw == last_passw:
            pair_chars.append(passw)
            pair += 1
    if pair < 2:
        return False
    in_a_row = 0
    max_in_a_row = 0
    for passw, last_passw in zip(password[1:], password[:-1]):
        if ord(passw) == ord(last_passw)+1:
            in_a_row += 1
        else:
            max_in_a_row = max(max_in_a_row, in_a_row)
            in_a_row = 0
    if max_in_a_row+1 <= 2:
        return False
    return True

password = increment(password)
while not is_valid(password):
    password = increment(password)

result(password)