from util import init, load_day, load_file, result
import math
init()

array = load_day(5)
total = 0

seeds = array[0].split(":")[1].split(" ")[1:]
new = []
min_seed = math.inf
min_start = 0
batch = 0
for i in range(0, len(seeds), 2):
    current_seeds = range(int(seeds[i]),int(seeds[i])+int(seeds[i+1]), int(math.sqrt(int(seeds[i+1]))))
    for k, line in enumerate(array[2:]):
        if ":" in line:
            index = k+3
            maps = []
            while array[index] != "":
                maps.append(array[index].split(" "))
                index += 1
                if index > len(array)-1:
                    break
            new_seeds = []
            indexes = []
            for j, seed in enumerate(current_seeds):
                print(f'{j}/{len(current_seeds)}')
                new_seed = int(seed)
                for m in maps:
                    if int(m[1]) <= int(seed) <= int(m[1])+int(m[2]):
                        new_seed = int(seed)-int(m[1])+int(m[0])
                        break
                new_seeds.append(new_seed)
                indexes.append(j)

            current_seeds = new_seeds
            current_indexes = indexes
    current_min = min_seed
    for seed, index in zip(current_seeds, current_indexes):
        if int(seed) < min_seed:
            min_seed = int(seed)
            min_start = int(index)
            batch = i

current_seeds = range(int(seeds[batch]),int(seeds[batch])+int(seeds[batch+1]), int(math.sqrt(int(seeds[batch+1]))))
start_seed = current_seeds[min_start] 

# assumes its not negaive
current_seeds = range(start_seed-int(math.sqrt(int(seeds[batch+1]))),start_seed+int(math.sqrt(int(seeds[batch+1]))))

for k, line in enumerate(array[2:]):
    if ":" in line:
        index = k+3
        maps = []
        while array[index] != "":
            maps.append(array[index].split(" "))
            index += 1
            if index > len(array)-1:
                break
        new_seeds = []
        indexes = []
        for j, seed in enumerate(current_seeds):
            print(f'{j}/{len(current_seeds)}')
            new_seed = int(seed)
            for m in maps:
                if int(m[1]) <= int(seed) <= int(m[1])+int(m[2]):
                    new_seed = int(seed)-int(m[1])+int(m[0])
                    break
            new_seeds.append(new_seed)
            indexes.append(j)

        current_seeds = new_seeds
        current_indexes = indexes
current_min = min_seed
for seed, index in zip(current_seeds, current_indexes):
    if int(seed) < min_seed:
        min_seed = int(seed)

result(min_seed)