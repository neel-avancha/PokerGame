from typing import List

from src.model.Card import Card
from collections import Counter
from src.model.Player import Player
import random


def create_deck():
    deck_of_cards = []
    list_of_suits = ["DIAMOND", "CLUB", "SPADE", "HEART"]
    for i in range(2, 15):
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
        straight_result, straight_best_five = self.check_straight()
        flush_result, flush_best_five = self.check_flush()

        

    def check_flush(self):
        suit_only = [card.suit for card in self.hand]

        counter_suit = Counter(suit_only)

        flush_suit_list = [num for num, count in counter_suit.items() if count >= 5]

        if len(flush_suit_list) == 0:
            return False
        else:
            flush_suit = flush_suit_list[0]

            best_hand = sorted([card for card in self.hand if card.suit == flush_suit],
                               key=lambda card: card.number, reverse=True)[:5]

            return "FLUSH", best_hand

    def check_straight(self):
        # Extract card numbers and remove duplicates
        card_numbers = sorted(set(card.number for card in self.hand), reverse=True)

        # Create a special case handling for Ace-low straight (A, 2, 3, 4, 5)
        if 14 in card_numbers:
            card_numbers.append(1)  # Add Ace as 1 for checking low straight

        # Check for a straight by slicing the sorted list
        for i in range(len(card_numbers) - 4):
            potential_straight = card_numbers[i:i + 5]
            if potential_straight[0] - potential_straight[-1] == 4:
                # Handle Ace-low case by placing Ace (14) at the end if it exists as 1
                if 1 in potential_straight:
                    potential_straight.remove(1)
                    potential_straight.append(14)

                best_five_cards = []
                for card in self.hand:
                    if card.number in potential_straight and all(card.number != c.number for c in best_five_cards):
                        best_five_cards.append(card)

                best_five_cards.sort(key=lambda card: card.number, reverse=True)
                return "STRAIGHT", best_five_cards

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
            "FULL_HOUSE": (counts[3] == 1 and counts[2] == 1) or (counts[3] == 2) or
                          (counts[3] == 1 and counts[2] == 2),
            "TRIPS": counts[3] == 1 and counts[2] == 0,  # Ensure not full house
            "TWO_PAIR": counts[2] == 2 or counts[2] == 3,
            "ONE_PAIR": counts[2] == 1 and counts[3] == 0  # Ensure not full house or trips
        }

        hand_tier_list = [tier for tier, bool_val in result_pairs.items() if bool_val]

        if len(hand_tier_list) == 0:
            hand_tier = "HIGH_CARD"
        else:
            hand_tier = hand_tier_list[0]

        return self.__match_value(hand_tier=hand_tier, rank_counts=rank_counts, counts=counts)

        # If no pairs, trips, or quads found, return the 5 highest cards

    def __match_value(self, hand_tier, rank_counts, counts):
        match hand_tier:
            case "QUADS":
                return "QUADS", self.__best_five_helper(4, rank_counts)
            case "FULL_HOUSE":
                trip_number = []
                pair_number = []
                if counts[3] == 1 and counts[2] == 1:
                    trip_number = self.__get_tier_numbers(3, rank_counts)
                    pair_number = self.__get_tier_numbers(2, rank_counts)
                elif counts[3] == 2:
                    trip_number_int, pair_number_int = self.__get_tier_numbers(3, rank_counts, top_two=True)
                    trip_number = [trip_number_int]
                    pair_number = [pair_number_int]
                elif counts[3] == 1 and counts[2] == 2:
                    trip_number = self.__get_tier_numbers(3, rank_counts)
                    pair_number = self.__get_tier_numbers(2, rank_counts)

                best_hand = [card for card in self.hand if card.number in trip_number][:3]
                best_hand += [card for card in self.hand if card.number in pair_number][:2]

                return "FULL_HOUSE", best_hand
            case "TRIPS":
                return "TRIPS", self.__best_five_helper(3, rank_counts)
            case "TWO_PAIR":
                return "TWO_PAIR", self.__best_five_helper(2, rank_counts, top_two=True)
            case "ONE_PAIR":
                return "ONE_PAIR", self.__best_five_helper(2, rank_counts)
            case "HIGH_CARD":
                high_cards = sorted(self.hand, key=lambda card: card.number, reverse=True)[:5]
                return "HIGH_CARD", high_cards

    def __best_five_helper(self, count_number, rank_counts, top_two=False):
        tier_number = self.__get_tier_numbers(count_number, rank_counts, top_two=top_two)

        best_hand = [card for card in self.hand if card.number in tier_number]

        num_kickers = 5 - len(best_hand) if not top_two else 1

        kickers = sorted([card for card in self.hand if card.number not in tier_number],
                         key=lambda card: card.number, reverse=True)[:num_kickers]
        best_hand += kickers
        return best_hand

    def __get_tier_numbers(self, count_number, rank_counts, top_two=False):
        if top_two:
            return sorted([num for num, count in rank_counts.items() if count == count_number], reverse=True)[:2]
        else:
            return [max([num for num, count in rank_counts.items() if count == count_number])]
