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

#  class Bag(enum):
    #  MONEY
    #  TICKET
    #  BOOK


texts = {
    State.START: {
        "opening": "This is the game opening text"
    },
    State.POTSDAM_HBF: {
        "opening": "This is the Potsdam Hbf opening text"
    },
    State.TICKET_AUTOMAT: {
        "opening": "Ticket automat opening text"
    },
    State.TRAIN_1: {
        "opening": "Train 1 opening text"
    },
    State.TRAIN_2: {
        "opening": "Train 1 opening text"
    },
    State.TICKET_CONTROL: {
        "opening": "Ticket control opening"
    },
    State.FEE: {
        "opening": "Fee opening"
    },
    State.LIBRARY: {
        "opening": "Library opening"
    },
    State.BOOK: {
        "opening": "Book opening"
    },
    State.COFFEE: {
        "opening": "Coffee opening"
    },
    State.NEW_GAME: {
        "opening": "New game opening"
    },
    State.EXIT: {
        "opening": "Exit opening"
    }
}


class Player:
    # TODO: 'name' is an optinal feature yet to implement
    # name = random.choice(["John", "Jane"])
    bag = {'money': 20, 'ticket': None, 'book': None}
    state = State.POTSDAM_HBF

    # TODO: Only necessary if name field is used
    # def __init__(self, name):
    #     if name != "":
    #         self.name = name

    def inspect_bag(self):
        pass

    def get_state(self):
        return self.state.name

    def set_state(self, state):
        self.current_state = state

    def get_money(self):
        return self.bag['money']

    def set_money(self, amount):
        self.bag['money'] = amount

    def put_ticket_into_bag(self):
        self.bag['ticket'] = True

    def has_ticket(self):
        return self.bag['ticket'] is not None


def initialize_player():
    # TODO: Opening text missing
    print("Opening text")
    # TODO: Read name from stdin
    return Player()


def text_printer(state):
    print(texts[state])


def game_loop():
    # Set the game's state initially to START
    current_state = State.START

    # The main game loop
    while True:
        if current_state is State.START:
            player = initialize_player()
        elif current_state is State.POTSDAM_HBF:
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
        elif current_state is State.NEW_GAME:
            pass
        elif current_state is State.EXIT:
            break

        current_state = player.get_state()


def main():
    game_loop()


if __name__ == "__main__":
    main()
