import sys
sys.path.append("../advent-of-code-2023")
from util import *
import numpy as np, math
from itertools import permutations
from collections import defaultdict
init()

array = load_day(9, 2015)
part_2 = False
total = 0

places = set()
cities = defaultdict(dict)
for line in array:
    city, distance = line.split(" = ")
    source, destination = city.split(" to ")
    places.add(source)
    places.add(destination)
    cities[source][destination] = int(distance)
    cities[destination][source] = int(distance)

shortest = math.inf
longest = 0
for items in permutations(cities):
    distance = sum(map(lambda x, y: cities[x][y], items[:-1], items[1:]))
    shortest = min(shortest, distance)
    longest = max(longest, distance)


result(shortest)
result(longest)