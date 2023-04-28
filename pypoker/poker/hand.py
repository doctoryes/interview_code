
from poker.deck import Deck

class Hand:
    def __init__(self, cards):
        self.cards = cards

        # Build a mapping of rank ("card") to the rank's index in the sorted array of all ranks.
        # So: {Two': 1, 'Three': 2, ... , 'King': 12, 'Ace': 13}
        self.rank_idx = {}
        for idx, rank in enumerate(Deck.cards):
            self.rank_idx[rank] = idx

    def sort_by_rank(self):
        """
        Sorts all cards in the hand by rank.
        """
        sorted_cards = []
        for rank in Deck.cards:
            for card in self.cards:
                if card.card == rank:
                    sorted_cards.append(card)
        self.cards = sorted_cards

    def is_straight(self):
        """
        Return True if the cards held are a straight. A straight is when the cards held are of sequential rank.
        For example,
            ["Two", "Three", "Four", "Five", "Six"]
        An ace can either be a One or bigger than a king.
        For example,
            ["Ace", "Two", "Three", "Four", "Five"] and
            ["Ten", "Jack", "Queen", "King", "Ace"]
        are both valid straights.
        """
        self.sort_by_rank()

        prev_idx = None
        ace_present = False
        for card in self.cards:

            if card.card == 'Ace':
                if not ace_present:
                    # Mark that ace was encountered - but don't consider for straight.
                    ace_present = True
                    continue
                else:
                    # This card is the second Ace card found - no straight.
                    return False

            if prev_idx is None:
                # First card to consider for a straight - so nothing to compare against yet.
                # Record it for comparison against the next card.
                prev_idx = self.rank_idx[card.card]
                continue

            if self.rank_idx[card.card] - prev_idx != 1:
                # Pair of ordered cards in the hand is not sequential - no straight.
                return False

            # Save this index for next comparison against the next card.
            prev_idx = self.rank_idx[card.card]

        if ace_present:
            # A single Ace card was present - and the rest of the cards are sequential.
            # Check to see if the first card is a Two -or- the next-to-last card is a King.
            # Why is the next-to-last card is checked?
            # Because the last card in an sorted single-Ace-containing hand will be an Ace.
            if self.cards[0].card != 'Two' and self.cards[-2].card != 'King':
                return False

        return True

    def is_flush(self):
        """
        Returns True if the cards held are a flush.
        A flush is when all the cards held are the same suit.
        """
        compare_suit = self.cards[0].suit
        for card in self.cards:
            if card.suit != compare_suit:
                return False
        return True

    def __lt__(self, other):
        return other
