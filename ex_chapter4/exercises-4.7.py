#!/usr/bin/python3
################################################################################
# 4.7 A deck of cards (itertools and random)
################################################################################
ranks = ['A', 'K', 'Q', 'J', '10', '9', '8', '7', '6', '5', '4', '3', '2']
suits = ['hearts', 'diamonds', 'clubs', 'spades']

print("\nAll cards:")
print("==========")
c = 1
for rank in ranks:
    for suit in suits:
        print("[{}] {} {}".format(c,rank, suit))
        c+=1

# Deck of cards in one line of code
print("\nDeck of cards:")
print("==============")
cards = ((rank, suit) for rank in ranks for suit in suits)
for card in cards:
    print(card)

# OR with product function
import itertools as it
deck = list(it.product(ranks, suits))
print("\nDeck of cards using itertools:")
for n in deck: print(n)

# Shuffled deck of cards: 
# itertools.product() in combination with random.shuffle()
import random
print("\nShuffled cards:")
print("===============")
random.shuffle(deck)
print("\nDECK1:")
for n in deck: print(n, end="")
random.shuffle(deck)
print("\nDECK2:")
for n in deck: print(n, end="")
################################################################################