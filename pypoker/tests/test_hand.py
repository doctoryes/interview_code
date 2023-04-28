# -*- coding: utf-8 -*-

from .common import *

class HandTest(unittest.TestCase):
    """Test hand methods"""

    def test_straight(self):
        cards = [ Card("Two", "Hearts"), Card("Three", "Spades"), Card("Four", "Hearts"), Card("Five", "Clubs"), Card("Six", "Diamonds") ]
        hand = Hand(cards)
        self.assertTrue(hand.is_straight())

    def test_straight_ace_low(self):
        cards = [ Card("Ace", "Diamonds"), Card("Two", "Hearts"), Card("Three", "Spades"), Card("Four", "Hearts"), Card("Five", "Clubs") ]
        hand = Hand(cards)
        self.assertTrue(hand.is_straight())

    def test_straight_ace_high(self):
        cards = [ Card("Ten", "Hearts"), Card("Jack", "Spades"), Card("Queen", "Clubs"), Card("King", "Diamonds"), Card("Ace", "Spades") ]
        hand = Hand(cards)
        self.assertTrue(hand.is_straight())

    def test_flush(self):
        cards = [ Card("Six", "Spades"), Card("King", "Spades"), Card("Ace", "Spades"), Card("Two", "Spades"), Card("Four", "Spades") ]
        hand = Hand(cards)
        self.assertTrue(hand.is_flush())


if __name__ == "__main__":
    unittest.main()
