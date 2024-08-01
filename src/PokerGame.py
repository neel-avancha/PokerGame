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

    shuffled_deck = shuffle_deck(deck_of_cards)
    return shuffled_deck


def shuffle_deck(deck):
    random.shuffle(deck)
    return deck


class PokerGame:

    def __init__(self, players: List[Player], big_blind_amount: int,
                 little_blind_amount: int, min_buy_in: int):
        self.players = players
        self.big_blind = big_blind_amount
        self.little_blind = little_blind_amount
        self.min_buy_in = min_buy_in
        self.deck_of_cards = create_deck()
        self.index_little_blind = 0
        self.index_big_blind = 1
        self.current_pot = 0
        self.current_bet = 0
        self.assign_blinds()

    def deal_cards(self):
        for player in self.players:
            card_1 = self.deck_of_cards.pop(0)
            card_2 = self.deck_of_cards.pop(0)
            player.assign_hand([card_1, card_2])

    def assign_blinds(self):
        player1 = self.players[self.index_little_blind]
        player2 = self.players[self.index_big_blind]
        player1.assign_little_blind()
        player2.assign_big_blind()

    def rotate_blinds(self):
        # Reset the blinds
        self.reset_blind()
        self.index_little_blind = self.index_little_blind + 1 if self.index_little_blind + 1 < len(self.players) else 0
        self.index_big_blind = self.index_big_blind + 1 if self.index_big_blind + 1 < len(self.players) else 0
        # Updating the players big and little blind status.
        current_little_blind_player = self.players[self.index_little_blind]
        current_big_blind_player = self.players[self.index_big_blind]

        current_little_blind_player.assign_little_blind()
        current_big_blind_player.assign_big_blind()

    def reset_blind(self):
        previous_little_blind_player = self.players[self.index_little_blind]
        previous_big_blind_player = self.players[self.index_big_blind]

        previous_little_blind_player.reset_blind_status()
        previous_big_blind_player.reset_blind_status()

    def betting_round(self):
        active_players = [player for player in self.players if not player.fold]
        current_better_index = self.index_little_blind

        while True:
            current_better = active_players[current_better_index]

            if current_better.fold:
                current_better_index = current_better_index + 1 % len(active_players)
                if current_better_index == self.index_little_blind:
                    break
                continue

                # Figure out why this is unreachable.
                current_better_index = (current_better_index + 1) % len(active_players)

                if all(player.round_bet_amount == self.current_bet or player.fold for player in active_players):
                    break

    def get_player_action(self, player, action, amount=0):
        if action == 'call':
            self.call(player)
        elif action == 'raise':
            self.raise_bet(player, amount)
        elif action == 'fold':
            self.fold(player)

    def call(self, player):
        amount_to_call = self.current_bet - player.round_bet_amount
        player.bet(amount_to_call)
        self.current_pot += amount_to_call

    def raise_bet(self, player, amount):
        min_raise = self.current_bet * 2
        if amount < self.current_bet + min_raise:
            raise ValueError(f"Raise amount must be at least {min_raise} more than the current bet.")
        additional_bet = amount - player.round_bet_amount
        player.bet(additional_bet)
        self.current_bet = amount
        self.current_pot += additional_bet

    def fold(self, player):
        player.fold_hand()


def main():
    players = [Player("Alice", 1000), Player("Bob", 1000),
               Player("Charlie", 1000), Player("Diana", 1000)]
    poker_round = PokerGame(players, 100, 50, 1000)

    # Check status of the players

    for player in players:
        print("Name:", player.name, "Little Blind Status:", player.little_blind_status,
              "Big Blind Status:", player.big_blind_status)

    print("-------------------------")

    poker_round.deal_cards()

    for player in players:
        print("Name:", player.name)
        for card in player.hand:
            print("Card Number:", card.number, "Card Suit:", card.suit)
    print("-------------------------")

    for card in poker_round.deck_of_cards:
        print("Card Number:", card.number, "Card Suit:", card.suit)

    print(len(poker_round.deck_of_cards))


if __name__ == "__main__":
    main()
