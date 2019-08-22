import time
import statistics
starttime = time.time()

# In the card game poker, a hand consists of five cards and are ranked, from lowest to highest, in the following way:
# 
# High Card: Highest value card.
# One Pair: Two cards of the same value.
# Two Pairs: Two different pairs.
# Three of a Kind: Three cards of the same value.
# Straight: All cards are consecutive values.
# Flush: All cards of the same suit.
# Full House: Three of a kind and a pair.
# Four of a Kind: Four cards of the same value.
# Straight Flush: All cards are consecutive values of same suit.
# Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.
# The cards are valued in the order:
# 2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace.
# 
# If two players have the same ranked hands then the rank made up of the highest value wins; for example, a pair of eights beats a pair of fives (see example 1 below). But if two ranks tie, for example, both players have a pair of queens, then highest cards in each hand are compared (see example 4 below); if the highest cards tie then the next highest cards are compared, and so on.
# 
# Consider the following five hands dealt to two players:
# 
# Hand	 	Player 1	 	Player 2	 	Winner
# 1	 	5H 5C 6S 7S KD
# Pair of Fives
#  	2C 3S 8S 8D TD
# Pair of Eights
#  	Player 2
# 2	 	5D 8C 9S JS AC
# Highest card Ace
#  	2C 5C 7D 8S QH
# Highest card Queen
#  	Player 1
# 3	 	2D 9C AS AH AC
# Three Aces
#  	3D 6D 7D TD QD
# Flush with Diamonds
#  	Player 2
# 4	 	4D 6S 9H QH QC
# Pair of Queens
# Highest card Nine
#  	3D 6D 7H QD QS
# Pair of Queens
# Highest card Seven
#  	Player 1
# 5	 	2H 2D 4C 4D 4S
# Full House
# With Three Fours
#  	3C 3D 3S 9S 9D
# Full House
# with Three Threes
#  	Player 1
# The file, poker.txt, contains one-thousand random hands dealt to two players. Each line of the file contains ten cards (separated by a single space): the first five are Player 1's cards and the last five are Player 2's cards. You can assume that all hands are valid (no invalid characters or repeated cards), each player's hand is in no specific order, and in each hand there is a clear winner.
# 
# How many hands does Player 1 win?

nums = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
values = {}
for i in range(0, len(nums)):
    values[nums[i]] = i + 2

def compare_with_highcard_wrapper(values1, values2):
    if max(values1) != max(values2):
        return max(values1) > max(values2)
    else:
        values1.remove(max(values1))
        values2.remove(max(values2))
        return compare_with_highcard_wrapper(values1, values2)

def compare_with_highcard(hand1, hand2):
    values1 = []
    values2 = []
    for card1, card2 in zip(hand1, hand2):
        values1.append(values[card1[:-1]])
        values2.append(values[card2[:-1]])
    return compare_with_highcard_wrapper(values1, values2)

def n_ofakind(hand, n):
    maxsofar = -99
    nfound = False
    for i in range(0, 6 - n):
        total = 0
        for j in range(i, 5):
            if hand[i][:-1] == hand[j][:-1]:
                total += 1
        if total == n:
            nfound = True
            if values[hand[i][:-1]] > maxsofar:
                maxsofar = values[hand[i][:-1]]
    return [nfound, maxsofar]

def double(hand):
    return n_ofakind(hand, 2)

def doubledouble(hand):
    yes = False
    result = double(hand)
    m = -99
    if result[0]:
        temp = []
        for card in hand:
            if values[card[:-1]] != result[1]:
                temp.append(values[card[:-1]])
        if len(list(set(temp))) == 2:
            yes = True
            m = statistics.median(temp)

    return [yes, max(m, result[1])]

def triple(hand):
    return n_ofakind(hand, 3)

def is_straight(hand):
    # x + x + 1 + ... + x + 4 = 5x + 10
    total = 0
    value = []
    for card in hand:
        value.append(values[card[:-1]])
        total += values[card[:-1]]
    return [((total - 10) / 5) == min(value) and not double(hand)[0], max(value)]

def is_flush(hand):
    maxsofar = -99
    for card in hand:
        if values[card[:-1]] > maxsofar:
            maxsofar = values[card[:-1]]
    return [hand[0][-1] == hand[1][-1] == hand[2][-1] == hand[3][-1] == hand[4][-1], maxsofar]

def fullhouse(hand):
    yes = False
    result = triple(hand)
    if result[0]:
        temp = []
        for card in hand:
            if values[card[:-1]] != result[1]:
                temp.append(values[card[:-1]])
        yes = temp[0] == temp[1]
    return [yes, result[1]]

def quadruple(hand):
    return n_ofakind(hand, 4)

def is_straight_flush(hand):
    result = [is_straight(hand)[0] and is_flush(hand)[0]]
    maxsofar = -99
    for card in hand:
        if values[card[:-1]] > maxsofar:
            maxsofar = values[card[:-1]]
    result.append(maxsofar)
    return result

def is_royal(hand):
    seen = [False, False, False, False, False]
    for card in hand:
        for v in range(0, len(nums[8:])):
            seen[v] = nums[8:][v] in card
    return seen[0] and seen[1] and seen[2] and seen[3] and seen[4] and is_flush(hand)[0]

def assign_handvalue(hand):
    if is_royal(hand):
        return [10, 12]
    elif is_straight_flush(hand)[0]:
        return [9, is_straight_flush(hand)[1]]
    elif quadruple(hand)[0]:
        return [8, quadruple(hand)[1]]
    elif fullhouse(hand)[0]:
        return [7, fullhouse(hand)[1]]
    elif is_flush(hand)[0]:
        return [6, is_flush(hand)[1]]
    elif is_straight(hand)[0]:
        return [5, is_straight(hand)[1]]
    elif triple(hand)[0]:
        return [4, triple(hand)[1]]
    elif doubledouble(hand)[0]:
        return [3, doubledouble(hand)[1]]
    elif double(hand)[0]:
        return [2, double(hand)[1]]
    else:
        v = []
        for card in hand:
            v.append(values[card[:-1]])
        return [1, max(v)]


one = 0
i = 0

def compare(hand1, hand2):
    hand1_value = assign_handvalue(hand1)
    hand2_value = assign_handvalue(hand2)
    if hand1_value[0] > hand2_value[0]:
        return True
    elif hand1_value[0] == hand2_value[0]:
        if hand1_value[1] > hand2_value[1]:
            return True
        elif hand1_value[1] == hand2_value[1]:
            if compare_with_highcard(hand1, hand2):
                return True

f = open('poker.txt', 'r')
for x in f:
    hand1 = x.split()[0:5]
    hand2 = x.split()[5:10]
    if compare(hand1, hand2):
        one += 1
print(one)
print(time.time() - starttime)
