import sys
sys.path.append("../advent-of-code")
import util
import hashlib

util.init()

part1 = 0
part2 = 0
input_ = 'iwrupvqb'

i = 0
while True:
    i += 1
    hash = hashlib.md5((input_+str(i)).encode('utf-8')).hexdigest()
    # print(hash) 
    if hash.startswith('00000'):
        part1 = input_+str(i)
    if hash.startswith('000000'):
        part2 = input_+str(i)
        break
    

util.result(part1)
util.result(part2)
            