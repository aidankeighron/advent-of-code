import sys
sys.path.append("../advent-of-code")
from util import init, load_day, load_file, result
init()
array = load_day(5, 2023)
total = 0

seeds = array[0].split(":")[1].split(" ")[1:]

for i, line in enumerate(array[2:]):
    if ":" in line:
        index = i+3
        maps = []
        while array[index] != "":
            maps.append(array[index].split(" "))
            if index > len(array)-1:
                break
        new_seeds = []
        for seed in seeds:
            new_seed = int(seed)
            for m in maps:
                if int(m[1]) <= int(seed) <= int(m[1])+int(m[2]):
                    new_seed = int(seed)-int(m[1])+int(m[0])
                    break
            new_seeds.append(new_seed)
        seeds = new_seeds

result(min(seeds))