#!/usr/bin/env python

from enum import Enum, auto
#  import random


class State(Enum):
    START = auto()
    POTSDAM_HBF = auto()
    TICKET_AUTOMAT = auto()
    TRAIN_1 = auto()
    TRAIN_2 = auto()
    TICKET_CONTROL = auto()
    FEE = auto()
    LIBRARY = auto()
    COFFEE_TRINKING = auto()
    BOOK_READING = auto()
    NEW_GAME = auto()
    EXIT = auto()


def function(arg1):
    """TODO: Docstring for function.

    :arg1: TODO
    :returns: TODO

    """
    pass


class Player:
    # TODO: name is an optinal feature
    # name = random.choice(["John", "Jane"])
    bag = {'money': 20, 'ticket': None, 'book': None}
    current_state = State.POTSDAM_HBF

    # TODO: Only necessary if name field is used
    # def __init__(self, name):
    #     if name != "":
    #         self.name = name

    def inspect_bag(self):
        pass

    def has_ticket(self):
        return self.bag['ticket'] is not None

    def get_current_state(self):
        return self.current_state.name

    def check_money(self):
        return self.bag['money']

    def put_ticket_into_bag(self):
        self.bag['ticket'] = True


def start_game():
    # TODO: Opening text missing
    print("Opening text")
    # TODO: Read name from stdin
    return Player()


def game_loop(player):
    while True:
        current_state = player.get_current_state()
        if current_state is State.POTSDAM_HBF:
            pass
        elif current_state is State.TICKET_AUTOMAT:
            pass
        elif current_state is State.TRAIN_1:
            pass
        elif current_state is State.TRAIN_2:
            pass
        elif current_state is State.TICKET_CONTROL:
            pass
        elif current_state is State.LIBRARY:
            pass
        elif current_state is State.FEE:
            pass
        elif current_state is State.BOOK_READING:
            pass
        elif current_state is State.COFFEE_TRINKING:
            pass
        elif current_state is State.EXIT:
            break


def main():
    new_round = True

    while new_round:

        # Start the game and initialize all objects
        player = start_game()

        game_loop(player)

        new_round = new_round()


if __name__ == "__main__":
    main()
