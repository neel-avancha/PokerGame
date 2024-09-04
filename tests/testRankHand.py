import unittest

from src.model.Dealer import RankHand
from src.model.Card import Card


class TestRankHand2(unittest.TestCase):

    def setUp(self):

        # Test High Card
        self.no_pair = [Card("CLUB", 8), Card("CLUB", 6), Card("HEART", 11),
                        Card("HEART", 10), Card("SPADE", 9),
                        Card("DIAMOND", 2), Card("HEART", 5)]

        # One-pair cases
        self.one_pair = [Card("CLUB", 8), Card("CLUB", 7), Card("HEART", 11),
                         Card("HEART", 10), Card("SPADE", 8),
                         Card("DIAMOND", 2), Card("HEART", 5)]

        self.one_pair_aces = [Card("CLUB", 14), Card("CLUB", 7), Card("HEART", 11),
                              Card("HEART", 10), Card("SPADE", 14),
                              Card("DIAMOND", 2), Card("HEART", 5)]

        # Two-pair cases
        self.two_pair = [Card("SPADE", 8), Card("DIAMOND", 4), Card("DIAMOND", 2),
                         Card("HEART", 1), Card("CLUB", 4),
                         Card("DIAMOND", 12), Card("HEART", 8)]

        self.three_pair = [Card("SPADE", 8), Card("DIAMOND", 7), Card("CLUB", 7),
                           Card("HEART", 12), Card("CLUB", 4),
                           Card("DIAMOND", 12), Card("HEART", 8)]

        # Trips
        self.trips = [Card("CLUB", 8), Card("DIAMOND", 8), Card("HEART", 8),
                      Card("HEART", 10), Card("SPADE", 9),
                      Card("DIAMOND", 2), Card("HEART", 5)]

        self.trips_second_case = [Card("CLUB", 14), Card("DIAMOND", 14), Card("HEART", 14),
                                  Card("HEART", 10), Card("SPADE", 9),
                                  Card("DIAMOND", 2), Card("HEART", 5)]

        # Straight
        self.straight_low_ace = [Card("CLUB", 5), Card("DIAMOND", 4), Card("HEART", 3),
                                 Card("HEART", 10), Card("SPADE", 9),
                                 Card("DIAMOND", 14), Card("HEART", 2)]

        self.straight_high_ace = [Card("CLUB", 14), Card("DIAMOND", 13), Card("HEART", 12),
                                  Card("HEART", 11), Card("SPADE", 10),
                                  Card("DIAMOND", 8), Card("HEART", 2)]

        self.straight_high_ace_repeats = [Card("CLUB", 14), Card("DIAMOND", 14),
                                          Card("HEART", 13), Card("CLUB", 13),
                                          Card("SPADE", 12),
                                          Card("DIAMOND", 11), Card("HEART", 10)]

        self.straight_low_ace_repeats = [Card("CLUB", 5),
                                         Card("DIAMOND", 4), Card("HEART", 3),
                                         Card("HEART", 2), Card("SPADE", 4),
                                         Card("DIAMOND", 14), Card("HEART", 2)]

        self.straight_low_ace_repeat_once = [Card("CLUB", 5),
                                             Card("DIAMOND", 4), Card("HEART", 3),
                                             Card("HEART", 2), Card("SPADE", 10),
                                             Card("DIAMOND", 14), Card("HEART", 2)]

        self.straight_high_ace_repeat_once = [Card("CLUB", 14), Card("DIAMOND", 14),
                                              Card("HEART", 13), Card("CLUB", 13),
                                              Card("SPADE", 12),
                                              Card("DIAMOND", 11), Card("HEART", 10)]

        self.straight_full_sequence_high_ace = [Card("CLUB", 14), Card("DIAMOND", 13),
                                                Card("HEART", 12), Card("CLUB", 11),
                                                Card("SPADE", 10),
                                                Card("DIAMOND", 9), Card("HEART", 8)]

        self.straight_full_sequence_low_ace = [Card("CLUB", 14), Card("DIAMOND", 2),
                                               Card("HEART", 3), Card("CLUB", 4),
                                               Card("SPADE", 5),
                                               Card("DIAMOND", 6), Card("HEART", 7)]

        self.straight_normal_sequence = [Card("CLUB", 6), Card("DIAMOND", 7),
                                         Card("HEART", 10), Card("CLUB", 14),
                                         Card("SPADE", 8),
                                         Card("DIAMOND", 9), Card("HEART", 11)]

        # Flush
        self.flush_base = [Card("DIAMOND", 11), Card("DIAMOND", 5),
                           Card("HEART", 3),
                           Card("DIAMOND", 14), Card("SPADE", 8),
                           Card("DIAMOND", 12), Card("DIAMOND", 11)]

        self.flush_six = [Card("DIAMOND", 11), Card("DIAMOND", 5),
                          Card("HEART", 3),
                          Card("DIAMOND", 14), Card("DIAMOND", 8),
                          Card("DIAMOND", 12), Card("DIAMOND", 11)]

        self.flush_seven = [Card("DIAMOND", 11), Card("DIAMOND", 5),
                            Card("DIAMOND", 3),
                            Card("DIAMOND", 14), Card("DIAMOND", 8),
                            Card("DIAMOND", 12), Card("DIAMOND", 11)]

        self.flush_dupes_off_suit = [Card("DIAMOND", 11), Card("DIAMOND", 5),
                                     Card("HEART", 3),
                                     Card("DIAMOND", 14), Card("HEART", 3),
                                     Card("DIAMOND", 2), Card("DIAMOND", 11)]

        self.flush_dupes_off_suit_2 = [Card("DIAMOND", 11), Card("DIAMOND", 5),
                                       Card("HEART", 3),
                                       Card("DIAMOND", 14), Card("DIAMOND", 6),
                                       Card("DIAMOND", 11), Card("HEART", 11)]

        # Full House
        self.full_house_base = [Card("CLUB", 8), Card("DIAMOND", 8),
                                Card("HEART", 8),
                                Card("HEART", 10), Card("SPADE", 10),
                                Card("DIAMOND", 2), Card("HEART", 5)]

        self.full_house_second_case = [Card("CLUB", 8), Card("DIAMOND", 8),
                                       Card("HEART", 8),
                                       Card("HEART", 10), Card("SPADE", 10),
                                       Card("DIAMOND", 10), Card("HEART", 5)]

        self.full_house_third_case = [Card("CLUB", 8), Card("DIAMOND", 8),
                                      Card("HEART", 5),
                                      Card("HEART", 10), Card("SPADE", 10),
                                      Card("DIAMOND", 10), Card("HEART", 5)]

        # Quads
        self.quads = [Card("CLUB", 10), Card("SPADE", 8), Card("HEART", 4),
                      Card("HEART", 10), Card("DIAMOND", 4),
                      Card("SPADE", 10), Card("DIAMOND", 10)]

        # Straight Flush
        self.straight_flush = [Card("CLUB", 8), Card("CLUB", 7), Card("CLUB", 6),
                               Card("CLUB", 5), Card("CLUB", 4),
                               Card("DIAMOND", 2), Card("HEART", 5)]

        self.straight_flush_low = [Card("HEART", 5), Card("HEART", 4), Card("HEART", 3),
                                   Card("HEART", 2), Card("HEART", 14),
                                   Card("CLUB", 10), Card("SPADE", 7)]

        self.straight_flush_high = [Card("SPADE", 13), Card("SPADE", 12), Card("SPADE", 11),
                                    Card("SPADE", 10), Card("SPADE", 9),
                                    Card("CLUB", 8), Card("DIAMOND", 7)]

        self.straight_flush_with_pair = [Card("DIAMOND", 8), Card("DIAMOND", 7), Card("DIAMOND", 6),
                                         Card("DIAMOND", 5), Card("DIAMOND", 4),
                                         Card("HEART", 8), Card("CLUB", 2)]

        self.straight_flush_seven_cards = [Card("CLUB", 9), Card("CLUB", 8), Card("CLUB", 7),
                                           Card("CLUB", 6), Card("CLUB", 5),
                                           Card("CLUB", 4), Card("CLUB", 3)]

        self.straight_flush_with_higher_flush = [Card("HEART", 8), Card("HEART", 7), Card("HEART", 6),
                                                 Card("HEART", 5), Card("HEART", 4),
                                                 Card("SPADE", 14), Card("SPADE", 13)]

        # Royal Flush
        self.royal_flush = [Card("CLUB", 14), Card("CLUB", 13), Card("CLUB", 12),
                            Card("CLUB", 11), Card("CLUB", 10),
                            Card("DIAMOND", 2), Card("HEART", 5)]

        # Royal Flush edge cases
        self.royal_flush_with_straight = [Card("DIAMOND", 14), Card("DIAMOND", 13), Card("DIAMOND", 12),
                                          Card("DIAMOND", 11), Card("DIAMOND", 10),
                                          Card("HEART", 9), Card("CLUB", 8)]

        self.royal_flush_with_flush = [Card("SPADE", 14), Card("SPADE", 13), Card("SPADE", 12),
                                       Card("SPADE", 11), Card("SPADE", 10),
                                       Card("SPADE", 9), Card("SPADE", 8)]

        self.royal_flush_with_full_house = [Card("CLUB", 14), Card("CLUB", 13), Card("CLUB", 12),
                                            Card("CLUB", 11), Card("CLUB", 10),
                                            Card("HEART", 14), Card("SPADE", 14)]

    def check_card_equality(self, expected_card_list, actual_card_list):

        for i in range(len(expected_card_list)):
            expected_card = expected_card_list[i]
            actual_card = actual_card_list[i]
            if not (((expected_card.suit == actual_card.suit) and
                     (expected_card.number == actual_card.number))):
                return False
        return True

    def run_test(self, hand_of_cards, expected_list, expected_tier):
        checker = RankHand(hand_of_cards)

        tier, best_five = checker.return_rank_of_hand()

        for card in best_five:
            print("CARD_NUM", card.number)
            print("CARD_SUIT", card.suit)

        print(len(best_five))

        self.assertEqual(tier, expected_tier)

        self.assertTrue(self.check_card_equality(expected_list, best_five))

    def test_high_card(self):
        expected_list = [Card("HEART", 11), Card("HEART", 10),
                         Card("SPADE", 9), Card("CLUB", 8),
                         Card("CLUB", 6)]

        self.run_test(hand_of_cards=self.no_pair, expected_list=expected_list, expected_tier="HIGH_CARD")

    def test_one_pair(self):
        expected_list = [Card("CLUB", 8), Card("SPADE", 8), Card("HEART", 11),
                         Card("HEART", 10), Card("CLUB", 7)]

        self.run_test(hand_of_cards=self.one_pair, expected_list=expected_list, expected_tier="ONE_PAIR")

        print("------------------------------------------")

        expected_list = [Card("CLUB", 14), Card("SPADE", 14), Card("HEART", 11),
                         Card("HEART", 10), Card("CLUB", 7)]

        self.run_test(hand_of_cards=self.one_pair_aces, expected_list=expected_list, expected_tier="ONE_PAIR")

    def test_two_pair(self):
        expected_list = [Card("SPADE", 8), Card("HEART", 8),
                         Card("DIAMOND", 4), Card("CLUB", 4),
                         Card("DIAMOND", 12)]

        self.run_test(hand_of_cards=self.two_pair, expected_list=expected_list, expected_tier="TWO_PAIR")

        expected_list = [Card("HEART", 12), Card("DIAMOND", 12),
                         Card("SPADE", 8), Card("HEART", 8),
                         Card("DIAMOND", 7)]

        self.run_test(hand_of_cards=self.three_pair, expected_list=expected_list, expected_tier="TWO_PAIR")

    def test_trips(self):
        expected_list = [Card("CLUB", 8), Card("DIAMOND", 8), Card("HEART", 8),
                         Card("HEART", 10), Card("SPADE", 9)]

        self.run_test(hand_of_cards=self.trips, expected_list=expected_list, expected_tier="TRIPS")

        expected_list = [Card("CLUB", 14), Card("DIAMOND", 14), Card("HEART", 14),
                         Card("HEART", 10), Card("SPADE", 9)]

        self.run_test(hand_of_cards=self.trips_second_case, expected_list=expected_list, expected_tier="TRIPS")

    def test_straight(self):
        expected_list = [Card("CLUB", 5), Card("DIAMOND", 4), Card("HEART", 3),
                         Card("HEART", 2), Card("DIAMOND", 14)]

        self.run_test(hand_of_cards=self.straight_low_ace, expected_list=expected_list, expected_tier="STRAIGHT")

        print("---------------------------------------------------")

        expected_list = [Card("CLUB", 14), Card("DIAMOND", 13), Card("HEART", 12),
                         Card("HEART", 11), Card("SPADE", 10)]

        self.run_test(hand_of_cards=self.straight_high_ace, expected_list=expected_list, expected_tier="STRAIGHT")

        print("---------------------------------------------------")

        expected_list = [Card("CLUB", 14), Card("HEART", 13), Card("SPADE", 12),
                         Card("DIAMOND", 11), Card("HEART", 10)]

        self.run_test(hand_of_cards=self.straight_high_ace_repeats,
                      expected_list=expected_list, expected_tier="STRAIGHT")

        print("---------------------------------------------------")

        expected_list = [Card("CLUB", 5), Card("DIAMOND", 4), Card("HEART", 3),
                         Card("HEART", 2), Card("DIAMOND", 14)]

        self.run_test(hand_of_cards=self.straight_low_ace_repeats,
                      expected_list=expected_list, expected_tier="STRAIGHT")

        print("---------------------------------------------------")

        self.run_test(hand_of_cards=self.straight_low_ace_repeat_once,
                      expected_list=expected_list, expected_tier="STRAIGHT")

        expected_list = [Card("CLUB", 14), Card("HEART", 13), Card("SPADE", 12),
                         Card("DIAMOND", 11), Card("HEART", 10)]

        print("---------------------------------------------------")

        self.run_test(hand_of_cards=self.straight_high_ace_repeat_once,
                      expected_list=expected_list, expected_tier="STRAIGHT")

        print("-----------------------------------------------------")

        expected_list = [Card("CLUB", 14), Card("DIAMOND", 13), Card("HEART", 12),
                         Card("CLUB", 11), Card("SPADE", 10)]

        self.run_test(hand_of_cards=self.straight_full_sequence_high_ace,
                      expected_list=expected_list, expected_tier="STRAIGHT")

        print("-----------------------------------------------------")

        expected_list = [Card("HEART", 7), Card("DIAMOND", 6), Card("SPADE", 5),
                         Card("CLUB", 4), Card("HEART", 3)]

        self.run_test(hand_of_cards=self.straight_full_sequence_low_ace,
                      expected_list=expected_list, expected_tier="STRAIGHT")

        print("-----------------------------------------------------")

        expected_list = [Card("HEART", 11), Card("HEART", 10), Card("DIAMOND", 9),
                         Card("SPADE", 8), Card("DIAMOND", 7)]

        self.run_test(hand_of_cards=self.straight_normal_sequence,
                      expected_list=expected_list, expected_tier="STRAIGHT")

    def test_flush(self):
        expected_list = [Card("DIAMOND", 14), Card("DIAMOND", 12),
                         Card("DIAMOND", 11),
                         Card("DIAMOND", 11), Card("DIAMOND", 5)]

        self.run_test(hand_of_cards=self.flush_base, expected_list=expected_list, expected_tier="FLUSH")

        print("-----------------------------------------------------")

        expected_list = [Card("DIAMOND", 14), Card("DIAMOND", 12),
                         Card("DIAMOND", 11),
                         Card("DIAMOND", 11), Card("DIAMOND", 8)]

        self.run_test(hand_of_cards=self.flush_six, expected_list=expected_list, expected_tier="FLUSH")

        print("-----------------------------------------------------")

        expected_list = [Card("DIAMOND", 14), Card("DIAMOND", 12),
                         Card("DIAMOND", 11),
                         Card("DIAMOND", 11), Card("DIAMOND", 8)]

        self.run_test(hand_of_cards=self.flush_six, expected_list=expected_list, expected_tier="FLUSH")

        print("-----------------------------------------------------")

        self.run_test(hand_of_cards=self.flush_seven, expected_list=expected_list, expected_tier="FLUSH")

        print("-----------------------------------------------------")

        expected_list = [Card("DIAMOND", 14), Card("DIAMOND", 11),
                         Card("DIAMOND", 11),
                         Card("DIAMOND", 5), Card("DIAMOND", 2)]

        self.run_test(hand_of_cards=self.flush_dupes_off_suit, expected_list=expected_list, expected_tier="FLUSH")

        print("-----------------------------------------------------")

        expected_list = [Card("DIAMOND", 14), Card("DIAMOND", 11),
                         Card("DIAMOND", 11),
                         Card("DIAMOND", 6), Card("DIAMOND", 5)]

        self.run_test(hand_of_cards=self.flush_dupes_off_suit_2, expected_list=expected_list, expected_tier="FLUSH")

        print("-----------------------------------------------------")

    def test_quads(self):
        expected_list = [Card("CLUB", 10), Card("HEART", 10),
                         Card("SPADE", 10), Card("DIAMOND", 10),
                         Card("SPADE", 8)]

        self.run_test(hand_of_cards=self.quads, expected_list=expected_list, expected_tier="QUADS")

    def test_full_house(self):
        expected_list = [Card("CLUB", 8), Card("DIAMOND", 8), Card("HEART", 8),
                         Card("HEART", 10), Card("SPADE", 10)]

        self.run_test(hand_of_cards=self.full_house_base, expected_list=expected_list, expected_tier="FULL_HOUSE")

        print("-----------------------------------------------------")

        expected_list = [Card("HEART", 10), Card("SPADE", 10), Card("DIAMOND", 10),
                         Card("CLUB", 8), Card("DIAMOND", 8)]

        self.run_test(hand_of_cards=self.full_house_second_case, expected_list=expected_list,
                      expected_tier="FULL_HOUSE")

        print("-----------------------------------------------------")

        self.run_test(hand_of_cards=self.full_house_third_case, expected_list=expected_list, expected_tier="FULL_HOUSE")

    def test_straight_flush(self):
        # Test low straight flush (5-high with Ace)
        expected_list = [Card("HEART", 14), Card("HEART", 5), Card("HEART", 4),
                         Card("HEART", 3), Card("HEART", 2)]
        self.run_test(hand_of_cards=self.straight_flush_low, expected_list=expected_list, expected_tier="STRAIGHT_FLUSH")

        print("-----------------------------------------------------")

        # Test high straight flush (King-high)
        expected_list = [Card("SPADE", 13), Card("SPADE", 12), Card("SPADE", 11),
                         Card("SPADE", 10), Card("SPADE", 9)]
        self.run_test(hand_of_cards=self.straight_flush_high, expected_list=expected_list, expected_tier="STRAIGHT_FLUSH")

        print("-----------------------------------------------------")

        # Test straight flush with a pair
        expected_list = [Card("DIAMOND", 8), Card("DIAMOND", 7), Card("DIAMOND", 6),
                         Card("DIAMOND", 5), Card("DIAMOND", 4)]
        self.run_test(hand_of_cards=self.straight_flush_with_pair, expected_list=expected_list, expected_tier="STRAIGHT_FLUSH")

        print("-----------------------------------------------------")

        # Test straight flush with seven cards in sequence
        expected_list = [Card("CLUB", 9), Card("CLUB", 8), Card("CLUB", 7),
                         Card("CLUB", 6), Card("CLUB", 5)]
        self.run_test(hand_of_cards=self.straight_flush_seven_cards, expected_list=expected_list, expected_tier="STRAIGHT_FLUSH")

        print("-----------------------------------------------------")

        # Test straight flush with higher flush available
        expected_list = [Card("HEART", 8), Card("HEART", 7), Card("HEART", 6),
                         Card("HEART", 5), Card("HEART", 4)]
        self.run_test(hand_of_cards=self.straight_flush_with_higher_flush, expected_list=expected_list, expected_tier="STRAIGHT_FLUSH")

    def test_royal_flush(self):
        # Test royal flush with straight
        expected_list = [Card("DIAMOND", 14), Card("DIAMOND", 13), Card("DIAMOND", 12),
                         Card("DIAMOND", 11), Card("DIAMOND", 10)]
        self.run_test(hand_of_cards=self.royal_flush_with_straight, expected_list=expected_list, expected_tier="ROYAL_FLUSH")

        print("-----------------------------------------------------")

        # Test royal flush with flush
        expected_list = [Card("SPADE", 14), Card("SPADE", 13), Card("SPADE", 12),
                         Card("SPADE", 11), Card("SPADE", 10)]
        self.run_test(hand_of_cards=self.royal_flush_with_flush, expected_list=expected_list, expected_tier="ROYAL_FLUSH")

        print("-----------------------------------------------------")

        # Test royal flush with full house
        expected_list = [Card("CLUB", 14), Card("CLUB", 13), Card("CLUB", 12),
                         Card("CLUB", 11), Card("CLUB", 10)]
        self.run_test(hand_of_cards=self.royal_flush_with_full_house, expected_list=expected_list, expected_tier="ROYAL_FLUSH")
