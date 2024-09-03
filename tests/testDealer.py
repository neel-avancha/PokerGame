import unittest

from src.model.Dealer import *
from src.model.Card import Card
from src.model.Player import *


class TestRankHand2(unittest.TestCase):

    def setUp(self):
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

        winner = Player("Winner", 10000)

        bob.assign_hand(self.no_pair)

        sam.assign_hand(self.straight)

        bill.assign_hand(self.one_pair)

        winner.assign_hand(self.flush)

        self.player_list_1 = [bob, sam, bill, winner]

        # Case 2
        self.player_list_2 = [bob]

    def test_base_case_dealer(self):
        dealer = Dealer(current_players=self.player_list_2)

        val = dealer.determine_winner()

        print(val)

    def test_basic_case_dealer(self):
        dealer = Dealer(current_players=self.player_list_1)

        val = dealer.determine_winner()
        print(val)





    # def determine_winner(self):
    #     if len(self.current_players) == 1:
    #         player = self.current_players[0]
    #         return [f"Player: {player.name} won the hand!"]
    #
    #     # The higher the index, the better value the hand holds.
    #     poker_rankings = self.poker_rankings
    #
    #     player_hands = []
    #     highest_rank = -1
    #
    #     for player in self.current_players:
    #         ranker = RankHand(player.hand)
    #         tier, best_five = ranker.return_rank_of_hand()
    #         rank = poker_rankings[tier]
    #         player_hands.append((player, rank, best_five))
    #         highest_rank = max(highest_rank, rank)
    #
    #     # Filter to only the highest ranking hands
    #     top_hands = [ph for ph in player_hands if ph[1] == highest_rank]
    #
    #     # If there's only one top hand, we have a winner
    #     if len(top_hands) == 1:
    #         winner = top_hands[0][0]
    #         return [
    #             f"Player: {winner.name} won the hand with "
    #             f"{list(poker_rankings.keys())[list(poker_rankings.values()).index(highest_rank)]}!"]
    #
    #     # If we're here, we need to break a tie
    #     winners = self.break_tie(top_hands)
    #
    #     if len(winners) == 1:
    #         return [f"Player: {winners[0].name} won the hand after tiebreak!"]
    #     else:
    #         return [f"Players: {', '.join([w.name for w in winners])} tied and split the pot!"]


