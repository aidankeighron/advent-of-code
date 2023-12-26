import sys
sys.path.append("../advent-of-code-2023")
from util import init, load_day, load_file, result
init()

array = load_day(4, 2023)
total = 0
part_2 = False

if part_2:
    number_of_copies = []
    for line in array:
        numbers, winning = line.split("|")
        winning = winning.split(" ")
        numbers = numbers.split(":")[1].split(" ")
        
        copies = 0
        for num in numbers:
            if num != '' and num in winning:
                copies += 1
        number_of_copies.append(copies)

    new_array = [1]*len(number_of_copies)
    for i, copies in enumerate(number_of_copies):
        for copy in range(copies):
            try:
                new_array[i+copy+1] += 1*new_array[i]
            except:
                ...

    result(sum(new_array))
else:
    for line in array:
        numbers, winning = line.split("|")
        winning = winning.split(" ")
        numbers = numbers.split(":")[1].split(" ")
        score = 0
        
        for num in numbers:
            if num != '' and num in winning:
                if score == 0:
                    score = 1
                else:
                    score *= 2
        total += score

    result(total)

