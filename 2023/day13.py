import sys
sys.path.append("../advent-of-code-2023")
from util import init, load_day, load_file, result
import math
import numpy as np
init()

array = load_day(13, 2023)
part_2 = False
total = 0


section = []
rows = []
cols = []
for line in array:
    if line != "":
        section.append(line)
    else:
        for i in range(len(section[0])):
            if i == 0 or i >= len(section[0])-2:
                continue
            if i > (len(section[0])-1)//2:
                z = i-(len(section[0])-1-i)
                sub_section = [s[z-1:i]+s[i:] for s in section]
                ...
            else:
                sub_section = [s[:i]+s[i:2*i] for s in section]
                ...
            
            sub_section = np.array([list(s) for s in sub_section])
            not_symetric = False
            differences = 0
            for j in range(len(sub_section[0])//2):
                differences += sum([1 for a, b in zip(list(sub_section[:,j]), list(sub_section[:,~j])) if a != b])

                # if not np.array_equal(sub_section[:,j], sub_section[:,~j]):
                #     not_symetric = True
                #     break
            not_symetric = True if differences != 1 else False
            if not not_symetric:
                rows.append(i)
                section = []
                break
        if not not_symetric:
            continue
            
        section = np.array([np.array(list(l)) for l in section])
        section = np.rot90(section)
        section = list([list(l) for l in section])

        for i in range(len(section[0])):
            if i == 0 or i >= len(section[0])-2:
                continue
            if i > (len(section[0])-1)//2:
                z = i-(len(section[0])-1-i)
                sub_section = [s[z-1:i]+s[i:] for s in section]
                ...
            else:
                sub_section = [s[:i]+s[i:2*i] for s in section]
                ...
            sub_section = np.array([list(s) for s in sub_section])
            not_symetric = False
            differences = 0
            for j in range(len(sub_section[0])//2):
                differences += sum([1 for a, b in zip(list(sub_section[:,j]), list(sub_section[:,~j])) if a != b])
                # if not np.array_equal(sub_section[:,j], sub_section[:,~j]):
                #     not_symetric = True
                #     break
            not_symetric = True if differences != 1 else False
            if not not_symetric:
                cols.append(i)
                section = []
                break
        section = []
        
        
total = sum(rows) + sum(cols)*100  

result(total)