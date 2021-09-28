#!/usr/bin/env python

from enum import Enum, auto
import random


class State(Enum):
    START = auto()
    POTSDAM_HBF = auto()
    TICKET_AUTOMAT = auto()
    TRAIN_1 = auto()
    TRAIN_2 = auto()
    TICKET_CONTROL = auto()
    FEE = auto()
    LIBRARY = auto()
    COFFEE = auto()
    BOOK = auto()
    NEW_GAME = auto()
    EXIT = auto()

#  class Bag(enum):
    #  MONEY
    #  TICKET
    #  BOOK


texts = {
    State.START: {
        "opening": "This is the game opening text",
        "query": ""
    },
    State.POTSDAM_HBF: {
        "opening": "This is the Potsdam Hbf opening text",
        "query": "What do you want to do?",
    },
    State.TICKET_AUTOMAT: {
        "opening": "Ticket automat opening text",
        "query": "Do you want to play another round?"
    },
    State.TRAIN_1: {
        "opening": "Train 1 opening text",
        "query": "Do you want to play another round?"
    },
    State.TRAIN_2: {
        "opening": "Train 1 opening text",
        "query": "Do you want to play another round?"
    },
    State.TICKET_CONTROL: {
        "opening": "Ticket control opening",
        "query": "Do you want to play another round?"
    },
    State.FEE: {
        "opening": "Fee opening",
        "query": "Do you want to play another round?"
    },
    State.LIBRARY: {
        "opening": "Library opening",
        "query": "Do you want to play another round?"
    },
    State.BOOK: {
        "opening": "Book opening",
        "query": "Do you want to play another round?"
    },
    State.COFFEE: {
        "opening": "Coffee opening",
        "query": "Do you want to play another round?"
    },
    State.NEW_GAME: {
        "opening": "You are about to exit the game.",
        "query": "Do you want to play another round?"
    },
    State.EXIT: {
        "opening": "Bye! Until next time.",
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
        return self.state

    def set_state(self, state):
        self.state = state

    def get_money(self):
        return self.bag['money']

    def set_money(self, amount):
        self.bag['money'] = amount

    def put_ticket_into_bag(self):
        self.bag['ticket'] = True

    def has_ticket(self):
        return self.bag['ticket'] is not None


def initialize_player():
    return Player()


def scene_description(state):
    print(texts[state]["opening"])


def query_player(state):
    print(texts[state]["query"])


def potsdam_hbf(player):
    while player.get_state() is State.POTSDAM_HBF:
        action = input(">>> ").lower()
        if action == "buy ticket":
            print("OK, let's go buy a ticket!")
            player.state = State.TICKET_AUTOMAT
        elif action == "get train":
            print("No ticket! Buy one first!")

        default_interactions(player, action)


def first_riddle(player):
    pass


def on_train_1(player):
    random.seed()
    # Generate a random number for 60% to get into a ticket control
    chance = random.randint(1, 100)
    while player.get_state() is State.TRAIN_1:
        action = input(">>> ").lower()
        if action == "get to golm":
            if chance <= 40:
                player.state = State.LIBRARY
            else:
                player.state = State.TICKET_CONTROL

        default_interactions(player, action)


def on_train_2(player):
    while player.get_state() is State.TRAIN_2:
        action = input(">>> ").lower()
        if action == "get to golm":
            player.set_state(State.COFFEE)

        default_interactions(player, action)


def ticket_control(player):
    # Generate random number for the 50% chance of an invalid ticket
    chance = random.randint(1, 100)
    while player.get_state() is State.TICKET_CONTROL:
        action = input(">>> ").lower()
        if action == "show ticket":
            if chance <= 50:
                player.set_state(State.FEE)
            else:
                player.set_state(State.LIBRARY)

        default_interactions(player, action)


def fee(player):
    while player.get_state() is State.FEE:
        action = input(">>> ").lower()
        if action == "pay fee":
            player.set_state(State.LIBRARY)
            player.set_money(player.get_money() - 15)

        default_interactions(player, action)


def library(player):
    second_riddle(player)
    while player.get_state() is State.LIBRARY:
        action = input(">>> ").lower()
        if action == "read book":
            player.set_state(State.BOOK)
        elif action == "get coffee":
            if player.get_money() > 0:
                player.set_state(State.COFFEE)
            else:
                print("no money left for buying a coffee")
        default_interactions(player, action)


def new_game(player):
    while player.get_state() is State.NEW_GAME:
        action = input(">>> ").lower()
        if action == "yes":
            player.set_state(State.START)
        elif action == "no":
            player.set_state(State.EXIT)
        else:
            print("Sorry, I don't understand. Is this a 'yes' or a 'no'?")


def second_riddle(player):
    pass


def default_interactions(player, action):
    if action == "inspect bag":
        player.inspect_bag()
    elif action == "exit":
        player.set_state(State.NEW_GAME)
    else:
        print("Sorry, this action is not possible! Try someting else.")


def game_loop():
    # Set game's state initially to START
    state = State.START

    # The main game loop
    while True:
        if state is State.START:
            player = initialize_player()
            continue

        if state is State.BOOK or State.COFFEE:
            scene_description(state)
            state = State.NEW_GAME
            continue

        if state is State.EXIT:
            scene_description(state)
            break

        scene_description(state)
        query_player(state)

        if state is State.POTSDAM_HBF:
            potsdam_hbf(player)
        elif state is State.TICKET_AUTOMAT:
            first_riddle(player)
            # TODO: Put payment into first_riddle()
            player.set_money(player.get_money() - 5)
        elif state is State.TRAIN_1:
            on_train_1(player)
        elif state is State.TRAIN_2:
            on_train_2(player)
        elif state is State.TICKET_CONTROL:
            ticket_control(player)
        elif state is State.FEE:
            fee(player)
        elif state is State.LIBRARY:
            library(player)
        elif state is State.NEW_GAME:
            new_game(player)

        state = player.get_state()


def main():
    game_loop()
    print("The game has ended!")


if __name__ == "__main__":
    main()
