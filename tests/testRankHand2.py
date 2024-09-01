import unittest

from src.model.Dealer import RankHand
from src.model.Card import Card


class TestRankHand2(unittest.TestCase):

    def setUp(self):
        self.one_pair = [Card("CLUB", 8), Card("CLUB", 7), Card("HEART", 11),
                         Card("HEART", 10), Card("SPADE", 8),
                         Card("DIAMOND", 2), Card("HEART", 5)]

        self.no_pair = [Card("CLUB", 8), Card("CLUB", 6), Card("HEART", 11),
                        Card("HEART", 10), Card("SPADE", 9),
                        Card("DIAMOND", 2), Card("HEART", 5)]

        self.trips = [Card("CLUB", 8), Card("DIAMOND", 8), Card("HEART", 8),
                      Card("HEART", 10), Card("SPADE", 9),
                      Card("DIAMOND", 2), Card("HEART", 5)]

        self.quads = [Card("CLUB", 10), Card("SPADE", 8), Card("HEART", 4),
                      Card("HEART", 10), Card("DIAMOND", 4),
                      Card("SPADE", 10), Card("DIAMOND", 10)]

        self.two_pair = [Card("SPADE", 8), Card("DIAMOND", 4), Card("DIAMOND", 2),
                         Card("HEART", 1), Card("CLUB", 4),
                         Card("DIAMOND", 12), Card("HEART", 8)]

        self.full_house = [Card("CLUB", 8), Card("DIAMOND", 8), Card("HEART", 8),
                           Card("HEART", 10), Card("SPADE", 10),
                           Card("DIAMOND", 2), Card("HEART", 5)]

        self.straight_flush = [Card("CLUB", 8), Card("CLUB", 7), Card("CLUB", 6),
                               Card("CLUB", 5), Card("CLUB", 4),
                               Card("DIAMOND", 2), Card("HEART", 5)]

        self.royal_flush = [Card("CLUB", 14), Card("CLUB", 13), Card("CLUB", 12),
                               Card("CLUB", 11), Card("CLUB", 10),
                               Card("DIAMOND", 2), Card("HEART", 5)]

    def test_card_equality(self, expected_card_list, actual_card_list):

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

        self.assertEqual(tier, expected_tier)

        self.assertTrue(self.test_card_equality(expected_list, best_five))

    def test_high_card(self):
        expected_list = [Card("HEART", 11), Card("HEART", 10),
                         Card("SPADE", 9), Card("CLUB", 8),
                         Card("CLUB", 6)]

        self.run_test(hand_of_cards=self.no_pair, expected_list=expected_list, expected_tier="HIGH_CARD")

    def test_one_pair(self):
        expected_list = [Card("CLUB", 8), Card("SPADE", 8), Card("HEART", 11),
                         Card("HEART", 10), Card("CLUB", 7)]

        self.run_test(hand_of_cards=self.one_pair, expected_list=expected_list, expected_tier="ONE_PAIR")

    def test_two_pair(self):
        expected_list = [Card("SPADE", 8), Card("HEART", 8),
                         Card("DIAMOND", 4), Card("CLUB", 4),
                         Card("DIAMOND", 12)]

        self.run_test(hand_of_cards=self.two_pair, expected_list=expected_list, expected_tier="TWO_PAIR")

    def test_trips(self):
        expected_list = [Card("CLUB", 8), Card("DIAMOND", 8), Card("HEART", 8),
                         Card("HEART", 10), Card("SPADE", 9)]

        self.run_test(hand_of_cards=self.trips, expected_list=expected_list, expected_tier="TRIPS")

    def test_quads(self):
        expected_list = [Card("CLUB", 10), Card("HEART", 10),
                         Card("SPADE", 10), Card("DIAMOND", 10),
                         Card("SPADE", 8)]

        self.run_test(hand_of_cards=self.quads, expected_list=expected_list, expected_tier="QUADS")

    def test_full_house(self):
        expected_list = [Card("CLUB", 8), Card("DIAMOND", 8), Card("HEART", 8),
                         Card("HEART", 10), Card("SPADE", 10)]

        self.run_test(hand_of_cards=self.full_house, expected_list=expected_list, expected_tier="FULL_HOUSE")

    def test_straight_flush(self):
        expected_list = [Card("CLUB", 14), Card("CLUB", 13), Card("CLUB", 12),
                         Card("CLUB", 11), Card("CLUB", 10)]

        self.run_test(hand_of_cards=self.royal_flush, expected_list=expected_list, expected_tier="ROYAL_FLUSH")


