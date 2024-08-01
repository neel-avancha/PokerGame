from src.enum.Suit import Suit
from src.Card import Card


class Player:

    def __init__(self, name, amount):
        self.name = name
        self.amount = amount
        self.fold = False
        self.little_blind_status = False
        self.big_blind_status = False
        self.hand = []

    def assign_hand(self, cards_to_assign):
        self.hand = cards_to_assign

    def assign_big_blind(self):
        self.big_blind_status = True

    def assign_little_blind(self):
        self.little_blind_status = True

    def reset_blind_status(self):
        self.little_blind_status = False
        self.big_blind_status = False