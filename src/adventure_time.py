#!/usr/bin/env python

from enum import Enum, auto
import random
import nltk
import time


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
    REPLAY = auto()
    EXIT = auto()


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
        "query": "ticket automat query"
    },
    State.TRAIN_1: {
        "opening": "Train 1 opening text",
        "query": "train 1 query"
    },
    State.TRAIN_2: {
        "opening": "Train 1 opening text",
        "query": "train 2 query"
    },
    State.TICKET_CONTROL: {
        "opening": "Ticket control opening",
        "query": "ticket control query"
    },
    State.FEE: {
        "opening": "Fee opening",
        "query": "fee query"
    },
    State.LIBRARY: {
        "opening": "Library opening",
        "query": "library query"
    },
    State.BOOK: {
        "opening": "Book opening",
    },
    State.COFFEE: {
        "opening": "Coffee opening",
    },
    State.REPLAY: {
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
        print("Your bag contains: Stuff")

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

    def put_book_into_bag(self):
        self.bag['book'] = True

    def has_book(self):
        return self.bag['book'] is not None


def initialize_player():
    return Player()


def scene_description(state):
    print(texts[state]["opening"])


def query_player(state):
    print(texts[state]["query"])


def potsdam_hbf(player):
    while player.get_state() is State.POTSDAM_HBF:
        action = input(">>> ").lower()
        standard_interactions(player, action)

        if action == "buy ticket":
            print("OK, let's go buy a ticket!")
            player.set_state(State.TICKET_AUTOMAT)
        elif action == "get train":
            print("No ticket! Buy one first!")
        else:
            print("Sorry, this action is not possible! Try someting else.")


def first_riddle(player):
    start_time = time.time()
    while player.get_state() is State.TICKET_AUTOMAT:
        present_time = time.time()
        if present_time - start_time > 120:
            player.set_state(State.TRAIN_2)

        alice = nltk.corpus.gutenberg.raw("carroll-alice.txt")
        alice = alice \
            .replace("\n", " ") \
            .replace("\r", " ")
            #  .replace("\' ", " ") \
            #  .replace(" \'", " ")

        tokenized_sentences = nltk.sent_tokenize(alice)

        # get random sentence from alice_tokenized_sentences list
        random_sentence = random.choice(tokenized_sentences)

        print('this is the random sentence :\n' + random_sentence)

        # tokenize the chosen sentence
        #  tokenizer = nltk.RegexpTokenizer(r"\w+")
        #  word_tokens = tokenizer.tokenize(random_sentence.lower())
        word_tokens = nltk.word_tokenize(random_sentence)
        print(word_tokens)

        # get random word index
        # if the word is not a type of punctuation, it is chosen
        random_word_index = -1  # TODO: if necessary
        while True:
            random_word_index = random.randint(0, len(word_tokens) - 1)
            if not word_tokens[random_word_index] in ".,!?':;":
                break

        solution = word_tokens[random_word_index]

        # get the pos tag for each word in the sentence
        pos_tag_list = nltk.pos_tag(word_tokens)
        pos_tag_of_word = f"{pos_tag_list[random_word_index][1]}"

        word_tokens[random_word_index] = f"<{pos_tag_of_word}>"
        output_sentence = " ".join(word_tokens) \
            .replace(" ,", ",") \
            .replace(" .", ".") \
            .replace(" :", ":") \
            .replace(" !", "!") \
            .replace(" ?", "?") \
            .replace(" ;", ";") \
            .replace(" \'", "\'")
        # print the sentence
        print(f'The answer is "{solution}"')
        for i in range(0, 3):
            if player.get_state() is not State.TICKET_AUTOMAT:
                break
            if i == 0:
                print('Can you guess the missing word?')
            else:
                print('Have another try.')
            print(output_sentence)
            answer = input(">>> ").lower()
            standard_interactions(player, answer)
            # put the cheating rule in place
            if answer == '###':
                print("Okay, this time I'm gonna turn a blind eye."
                      f"If you're interested, the solution was '{solution}'.")
                player.set_state(State.TRAIN_1)
            # if the right word was guessed, you win the riddle
            if answer == solution:
                print(f"That's correct! It's '{solution}'. Here is your trainticket.")
                player.set_state(State.TRAIN_1)
            else:
                print("I'm sorry that's not the word. Try again!")


def on_train_1(player):
    random.seed()
    # Generate a random number for 60% chance to get into a ticket control
    chance = random.randint(1, 100)
    while player.get_state() is State.TRAIN_1:
        action = input(">>> ").lower()
        standard_interactions(player, action)

        if action == "get to golm":
            if chance <= 40:
                player.set_state(State.LIBRARY)
            else:
                player.set_state(State.TICKET_CONTROL)
        else:
            print("Sorry, this action is not possible! Try someting else.")


def on_train_2(player):
    while player.get_state() is State.TRAIN_2:
        action = input(">>> ").lower()
        standard_interactions(player, action)

        if action == "get to golm":
            player.set_state(State.COFFEE)
        else:
            print("Sorry, this action is not possible! Try someting else.")


def ticket_control(player):
    # Generate random number for the 50% chance of an invalid ticket
    chance = random.randint(1, 100)
    while player.get_state() is State.TICKET_CONTROL:
        action = input(">>> ").lower()
        standard_interactions(player, action)

        if action == "show ticket":
            if chance <= 50:
                player.set_state(State.FEE)
            else:
                player.set_state(State.LIBRARY)
        else:
            print("Sorry, this action is not possible! Try someting else.")


def fee(player):
    while player.get_state() is State.FEE:
        action = input(">>> ").lower()
        standard_interactions(player, action)

        if action == "pay fee":
            player.set_state(State.LIBRARY)
            player.set_money(player.get_money() - 15)
        else:
            print("Sorry, this action is not possible! Try someting else.")


def library(player):
    second_riddle(player)
    while player.get_state() is State.LIBRARY:
        action = input(">>> ").lower()
        standard_interactions(player, action)

        if action == "read book":
            player.set_state(State.BOOK)
        elif action == "get coffee":
            if player.get_money() > 0:
                player.set_state(State.COFFEE)
            else:
                print("no money left for buying a coffee")
        else:
            print("Sorry, this action is not possible! Try someting else.")


def replay(player):
    while player.get_state() is State.REPLAY:
        action = input(">>> ").lower()
        if action == "yes":
            player.set_state(State.START)
        elif action == "no":
            player.set_state(State.EXIT)
        else:
            print("Sorry, I don't understand. Is this a 'yes' or a 'no'?")


def second_riddle(player):
    pass


def standard_interactions(player, action):
    if action == "inspect bag":
        player.inspect_bag()
    elif action == "exit":
        player.set_state(State.REPLAY)


def game_loop():
    # Set game's state initially to START
    state = State.START
    player = None

    # The main game loop
    while True:
        if state is State.EXIT:
            scene_description(state)
            break

        if state is State.START:
            player = initialize_player()
            state = player.get_state()

        if state in [State.BOOK, State.COFFEE]:
            scene_description(state)
            state = State.REPLAY

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

        state = player.get_state()


def main():
    game_loop()
    print("The game has ended!")


if __name__ == "__main__":
    main()
