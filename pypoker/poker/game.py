#/usr/bin/python3

import numpy as np
from poker.hand import *
from poker.card import *
from poker.deck import *

class Game:


    def new_game(self, players = 2):
        deal = np.random.choice(Deck.deck, 5 * players)
        return [Hand(deal) for deal in np.array_split(deal, players)]
