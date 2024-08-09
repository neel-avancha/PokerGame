import unittest

from src.model.Player import Player
from src.model.PokerGame import PokerGame


class TestPokerRound(unittest.TestCase):
    def setUp(self):
        self.players_size_4 = [Player("Alice", 1000), Player("Bob", 1000),
                               Player("Charlie", 1000), Player("Diana", 1000)]
        self.poker_round_size_4 = PokerGame(self.players_size_4, 100, 50, 1000)

        self.players_size_3 = [Player("Alice", 1000), Player("Bob", 1000),
                               Player("Charlie", 1000)]

        self.poker_round_size_3 = PokerGame(self.players_size_3, 100, 50, 1000)

    def assert_blinds(self, poker_round, expected_little_blind, expected_big_blind):
        self.assertEqual(poker_round.index_little_blind, expected_little_blind)
        self.assertEqual(poker_round.index_big_blind, expected_big_blind)

        little_blind_player = poker_round.players[expected_little_blind]
        big_blind_player = poker_round.players[expected_big_blind]

        self.assertTrue(little_blind_player.little_blind_status)
        self.assertFalse(little_blind_player.big_blind_status)

        self.assertFalse(big_blind_player.little_blind_status)
        self.assertTrue(big_blind_player.big_blind_status)

    def test_size_3(self):
        self.assert_blinds(self.poker_round_size_3, 0, 1)
        self.poker_round_size_3.rotate_blinds()
        self.assert_blinds(self.poker_round_size_3, 1, 2)
        self.poker_round_size_3.rotate_blinds()
        self.assert_blinds(self.poker_round_size_3, 2, 0)
        self.poker_round_size_3.rotate_blinds()
        self.assert_blinds(self.poker_round_size_3, 0, 1)


if __name__ == "__main__":
    unittest.main()
