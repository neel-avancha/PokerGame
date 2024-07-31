from typing import List

from src.enum.Suit import Suit
from src.Card import Card
from src.Player import Player
import random


def create_deck():
    deck_of_cards = []
    list_of_suits = ["DIAMOND", "CLUB", "SPADE", "HEART"]
    for i in range(1, 14):
        for suit in list_of_suits:
            card = Card(suit, i)
            deck_of_cards.append(card)
    return deck_of_cards


class PokerRound:

    def __init__(self, players: List[Player], big_blind_amount: int,
                 little_blind_amount: int, buy_in: int):
        self.players = players
        self.big_blind = big_blind_amount
        self.little_blind = little_blind_amount
        self.buy_in = buy_in
        self.deck_of_cards = create_deck()
        self.index_little_blind = 0

    def deal_cards(self):
        for player in self.players:
            card_1 = random.choice(self.deck_of_cards)
            self.deck_of_cards.remove(card_1)
            card_2 = random.choice(self.deck_of_cards)
            self.deck_of_cards.remove(card_2)
            player.assign_hand([card_1, card_2])

    def assign_blinds(self):
        player1 = self.players[0]
        player2 = self.players[1]

        player1.little_blind_status = True
        player2.big_blind_status = True


    def rotate_blinds(self):
        pass
       # max_index = len(self.players) - 1
       #
       #  if self.index_little_blind <


def main():
    pass


if __name__ == "__main__":
    main()
