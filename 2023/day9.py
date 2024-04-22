import sys
sys.path.append("../advent-of-code")
from util import init, load_day, load_file, result
import math
init()

array = load_day(9, 2023)
part_2 = False
total = 0

for line in array:
    numbers = line.split()
    difference = [[int(n) for n in numbers]]
    while True:
        new_numbers = []
        for i in range(len(difference[-1])-1):
            new_numbers.append(difference[-1][i+1]-difference[-1][i])
        difference.append(new_numbers)
        if new_numbers[-1] == 0:
            break
    
    new_num = 0
    # print(difference)
    for i, number in enumerate(difference[::-1]):
        if i == len(difference)-1:
            break
        change = difference[-i-2][0]
        new_num = change-number[0]
        difference[-i-2].insert(0, new_num)
    # print(difference)
    # print(new_num)
    # print(difference)
    # print("**")
    # quit()
    total += new_num
        
        

result(total)