from util import init, load_day, load_file, result
init()

array = load_day(4)
total = 0
part_2 = False

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
