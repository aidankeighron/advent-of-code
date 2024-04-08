import sys
sys.path.append("../advent-of-code-2023")
from util import *
import numpy as np, math
from copy import deepcopy
from dataclasses import dataclass
from typing import List, Tuple
init()

part_2 = True

@dataclass
class Player:
    hp: int
    mana: int
    armor: int
    spent: int
    poison_t: int
    armor_t: int
    recharge_t: int
    
@dataclass
class Boss:
    hp: int
    damage: int

def simulate(player: Player, boss: Boss, player_damage: int = 0, player_healing: int = 0) -> tuple:
    def effects(player_turn):
        if (player.poison_t and not (player_turn and player.poison_t == 6)):
            boss.hp -= 3
            player.poison_t -= 1
        if (player.armor_t and not (player_turn and player.armor_t == 6)):
            player.armor = 7
            player.armor_t -= 1
        else:
            player.armor = 0
        if (player.recharge_t and not (player_turn and player.recharge_t == 5)):
            player.mana += 101
            player.recharge_t -= 1
    
    # player turn
    if (part_2):
        player.hp -= 1
        if (player.hp <= 0):
            return 0, player, boss
    effects(True)
    boss.hp -= player_damage
    player.hp += player_healing
    
    if (boss.hp <= 0):
        return 1, player, boss
    
    # boss turn
    effects(False)
    player.hp -= max(boss.damage - player.armor, 1)
        
    if (player.hp <= 0):
        return 0, player, boss
    if (boss.hp <= 0):
        return 1, player, boss
    return 2, player, boss
    
        

rounds: List[Tuple[Boss, Player]] = [(Boss(51, 9), Player(50, 500, 0, 0, 0, 0, 0))]

total = 9999999
while rounds:
    b, p = rounds.pop(0)
    
    if p.mana < 53 or p.spent >= total:
        continue
    
    def check(alive, new_p, new_b):
        global total
        if alive:
            if alive == 1:
                print(new_p.spent)
                total = min(total, new_p.spent)
            else:
                rounds.append((new_b, new_p))
    
    def cost(c, new_p):
        new_p.mana -= c
        new_p.spent += c

    if p.mana >= 53:
        new_p = deepcopy(p)
        cost(53, new_p)
        new_b = deepcopy(b)
        alive, new_p, new_b = simulate(new_p, new_b, 4, 0)
        check(alive, new_p, new_b)
    if p.mana >= 73:
        new_p = deepcopy(p)
        cost(73, new_p)
        new_b = deepcopy(b)
        alive, new_p, new_b = simulate(new_p, new_b, 2, 2)
        check(alive, new_p, new_b)
    if p.mana >= 113 and p.armor_t <= 1:
        new_p = deepcopy(p)
        cost(113, new_p)
        new_p.armor_t = 6 + p.armor_t
        new_b = deepcopy(b)
        alive, new_p, new_b = simulate(new_p, new_b, 0, 0)
        check(alive, new_p, new_b)
    if p.mana >= 173 and p.poison_t <= 1:
        new_p = deepcopy(p)
        cost(173, new_p)
        new_p.poison_t = 6 + p.poison_t
        new_b = deepcopy(b)
        alive, new_p, new_b = simulate(new_p, new_b, 0, 0)
        check(alive, new_p, new_b)
    if p.mana >= 229 and p.recharge_t <= 1:
        new_p = deepcopy(p)
        cost(229, new_p)
        new_p.recharge_t = 5 + p.recharge_t
        new_b = deepcopy(b)
        alive, new_p, new_b = simulate(new_p, new_b, 0, 0)
        check(alive, new_p, new_b)
        

result(total)