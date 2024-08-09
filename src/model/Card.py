from src.enum.Suit import Suit


class Card:
    def __init__(self, suit, number):
        # if not isinstance(suit, Suit):
        #     raise ValueError(f'suit must be an instance of Suit Enum, got {type(suit).__name__}')

        self.suit = suit
        self.number = number
