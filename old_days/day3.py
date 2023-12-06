from util import init, load_day, load_file, result
init()

part_2 = True
total = 0
array = load_day(3, True)

def find_number(i, j):
    number = [[j, int(array[i][j])]]
    index = j
    while array[i][index-1].isdigit():
        number.append([index-1, int(array[i][index-1])])
        index -= 1
        if (index-1) < 0:
            break
    index = j
    while array[i][index+1].isdigit():
        number.append([index+1, int(array[i][index+1])])
        index += 1
        if (index+1) > len(array[i])-1:
            break
    return int(''.join([str(char[1]) for char in sorted(number, key=lambda x: x[0])]))
    
for i, line in enumerate(array):
    for j, char in enumerate(line):
        numbers = set()
        if (part_2 and char == "*") or (not char.isdigit() and char != '.'):
            if array[i+1][j+1].isdigit():
                numbers.add(find_number(i+1, j+1))
            if array[i+1][j].isdigit():
                numbers.add(find_number(i+1, j))
            if array[i+1][j-1].isdigit():
                numbers.add(find_number(i+1, j-1))
            if array[i][j+1].isdigit():
                numbers.add(find_number(i, j+1))
            if array[i][j-1].isdigit():
                numbers.add(find_number(i, j-1))
            if array[i-1][j+1].isdigit():
                numbers.add(find_number(i-1, j+1))
            if array[i-1][j].isdigit():
                numbers.add(find_number(i-1, j))
            if array[i-1][j-1].isdigit():
                numbers.add(find_number(i-1, j-1))
        if part_2:
            if len(numbers) == 2:
                total += numbers.pop()*numbers.pop()
        else:
            total += sum(numbers)
        
result(total)
# print(total) 
                