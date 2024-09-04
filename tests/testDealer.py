import unittest

from src.model.Dealer import *
from src.model.Card import Card
from src.model.Player import *


class TestRankHand2(unittest.TestCase):

    def setUp(self):
        # Example One
        self.no_pair = [Card("CLUB", 8), Card("CLUB", 6), Card("CLUB", 11),
                        Card("HEART", 10), Card("SPADE", 9),
                        Card("CLUB", 14),
                        Card("HEART", 5)]

        self.straight = [Card("CLUB", 8), Card("CLUB", 6), Card("CLUB", 11),
                         Card("HEART", 10), Card("SPADE", 9),
                         Card("DIAMOND", 13),
                         Card("SPADE", 12)]

        self.flush = [Card("CLUB", 8), Card("CLUB", 6), Card("CLUB", 11),
                      Card("HEART", 10), Card("SPADE", 9),
                      Card("CLUB", 13),
                      Card("CLUB", 2)]

        self.one_pair = [Card("CLUB", 8), Card("CLUB", 6), Card("CLUB", 11),
                         Card("HEART", 10), Card("SPADE", 9),
                         Card("DIAMOND", 8),
                         Card("SPADE", 2)]

        bob = Player("Bob", 10000)

        sam = Player("Sam", 10000)

        bill = Player("Bill", 10000)

        dave = Player("Winner", 10000)

        bob.assign_hand(self.no_pair)

        sam.assign_hand(self.straight)

        bill.assign_hand(self.one_pair)

        dave.assign_hand(self.flush)

        self.player_list_1 = [bob, sam, bill, dave]

        # Case 2
        self.player_list_2 = [bob]

        # Case 3
        river = [Card("DIAMOND", 14), Card("DIAMOND", 6), Card("DIAMOND", 7),
                 Card("DIAMOND", 11), Card("DIAMOND", 12)]

        bob = Player("Bob", 10000)
        bob_hand = [Card("DIAMOND", 5), Card("HEART", 10)]
        bob.assign_hand(river+bob_hand)

        sam = Player("Sam", 10000)
        sam_hand = [Card("HEART", 5), Card("HEART", 10)]
        sam.assign_hand(river+sam_hand)

        bill = Player("Bill", 10000)
        bill_hand = [Card("HEART", 14), Card("CLUB", 14)]
        bill.assign_hand(river+bill_hand)

        dave = Player("Dave", 10000)
        dave_hand = [Card("DIAMOND", 4), Card("CLUB", 10)]
        dave.assign_hand(river+dave_hand)

        self.player_list_3 = [bob, sam, bill, dave]

        winner = Player("Winner", 10000)
        winner_hand = [Card("DIAMOND", 13), Card("HEART", 9)]
        winner.assign_hand(river + dave_hand)
        winner.assign_hand(river+winner_hand)

        self.player_list_4 = [bob, sam, bill, dave, winner]




    def test_base_case(self):
        dealer = Dealer(current_players=self.player_list_2)
        dealer.determine_winner()
        self.assertEqual(dealer.winners, "Bob")

    def test_one_winner_case(self):
        dealer = Dealer(current_players=self.player_list_1)
        dealer.determine_winner()
        self.assertEqual(dealer.winners, "Winner")

    def test_multiple_winner_case(self):
        dealer = Dealer(current_players=self.player_list_3)
        dealer.determine_winner()
        self.assertEqual(dealer.winners, ['Bob', 'Sam', 'Bill', 'Dave'])

    def test_break_tie_case(self):
        dealer = Dealer(current_players=self.player_list_4)
        dealer.determine_winner()
        self.assertEqual(dealer.winners, "Winner")


