from src.enum.Suit import Suit


class Card:
    def __init__(self, suit, number):
        # if not isinstance(suit, Suit):
        #     raise ValueError(f'suit must be an instance of Suit Enum, got {type(suit).__name__}')

        self.suit = suit
        self.number = number

    @staticmethod
    def create_deck():
        deck_of_cards = []
        list_of_suits = ["DIAMOND", "CLUB", "SPADE", "HEART"]
        for i in range(1, 14):
            for suit in list_of_suits:
                card = Card(suit, i)
                deck_of_cards.append(card)
        return deck_of_cards


def main():
    print("Starting main function")
    deck_of_cards = Card.create_deck()


if __name__ == "__main__":
    main()
