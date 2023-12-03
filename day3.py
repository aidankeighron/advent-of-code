
part_2 = True
total = 0
array = []
with open('day3.txt', 'r') as file:
    while True:

        line = file.readline().replace('\n', '')
        if not line:
            break
        array.append(list(line))
        
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
        if not char.isdigit() and char != '.':
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
        total += sum(numbers)
        
print(total) 
                