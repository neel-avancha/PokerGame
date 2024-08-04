from typing import List

from src.enum.Suit import Suit
from src.Card import Card
from src.Player import Player
import random
from collections import Counter


class RankHand:
    # The higher the index, the better value the hand holds.
    poker_rankings = ["HIGH_CARD", "ONE_PAIR", "TWO_PAIR", "TRIPS", "STRAIGHT",
                      "FLUSH", "FULL_HOUSE", "QUADS", "STRAIGHT_FLUSH", "ROYAL_FLUSH"]

    def __init__(self, hand: List[Card]):

        if len(hand) != 7:
            raise ValueError("Must pass in 7 cards in order to receive a ranking!")

        else:
            self.hand = hand

    def return_rank_of_hand(self):
        pass

    def check_royal_flush(self):
        pass

    def check_straight_flush(self):
        pass

    def check_flush(self):
        pass

    def check_straight(self):
        pass

    def check_pair(self):

        hand_numbers_only = [card.number for card in self.hand]
        rank_counts = Counter(hand_numbers_only)

        counts = {4: 0, 3: 0, 2: 0}  # Initialize counts for quads, trips, and pairs

        for count in rank_counts.values():
            if count in counts:
                counts[count] += 1

        result_pairs = {
            "QUADS": counts[4] == 1,
            "FULL_HOUSE": counts[3] == 1 and counts[2] == 1,
            "TRIPS": counts[3] == 1 and counts[2] != 1, # Ensure not full house
            "TWO_PAIR": counts[2] == 2,
            "ONE_PAIR": counts[2] == 1 and counts[3] == 0 # Ensure not full house or trips
        }

        for hand, true_value in result_pairs.items():
            if true_value:
                return hand

        return None

