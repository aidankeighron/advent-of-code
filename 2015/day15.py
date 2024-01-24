import sys
sys.path.append("../advent-of-code-2023")
from util import *
import numpy as np, math
from functools import reduce
init()

array = load_day(15, 2015)
part_2 = False
total = 0

ingredients = {}
amounts = [0, 0, 0, 0]
for line in array:
    name, capacity, durability, flavor, texture, calories = parse_line(line, '{}: capacity {}, durability {}, flavor {}, texture {}, calories {}')
    ingredients[name] = [int(capacity), int(durability), int(flavor), int(texture), int(calories)]
    
def score(ingredients, amounts):
    score = [0, 0, 0, 0, 0]
    for ingredient, amount in zip(ingredients.values(), amounts):
        for i, count in enumerate(ingredient):
            score[i] += count * amount
    if score[-1] != 500:
        return 0
    return reduce(lambda x, y: x * y, [max(x, 0) for x in score[:-1]])

for i in range(0, 100):
    for j in range(0, 100-i):
        for k in range(0, 100-i-j):
            amounts = [i, j, k, 100-i-j-k]
            total = max(total, score(ingredients, amounts))

result(total)