#!/usr/bin/python3


class Card:
    def __init__(self, card, suit):
        self.suit = suit
        self.card = card

    def __repr__(self):
        return self.card + " of " + self.suit
