from typing import List

from src.model.Card import Card
from collections import Counter
from Player import Player
import random


def create_deck():
    deck_of_cards = []
    list_of_suits = ["DIAMOND", "CLUB", "SPADE", "HEART"]
    for i in range(1, 14):
        for suit in list_of_suits:
            card = Card(suit, i)
            deck_of_cards.append(card)
    shuffled_deck = shuffle_deck(deck_of_cards)
    return shuffled_deck


def shuffle_deck(deck):
    random.shuffle(deck)
    return deck


class Dealer:

    def __init__(self, current_players: List[Player]):
        self.current_players = current_players
        self.deck_of_cards = create_deck()
        self.river = []

    def update_current_players(self, current_players):
        self.current_players = current_players

    def deal_cards(self):
        for player in self.current_players:
            card_1 = self.deck_of_cards.pop(0)
            card_2 = self.deck_of_cards.pop(0)
            player.assign_hand([card_1, card_2])

    # Think about moving the rotation of the blinds here, as this would be the dealer's
    # responsibility

    def deal_flop(self):
        # Burn a card
        self.deck_of_cards.pop(0)
        for i in range(3):
            card = self.deck_of_cards.pop(0)
            self.river.append(card)

    def deal_next_river_card(self):
        # Burn a card
        self.deck_of_cards.pop(0)
        card = self.deck_of_cards.pop(0)
        self.river.append(card)


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
        suit_only = [card.suit for card in self.hand]

        suit_occurrences = Counter(suit_only)

        for count in suit_occurrences.values():
            if count >= 5:
                return True

        return False

    def check_straight(self):
        number_only = [card.number for card in self.hand]

        number_only.sort()

        prev_number = 0
        consecutive_numbers = 0
        for current_number in number_only:
            if consecutive_numbers >= 4:
                break
            if prev_number == 0:
                prev_number = current_number
            else:
                if prev_number + 1 == current_number:
                    consecutive_numbers += 1
                elif prev_number == current_number:
                    consecutive_numbers = consecutive_numbers
                else:
                    consecutive_numbers = 0

                prev_number = current_number

        if consecutive_numbers >= 4:
            return True
        else:
            return False

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
            "TRIPS": counts[3] >= 1 and counts[2] != 1,  # Ensure not full house
            "TWO_PAIR": counts[2] >= 2,
            "ONE_PAIR": counts[2] == 1 and counts[3] == 0  # Ensure not full house or trips
        }

        for hand, true_value in result_pairs.items():
            if true_value:


        return None


    def __fill_max(self, rank_counts, value_to_find):
        """
        Helper function designed to return the n highest cards to fill for the best five cards.
        :return: The highest rest of cards to fill.
        """
        final_cards_numbers = self.__return_highest_tier_cards(rank_counts, value_to_find)

        num_cards_to_fill = 5 - len(final_cards_numbers)

        hand_numbers_only = [card.number for card in self.hand]

        cards_remaining = [card_number for card_number in hand_numbers_only if card_number not in final_cards_numbers]

        cards_remaining.sort(reverse=True)

        highest_remaining_to_add = cards_remaining[:num_cards_to_fill]

        best_five_cards = final_cards_numbers + highest_remaining_to_add

        return best_five_cards




    def __return_highest_tier_cards(self, rank_counts, value_to_find):
        """
        Helper function designed to return the best cards for the tier.
        e.g: Returning the highest number one-pair, two-pair, trips, etc.

        :param rank_counts: Dictionary where the key is the number and the value is how
        many times it occurs.
        :param value_to_find: A value to look for within rank_counts
        :return: A List containing the highest-tier cards -
        [5,5] Highest one-pair
        [9,9,9,9] Highest Quads
        """

        dict_rank_counts = dict(rank_counts)

        card_numbers = [number for number, occurrence in dict_rank_counts.items() if occurrence == value_to_find]

        card_numbers.sort(reverse=True)

        card = card_numbers[0]

        return [card for _ in range(value_to_find)]

