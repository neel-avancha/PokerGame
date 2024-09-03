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

        # Allow this to be a class method within the player class (add river)
        for player in self.current_players:
            player.hand.append(self.river)

    def deal_next_river_card(self):
        # Burn a card
        self.deck_of_cards.pop(0)
        card = self.deck_of_cards.pop(0)
        self.river.append(card)

        for player in self.current_players:
            player.hand.append(card)


class RankHand:
    # The higher the index, the better value the hand holds.
    poker_rankings = {
        "ROYAL_FLUSH": 9,
        "STRAIGHT_FLUSH": 8,
        "QUADS": 7,
        "FLUSH": 6,
        "STRAIGHT": 5,
        "TRIPS": 4,
        "TWO_PAIR": 3,
        "ONE_PAIR": 2,
        "HIGH_CARD": 1
    }

    def __init__(self, hand: List[Card]):

        if len(hand) != 7:
            raise ValueError("Must pass in 7 cards in order to receive a ranking!")

        else:
            self.hand = hand

    def return_rank_of_hand(self):
        sequence_of_methods = [self.check_royal_flush, self.check_straight_flush,
                               self.check_flush, self.check_straight, self.check_pair]

        for method in sequence_of_methods:
            tier, best_five = method()
            if tier:
                return tier, best_five

    def check_royal_flush(self):
        valid_royal_flush_card_nums = [10, 11, 12, 13, 14]

        flush_status = self.check_flush()[0]

        if not flush_status:
            return False, []

        potential_royal_flush = []
        for card in self.hand:
            if card.number in valid_royal_flush_card_nums and all(
                    card.number != c.number for c in potential_royal_flush):
                potential_royal_flush.append(card)

        if len(potential_royal_flush) == 5:
            return "ROYAL_FLUSH", potential_royal_flush
        else:
            return False, []

    def check_straight_flush(self):
        flush_suit = self.__check_flush_occurrence()

        if flush_suit is None:
            return False, []

        flush_cards = self.__return_same_suit(flush_suit=flush_suit)

        straight_occurrences = self.__return_sequence_cards()

        if straight_occurrences is None:
            return False, []

        overlapping_cards = [
            card for card in straight_occurrences
            if any(card.number == flush_card.number and card.suit == flush_card.suit for flush_card in flush_cards)
        ]

        if len(overlapping_cards) < 5:
            return False, []

        best_five = sorted(overlapping_cards, key=lambda card: card.number, reverse=True)[:5]

        return "STRAIGHT_FLUSH", best_five

    def __return_same_suit(self, flush_suit):
        return sorted([card for card in self.hand if card.suit == flush_suit],
                      key=lambda card: card.number, reverse=True)

    def __check_flush_occurrence(self):
        suit_only = [card.suit for card in self.hand]

        counter_suit = Counter(suit_only)

        flush_suit_list = [num for num, count in counter_suit.items() if count >= 5]

        if len(flush_suit_list) == 0:
            return None
        else:
            flush_suit = flush_suit_list[0]
            return flush_suit

    def check_flush(self):

        flush_suit = self.__check_flush_occurrence()

        if flush_suit is None:
            return False, []

        suited_cards = self.__return_same_suit(flush_suit=flush_suit)

        best_hand = suited_cards[:5]

        return "FLUSH", best_hand

    def __return_sequence_cards(self):
        # Extract card numbers and remove duplicates
        card_numbers = sorted(set(card.number for card in self.hand), reverse=True)

        # Create a special case handling for Ace-low straight (A, 2, 3, 4, 5)
        if 14 in card_numbers:
            card_numbers.append(1)  # Add Ace as 1 for checking low straight

        # Initialize variables to track the longest sequence
        longest_sequence = []

        # Check for any sequence by iterating through the sorted list
        current_sequence = [card_numbers[0]]
        for i in range(1, len(card_numbers)):
            if card_numbers[i] == card_numbers[i - 1] - 1:
                current_sequence.append(card_numbers[i])
            else:
                if len(current_sequence) >= 5:
                    longest_sequence.extend(current_sequence)
                current_sequence = [card_numbers[i]]

        # Add the last sequence if it qualifies
        if len(current_sequence) >= 5:
            longest_sequence.extend(current_sequence)

        # Handle Ace-low case by placing Ace (14) at the end if it exists as 1
        if 1 in longest_sequence:
            longest_sequence.remove(1)
            longest_sequence.append(14)

        if len(longest_sequence) >= 5:
            sequence_cards = []
            for card in self.hand:
                if card.number in longest_sequence and card not in sequence_cards:
                    sequence_cards.append(card)

            return sequence_cards

        return None

    def check_straight(self):
        sequence_cards = self.__return_sequence_cards()

        if sequence_cards is None:
            return False, []

        card_numbers = [card.number for card in sequence_cards]

        card_numbers_no_dupes = list(set(card_numbers))

        if len(card_numbers_no_dupes) < 5:
            return False, []

        sequence_cards_no_dupes = []
        for number in card_numbers_no_dupes:
            card_to_append = [card for card in sequence_cards if card.number == number][0]
            sequence_cards_no_dupes.append(card_to_append)

        sequence_cards = sorted(sequence_cards_no_dupes, key=lambda card: card.number, reverse=True)

        first_card = sequence_cards[0]
        second_card = sequence_cards[1]

        # If the Ace is represented as a 1 instead of a 14, add it to the end of the list when outputting.
        if first_card.number == 14 and second_card.number != 13:
            sequence_cards.remove(first_card)
            sequence_cards.append(first_card)

        best_hand = sequence_cards[:5]

        return "STRAIGHT", best_hand

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

        best_hand = sorted([card for card in self.hand if card.number in tier_number],
                           key=lambda card: card.number, reverse=True)

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
