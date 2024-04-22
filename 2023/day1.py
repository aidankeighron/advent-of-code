import sys
sys.path.append("../advent-of-code")
from util import init, load_day, load_file, result
init()

words = {"one":"1","two":"2","three":"3","four":"4","five":"5","six":"6","seven":"7","eight":"8","nine":"9"}
total = 0
part_2 = True

for line in load_day(1, 2023):            
    matches = []       
    for i, char in enumerate(line):
        if char.isdigit():
            matches.append([i, int(char)])
            
    if part_2:
        for word, value in words.items():
            if word in line:
                index = line.find(word)
                while True:
                    matches.append([index, int(value)])
                    index = line.find(word, index+1)
                    if index == -1:
                        break
                    
    matches = sorted(matches, key=lambda x: x[0])
    total += matches[-1][1]+matches[0][1]*10

result(total)
# print(total) 
                