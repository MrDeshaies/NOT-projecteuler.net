# In the card game poker, a hand consists of five cards and are ranked, from lowest to highest, 
# in the following way:
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
# If two players have the same ranked hands then the rank made up of the highest value wins; for example, 
# a pair of eights beats a pair of fives (see example 1 below). But if two ranks tie, for example, 
# both players have a pair of queens, then highest cards in each hand are compared (see example 4 below); 
# if the highest cards tie then the next highest cards are compared, and so on.
#
# The file, poker.txt, contains one-thousand random hands dealt to two players. 
# Each line of the file contains ten cards (separated by a single space): 
# the first five are Player 1's cards and the last five are Player 2's cards. You can assume that all hands are valid (no invalid characters or repeated cards), each player's hand is in no specific order, and in each hand there is a clear winner.
# 
# How many hands does Player 1 win?
from collections import namedtuple,Counter

# ace is A, 10=T, Jack=J, Queen=Q, King=Q
# Suits are Heart (H), Spade (S), Club (C), Diamond (D)

CARD_VALUES = {
        "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9,
        "T":10, "J":11, "Q":12, "K":13, "A":14
    }

Card = namedtuple('Card', 'value, suit')
Card.numerical_value = lambda card: CARD_VALUES[card.value]

def sort_hand(cards):
    cards.sort(key=Card.numerical_value)

def parse_hand(x):
    # hand look like 6H 4H 5C 3H 2H
    cards = x.split(" ")
    result = [Card._make(x) for x in [list(c) for c in cards]]
    sort_hand(result)
    return result

def parse_data_line(line):
    # records in the file look like (first 5 are player 1)
    # 6H 4H 5C 3H 2H 3S QH 5S 6S AS
    # 8C KC 7S TC 2D TS 8H QD AC 5C
    player1 = line[0:14]
    h1 = parse_hand(player1)
    player2 = line[15:]
    h2 = parse_hand(player2)
    return (h1,h2)

def suits(cards):
    return [c.suit for c in cards]

def card_values(cards):
    return [c.numerical_value() for c in cards]

def high_card(cards):
    return max(card_values(cards))

def all_same_suit(cards):
    suit = cards[0].suit
    return all([suit == c.suit for c in cards])

def royal_flush(cards):
    # Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.
    flush = card_values(cards) == [10,11,12,13,14]
    return {True:10, False:0}[all_same_suit(cards) and flush]

def straight(cards):
    # Straight: All cards are consecutive values.
    start_value = cards[0].numerical_value()
    num_values = card_values(cards)
    straight = all(start_value+x in num_values for x in range(5))
    return {True:start_value, False:0}[straight]

def straight_flush(cards):
    # Straight Flush: All cards are consecutive values of same suit.
    straight_value = straight(cards)
    return {True:straight_value, False:0}[all_same_suit(cards) and straight_value != 0]

def flush(cards):
    # Flush: All cards of the same suit.
    return {True:max(card_values(cards)), False:0}[all_same_suit(cards)]

def x_of_a_kind(cards,x):
    most_common = Counter(card_values(cards)).most_common(1)
    return {True:most_common[0][0], False:0}[most_common[0][1] >= x]

def card_values_not_x(cards,x):
    return [y for y in card_values(cards) if y != x]

def pair(cards):
    # One Pair: Two cards of the same value.
    return x_of_a_kind(cards,2)

def three_of_a_kind(cards):
    # Three of a Kind: Three cards of the same value.
    return x_of_a_kind(cards,3)

def four_of_a_kind(cards):
    # Four of a Kind: Four cards of the same value.
    return x_of_a_kind(cards,4)

def two_pairs(cards):
    # Two Pairs: Two different pairs.
    first_pair_value = x_of_a_kind(cards,2)
    if first_pair_value == 0:
        return 0
    
    def pair_values(x1,x2,x3):
        if x1 == x2 or x1 == x3:
            return x1
        if x2 == x3:
            return x2
        return 0
    
    other_values = card_values_not_x(cards,first_pair_value)
    other_pair_value = pair_values(other_values[0],other_values[1],other_values[2])
    return {True:max(first_pair_value,other_pair_value), False:0}[other_pair_value!=0]

def full_house(cards):
    # Full House: Three of a kind and a pair.
    three = x_of_a_kind(cards,3)
    if three == 0:
        return 0
    
    # now get the pair that is NOT the same as the 3 of the kind.
    other_values = card_values_not_x(cards,three)
    return {True:three, False:0}[len(other_values)==2 and other_values[0] == other_values[1]]

def score_hand(cards,max_score=1000000):
    ranks = [
        (royal_flush,1000),
        (straight_flush,900),
        (four_of_a_kind,800),
        (full_house,700),
        (flush,600),
        (straight,500),
        (three_of_a_kind,400),
        (two_pairs,300),
        (pair,200),
        (high_card,100)]
    
    for rank in ranks:
        s = rank[0](cards)
        if s != 0 and rank[1]+s < max_score:
            return rank[1] + s
    return 0

def tie_breaker(p1_cards, p2_cards):
    if card_values(p1_cards) > card_values(p2_cards):
        return 1
    return 2

def find_winner(p1_cards, p2_cards):
    max_score = 1000000
    while max_score > 0:
        p1_score = score_hand(p1_cards,max_score)
        p2_score = score_hand(p2_cards,max_score)

        if p1_score > p2_score:
            return 1
        if p2_score > p1_score:
            return 2
        max_score = p1_score
    
    # woah nelly, need to break tie!
    return tie_breaker(p1_cards,p2_cards)

def find_player1_wins_in_file():
    hands = []
    f = open("p054_poker.txt", "r")
    for line in f:
        hands.append(parse_data_line(line.strip()))
    f.close()

    p1_wins = 0
    for game in hands:
        if find_winner(game[0],game[1]) == 1:
            p1_wins += 1
    print("P1 wins {0} times".format(p1_wins))

if __name__ == '__main__':
    find_player1_wins_in_file()