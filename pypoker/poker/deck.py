from poker.card import *
import itertools

class Deck:
    suits = ["Spades", "Hearts", "Diamonds", "Clubs"]
    cards = ["Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine",
             "Ten", "Jack", "Queen", "King", "Ace"]
    deck = [Card(item[0], item[1]) for item in itertools.product(cards, suits)]
