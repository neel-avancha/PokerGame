import unittest

from src.model.Dealer import RankHand
from src.model.Card import Card


class TestRankHand(unittest.TestCase):

    def setUp(self):
        self.one_pair = [Card("CLUB", 8), Card("CLUB", 7), Card("HEART", 11),
                         Card("HEART", 10), Card("SPADE", 8),
                         Card("DIAMOND", 2), Card("HEART", 5)]

        self.no_pair = [Card("CLUB", 8), Card("CLUB", 7), Card("HEART", 11),
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

    def test_one_pair(self):
        checker = RankHand(self.one_pair)

        self.assertEqual(checker.check_pair(), "ONE_PAIR")

    def test_two_pair(self):
        checker = RankHand(self.two_pair)

        self.assertEqual(checker.check_pair(), "TWO_PAIR")

    def test_no_pair(self):
        checker = RankHand(self.no_pair)

        self.assertEqual(checker.check_pair(), None)

    def test_trips(self):
        checker = RankHand(self.trips)

        self.assertEqual(checker.check_pair(), "TRIPS")

    def test_quads(self):
        checker = RankHand(self.quads)

        self.assertEqual(checker.check_pair(), "QUADS")

    def test_full_house(self):
        checker = RankHand(self.full_house)

        self.assertEqual(checker.check_pair(), "FULL_HOUSE")
