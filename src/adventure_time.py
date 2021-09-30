#!/usr/bin/env python

from enum import Enum, auto
import random
import nltk
from nltk.corpus import wordnet as wn
import time
import csv
import json


texts = {}
invalid = {}


class State(Enum):
    START = auto()
    POTSDAM_HBF = auto()
    TICKET_MACHINE = auto()
    TRAIN_1 = auto()
    TRAIN_2 = auto()
    TICKET_CONTROL = auto()
    FEE = auto()
    LIBRARY = auto()
    GOT_BOOK = auto()
    NO_BOOK = auto()
    COFFEE = auto()
    BOOK = auto()
    REPLAY = auto()
    EXIT = auto()


class Player:
    bag = {}
    state = None

    def __init__(self):
        self.bag = {'money': 20, 'ticket': False, 'book': False}
        self.state = State.POTSDAM_HBF

    def inspect_bag(self):
        print("Your bag contains:")
        print(f"➜ {self.bag['money']} euros")
        if self.bag['ticket'] is True:
            print("➜ a train ticket")
        if self.bag['book'] is True:
            print("➜ the book 'Analysis I for Computer Scientists'")

    def get_state(self):
        return self.state

    def get_state_str(self):
        return self.state.name

    def set_state(self, state):
        self.state = state

    def get_money(self):
        return self.bag['money']

    def set_money(self, amount):
        self.bag['money'] = amount

    def pay_ticket(self):
        self.bag['money'] -= 5

    def put_ticket_into_bag(self):
        self.bag['ticket'] = True

    def pay_fee(self):
        self.bag['money'] -= 15

    def has_ticket(self):
        return self.bag['ticket'] is True

    def put_book_into_bag(self):
        self.bag['book'] = True

    def has_book(self):
        return self.bag['book'] is True


def initialize_player():
    return Player()


def scene_description(state):
    print(texts[state.name]["scene_description"])


def query_player(state):
    print(texts[state.name]["query"])


def potsdam_hbf(player):
    while player.get_state() is State.POTSDAM_HBF:
        action = input(">>> ").lower()
        if standard_interactions(player, action):
            continue

        if action == "buy ticket":
            print(texts[player.get_state_str()][action])
            player.set_state(State.TICKET_MACHINE)
        elif action == "get train":
            print(texts[player.get_state_str()][action])
        else:
            invalid_input_reply()


def first_riddle(player):
    start_time = time.time()
    while player.get_state() is State.TICKET_MACHINE:
        alice = nltk.corpus.gutenberg.raw("carroll-alice.txt")
        alice = alice \
            .replace("\n", " ") \
            .replace("\r", " ") \

        sentence_tokens = nltk.sent_tokenize(alice)

        # get random sentence from alice_tokenized_sentences list
        random_sentence = random.choice(sentence_tokens)
        # print(f"This is the random sentence:\n\n{random_sentence}")

        # tokenize the chosen sentence
        word_tokens = nltk.word_tokenize(random_sentence)
        # print(f"These are the word tokens:\n\n{word_tokens})

        # get random word index
        # if the word is not a type of punctuation, it is chosen
        while True:
            random_word_index = random.randint(0, len(word_tokens) - 1)
            if word_tokens[random_word_index].isalpha():
                break

        # store the searched word
        solution = word_tokens[random_word_index]

        # generate pos tags for all words in the sentence
        pos_tag_list = nltk.pos_tag(word_tokens)

        # get the pos tag for the searched word
        pos_tag_of_word = f"{pos_tag_list[random_word_index][1]}"

        # replace the searched word with its pos tag
        word_tokens[random_word_index] = f"<{pos_tag_of_word}>"

        # rejoin the sentence and correct for unwanted spaces
        output_sentence = " ".join(word_tokens) \
            .replace(" ,", ",") \
            .replace(" .", ".") \
            .replace(" :", ":") \
            .replace(" !", "!") \
            .replace(" ?", "?") \
            .replace(" ;", ";") \
            .replace("( ", "(") \
            .replace(" )", ")") \
            .replace(" '", "'") \
            .replace("`` ", "``") \
            .replace(" n't", "n't")

        # start the 3 tries loop
        print(f"\t»{output_sentence}«")
        for i in range(0, 3):
            if player.get_state() is not State.TICKET_MACHINE:
                break

            answer = input(">>> ").lower()
            if standard_interactions(player, answer):
                i -= 1
                continue

            # put the cheating rule in place
            if answer == "###":
                print(f"{texts[player.get_state_str()][answer]} »{solution}«.")

            # if the right word was guessed, the player wins the riddle
            if answer == solution:
                print(texts[player.get_state_str()]['win'])

            # if solved, change state, add ticket to bag, and take money from player
            if answer in ["###", solution]:
                player.pay_ticket()
                player.put_ticket_into_bag()

                current_time = time.time()
                if current_time - start_time > 120:
                    player.set_state(State.TRAIN_2)
                    return

                player.set_state(State.TRAIN_1)
                return
            elif i < 2:
                print(texts[player.get_state_str()]["wrong"])
                print(f"\t»{output_sentence}«")
            else:
                print(texts[player.get_state_str()]["wrong3x"])


def on_train_1(player):
    # Generate a random number for a 60% chance to get into a ticket control
    random.seed()
    chance = random.randint(1, 100)

    while player.get_state() is State.TRAIN_1:
        action = input(">>> ").lower()
        if standard_interactions(player, action):
            continue

        if action == "get to golm":
            if chance <= 40:
                player.set_state(State.LIBRARY)
            else:
                player.set_state(State.TICKET_CONTROL)
        else:
            invalid_input_reply()


