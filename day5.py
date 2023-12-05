from util import init, load_day, load_file, result
init()

array = load_day(5)
total = 0
part_2 = False

seeds = array[0].split(":")[1].split(" ")[1:]
new = []
for i in range(0, len(seeds), 2):
    # print(seeds[i])
    # print(seeds[i+1])
    new.extend(range(int(seeds[i]),int(seeds[i])+int(seeds[i+1])))
# print(new)
# quit()
seeds = new
print('seeds found')
# print(seeds)
for i, line in enumerate(array[2:]):
    if ":" in line:
        index = i+3
        maps = []
        while array[index] != "":
            maps.append(array[index].split(" "))
            index += 1
            if index > len(array)-1:
                break
        new_seeds = []
        for seed in seeds:
            print(f'{i}/{len(seeds)}')
            new_seed = int(seed)
            for m in maps:
                if int(m[1]) <= int(seed) <= int(m[1])+int(m[2]):
                    # if int(seed) == 77:
                    #     print(m)
                    new_seed = int(seed)-int(m[1])+int(m[0])
                    break
            new_seeds.append(new_seed)
        print(seeds)
        seeds = new_seeds
    # print("***")

result(min(seeds))