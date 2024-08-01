from src.enum.Suit import Suit
from src.Card import Card


class Player:
    def __init__(self, name, total_amount):
        self.name = name
        self.total_amount = total_amount
        self.fold = False
        self.little_blind_status = False
        self.big_blind_status = False
        self.hand = []
        self.round_bet_amount = 0

    def assign_hand(self, cards_to_assign):
        self.hand = cards_to_assign

    def assign_big_blind(self):
        self.big_blind_status = True

    def assign_little_blind(self):
        self.little_blind_status = True

    def reset_blind_status(self):
        self.little_blind_status = False
        self.big_blind_status = False

    def bet(self, amount):
        if amount > self.total_amount:
            raise ValueError(f"{self.name} does not have enough money to bet this amount.")
        self.total_amount -= amount
        self.round_bet_amount += amount
        return amount



    def fold_hand(self):
        self.fold = True