def on_train_2(player):
    """
    This function queries the player what to do on the second train.
    When the player chooses "get to golm" their state is changed to
    NO_BOOK.

    :param player: instance of Player
    """
    while player.get_state() is State.TRAIN_2:
        action = input(">>> ").lower()
        if standard_interactions(player, action):
            continue

        if action == "get to golm":
            player.set_state(State.NO_BOOK)
        else:
            invalid_input_reply()


def ticket_control(player):
    # Generate random number for the 50% chance of an invalid ticket
    random.seed()
    chance = random.randint(1, 100)

    while player.get_state() is State.TICKET_CONTROL:
        action = input(">>> ").lower()
        if standard_interactions(player, action):
            continue

        if action == "show ticket":
            if chance <= 50:
                player.set_state(State.FEE)
            else:
                player.set_state(State.LIBRARY)
        else:
            invalid_input_reply()


def fee(player):
    while player.get_state() is State.FEE:
        action = input(">>> ").lower()
        if standard_interactions(player, action):
            continue

        if action == "pay fee":
            player.pay_fee()
            player.set_state(State.LIBRARY)
        else:
            invalid_input_reply()


def second_riddle(player):
    """
    This function starts the second riddle in which the player has to guess the animal
    just by reading the definition of it. The player gets 3 guesses for each randomly
    chosen animal. If the player guesses the animal correct or puts in the cheat "###"
    they win the game and get the book from the library. Else the game goes on til the
    player gets it right. The player can always exit the game with "exit()" or inspect
    their bag with "inspect_bag()".

    :player: instance of Player
    """

    # open animal.csv file
    with open('../data/animals.csv', 'r') as file:
        # read animals.csv
        reader = csv.reader(file)
        animal_list = list(reader)
    while player.get_state() is State.LIBRARY:
        # get random animal
        animal_name = random.choice(animal_list)[0]
        # get definition of the random animal
        definition = wn.synset(animal_name + '.n.01').definition()

        # allow player to guess 3 times per animal
        for i in range(0, 3):
            if player.get_state() is not State.LIBRARY:
                break
            print(f"Definition: {definition}")
            action = input(">>> ").lower()

            # the standard interaction 'check bag' is not counted as a guess
            # so the loop counter 'i' is lowered by 1 and the remaining code is
            # skipped
            if standard_interactions(player, action):
                i -= 1
                continue

            # if player's guess is the cheat
            elif action == "###":
                # animal gets revealed
                print(f"The animal was: {animal_name}")
                print(texts[player.get_state_str()][action])
            # if player's guess is the random animal
            elif action == animal_name:
                # they won the game and get the book
                print(texts[player.get_state_str()]["win"])

            if action in [animal_name, "###"]:
                player.put_book_into_bag()
                player.set_state(State.GOT_BOOK)
                return
            else:
                print(texts[player.get_state_str()]["wrong"])

        if player.get_state() is State.LIBRARY:
            print(texts[player.get_state_str()]["wrong3x"].format(animal=animal_name))


def got_book(player):
    while player.get_state() is State.GOT_BOOK:
        action = input(">>> ").lower()
        if standard_interactions(player, action):
            continue

        if action == "read book":
            player.set_state(State.BOOK)
            return
        elif action == "get coffee":
            if player.get_money() > 0:
                player.set_state(State.COFFEE)
                return
            else:
                print(texts[player.get_state_str()]["no_money"])
        else:
            invalid_input_reply()


def library_closed(player):
    while player.get_state() is State.NO_BOOK:
        action = input(">>> ").lower()
        if standard_interactions(player, action):
            continue

        elif action == "get coffee":
            player.set_state(State.COFFEE)
            return
        else:
            invalid_input_reply()


def replay(player):
    while player.get_state() is State.REPLAY:
        action = input(">>> ").lower()
        if action == "yes":
            player.set_state(State.START)
        elif action == "no":
            player.set_state(State.EXIT)
        else:
            print(texts[player.get_state_str()]["no_option"])


def standard_interactions(player, action):
    matched = False
    if action == "inspect bag":
        player.inspect_bag()
        matched = True
    elif action == "exit":
        player.set_state(State.REPLAY)
        matched = True
    return matched


def invalid_input_reply():
    random.seed()
    print(random.choice(invalid["invalid"]))


def game_loop():
    # set game's state initially to START
    state = State.START
    player = None

    # the main game loop
    while True:
        if state is State.START:
            player = Player()
            state = player.get_state()

        scene_description(state)

        if state is State.EXIT:
            return

        if state in [State.BOOK, State.COFFEE]:
            state = State.REPLAY
            player.set_state(state)

        query_player(state)

        if state is State.POTSDAM_HBF:
            potsdam_hbf(player)
        elif state is State.TICKET_MACHINE:
            first_riddle(player)
        elif state is State.TRAIN_1:
            on_train_1(player)
        elif state is State.TRAIN_2:
            on_train_2(player)
        elif state is State.TICKET_CONTROL:
            ticket_control(player)
        elif state is State.FEE:
            fee(player)
        elif state is State.LIBRARY:
            second_riddle(player)
        elif state is State.GOT_BOOK:
            got_book(player)
        elif state is State.NO_BOOK:
            library_closed(player)
        elif state is State.REPLAY:
            replay(player)

        state = player.get_state()


def main():
    global texts
    with open("../data/texts.json", "r") as texts_json:
        texts = json.load(texts_json)
    global invalid
    with open("../data/invalid.json", "r") as invalid_json:
        invalid = json.load(invalid_json)
    game_loop()


if __name__ == "__main__":
    main()
