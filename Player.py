from src.enum.Suit import Suit
from src.Card import Card


class Player:

    def __init__(self, amount):
        self.amount = amount
        self.fold = False
        self.little_blind_status = False
        self.big_blind_status = False
        self.hand = []

    def assign_hand(self, cards_to_assign):
        self.hand = cards_to_assign



