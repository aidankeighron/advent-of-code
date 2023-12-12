from util import init, load_day, load_file, result
import math
import numpy as np
init()

array = load_day(12)
part_2 = False
total = 0

def is_valid(line, nums):
    line = ''.join(line).split(".")
    current = 0
    for char in line:
        if "#" in char:
            if current > len(nums)-1:
                return False
            if len(char) != int(nums[current]):
                return False
            current += 1
    return current == len(nums)

for line in array:
    # print("Line")
    line *= 5
    chars, nums = line.split()
    chars = list(chars)
    nums = nums.split(",")
    options = [chars]
    loop = True
    while loop:
        no = 0
        for i, option in enumerate(options):
            leave = False
            for j, char in enumerate(option):
                if char == "?":
                    options.append(option[:j]+['#']+option[j+1:])
                    options.append(option[:j]+['.']+option[j+1:])
                    del options[i]
                    leave = True
                    break
            if "?" not in option:
                no += 1
            if leave:
                break
        if no >= len(options)-1:
            loop = False
        
    for option in options:
        total += int(is_valid(option, nums))

result(total)