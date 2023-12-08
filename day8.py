from util import init, load_day, load_file, result, format
import math
init()

array = load_day(8)
part_2 = False
total = 0

path = {}
current = []
end = []
for line in array[2:]:
    key, path1, path2 = format(line, "{} = ({}, {})")
    if key[2] == "A":
        current.append(key)
    if key[2] == "Z":
        end.append(key)
    path[key] = [path1, path2]

# end = 'QKJ'
# end = 'ZZZ'
# current = 'BQV'
# current = 'AAA'
found = False
while not found:
    for char in array[0]:
        current = [path[c][0 if char == 'L' else 1] for c in current]
        total += 1
        for c in current:
            if c not in end:
                break
        else:
        # if current == end:
            found = True
            break      

result(total)