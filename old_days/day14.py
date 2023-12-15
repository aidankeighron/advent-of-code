from util import init, load_day, load_file, result
import math
import numpy as np
init()

array = load_day(14)
part_2 = False
total = 0

array = np.array([list(i) for i in array])

def roll(dir_1, array):
    array = np.array(array)
    if dir_1 == 2:
        array = np.rot90(array)
    if dir_1 == 3:
        array = np.rot90(array)
        array = np.rot90(array)
    if dir_1 == 4:
        array = np.rot90(array)
        array = np.rot90(array)
        array = np.rot90(array)
    for i in range(len(array[0])):
        for j, line in enumerate(array[:, 1:i]):
            if array[i, j] == "O":
                index = i
                while array[j, index-1] == ".":
                    array[j, index-1] = "O"
                    array[j, index] = "."
                    index -= 1
            
roll(1, array)        
print(array)
quit()

for i in range(len(array[0])):
    stop = 0
    # o = 0
    load = 0
    for j, char in enumerate(array[:, i]):
        if char == "O":
            load += (len(array[0])-j-1)+1+(-stop)
            print(len(array[0])-j-1)
            # load = o
            # print(load)
        if char == "#":
            stop = j
    print(load)
    quit()
    total += load

result(total)