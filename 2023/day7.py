from collections import Counter
import sys
sys.path.append("../advent-of-code")
from util import init, load_day, load_file, result
import math
from functools import cmp_to_key
init()

array = load_day(7, 2023)
part_2 = False
total = 0
cards = ["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"]

hands = []
for i, line in enumerate(array):
    # print(line)
    hand, bid = line.split(" ")
    most_cards = 0
    rank = 0
    two = False
    twotwo = False
    for card in cards[:-1]:
        most_cards = max(most_cards, hand.count(card)+hand.count('J'))
        if two and (hand.count(card) == 2 or hand.count(card)+hand.count('J') >= 2):
            twotwo = True
        if (hand.count(card) == 2 or hand.count(card)+hand.count('J') >= 2):
            two = True
    if most_cards == 3 and two:
        rank = 5
    else:
        if most_cards >= 4:
            rank = most_cards + 2
        elif most_cards == 3:
            rank = 4
        elif twotwo:
            rank = 3
        elif most_cards == 2:
            rank = 2
        elif most_cards == 1:
            rank = 1
            # rank = most_cards
    hands.append([rank, hand, bid])

def compare(hand1, hand2):
    if hand1[0] > hand2[0]:
        return 1
    elif hand2[0] > hand1[0]:
        return -1
    else:
        for h1, h2 in zip(hand1[1], hand2[1]):
            if cards.index(h1) < cards.index(h2):
                return 1
            elif cards.index(h2) < cards.index(h1):
                return -1
    return 0
    
# hands.sort(key=sort) 
hands = sorted(hands, key=cmp_to_key(compare))   


# print(hands)
result(sum(int(hand[2])*(int(i)+1) for i, hand in enumerate(hands)))
# part 1
# hands = []
# for i, line in enumerate(array):
#     # print(line)
#     hand, bid = line.split(" ")
#     most_cards = 0
#     rank = 0
#     two = False
#     twotwo = False
#     for card in cards:
#         most_cards = max(most_cards, hand.count(card))
#         if two and hand.count(card) == 2:
#             twotwo = True
#         if hand.count(card) == 2:
#             two = True
#     if most_cards == 3 and two:
#         rank = 5
#     else:
#         if most_cards >= 4:
#             rank = most_cards + 2
#         elif most_cards == 3:
#             rank = 4
#         elif twotwo:
#             rank = 3
#         elif most_cards == 2:
#             rank = 2
#         elif most_cards == 1:
#             rank = 1
#             # rank = most_cards
#     hands.append([rank, hand, bid])

# def compare(hand1, hand2):
#     if hand1[0] > hand2[0]:
#         return 1
#     elif hand2[0] > hand1[0]:
#         return -1
#     else:
#         for h1, h2 in zip(hand1[1], hand2[1]):
#             if cards.index(h1) < cards.index(h2):
#                 return 1
#             elif cards.index(h2) < cards.index(h1):
#                 return -1
#     return 0
    
# # hands.sort(key=sort) 
# hands = sorted(hands, key=cmp_to_key(compare))   


# print(hands)
# result(sum(int(hand[2])*(int(i)+1) for i, hand in enumerate(hands)))