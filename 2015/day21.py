import sys
sys.path.append("../advent-of-code-2023")
from util import *
import numpy as np, math, itertools
init()

array = load_day(21, 2015)

boss_hp = 104
boss_damage = 8
boss_armor = 1

def simulate(player_hp, player_damage, player_armor):
    hp = boss_hp
    while True:
        hp -= max(1, player_damage - boss_armor)
        if hp <= 0:
            return True
        player_hp -= max(1, boss_damage - player_armor)
        if player_hp <= 0:
            return False

weapons = [[8,4,0],[10,5,0],[25,6,0],[40,7,0],[74,8,0]]
armor = [[13,0,1],[31,0,2],[53,0,3],[75,0,4],[102,0,5]]
rings = [[25,1,0],[50,2,0],[100,3,0],[20,0,1],[40,0,2],[80,0,3]]


armor.append([0, 0, 0]) # making not wearing armor possible
rings.append([0, 0, 0]) # same for rings
rings.append([0, 0, 0])

m = 1e100
for i0 in weapons:
    for i1 in armor:
        for i2, i3 in itertools.combinations(rings, 2):
            php = 100
            cost = i0[0] + i1[0] + i2[0] + i3[0]
            player_damage = i0[1] + i1[1] + i2[1] + i3[1]
            player_armor = i0[2] + i1[2] + i2[2] + i3[2]
            if simulate(php, player_damage, player_armor):
                m = min(m, cost)
print(m)

m = -1e100
for i0 in weapons:
    for i1 in armor:
        for i2, i3 in itertools.combinations(rings, 2):
            php = 100
            cost = i0[0] + i1[0] + i2[0] + i3[0]
            player_damage = i0[1] + i1[1] + i2[1] + i3[1]
            player_armor = i0[2] + i1[2] + i2[2] + i3[2]
            if not simulate(php, player_damage, player_armor):
                m = max(m, cost)
print(m)