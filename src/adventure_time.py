#!/usr/bin/env python

from enum import Enum, auto
import random
import nltk
from nltk.corpus import wordnet as wn
import time
import csv


class State(Enum):
    START = auto()
    POTSDAM_HBF = auto()
    TICKET_AUTOMAT = auto()
    TRAIN_1 = auto()
    TRAIN_2 = auto()
    TICKET_CONTROL = auto()
    FEE = auto()
    LIBRARY = auto()
    GOT_BOOK = auto()
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
    State.GOT_BOOK: {
        "opening": "Got book opening",
        "query": "got book query"
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
    # TODO: 'name' is an optional feature yet to implement
    # name = random.choice(["John", "Jane"])
    bag = {'money': 20, 'ticket': None, 'book': None}
    state = State.POTSDAM_HBF

    # TODO: Only necessary if name field is used
    # def __init__(self, name):
    #     if name != "":
    #         self.name = name

    def inspect_bag(self):
        print("Your bag contains:")
        print(f"➜ {self.bag['money']} euros")
        if self.bag['ticket'] is not None:
            print(f"➜ a train ticket")
        if self.bag['book'] is not None:
            print(f"➜ the book 'Analysis I for Computer Scientists'")

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
        if standard_interactions(player, action):
            continue

        if action == "buy ticket":
            print("OK, let's go buy a ticket!")
            player.set_state(State.TICKET_AUTOMAT)
        elif action == "get train":
            print("No ticket! Buy one first!")
        else:
            print("Sorry, this action is not possible! Try something else.")


def first_riddle(player):
    start_time = time.time()
    while player.get_state() is State.TICKET_AUTOMAT:
        current_time = time.time()
        if current_time - start_time > 120:
            player.set_state(State.TRAIN_2)
            player.set_money(player.get_money() - 5)
            player.put_ticket_into_bag()
            continue

        alice = nltk.corpus.gutenberg.raw("carroll-alice.txt")
        alice = alice \
            .replace("\n", " ") \
            .replace("\r", " ") \
            .replace("\' ", " ") \
            .replace(" \'", " ") \

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
        print(f"»{output_sentence}«")
        print("Can you guess the missing word?")
        for i in range(0, 3):
            if player.get_state() is not State.TICKET_AUTOMAT:
                break

            answer = input(">>> ").lower()
            if standard_interactions(player, answer):
                i -= 1
                continue

            # put the cheating rule in place
            if answer == "###":
                print("Okay, this time I'm gonna turn a blind eye.")
                print(f"If you're interested, the solution was '{solution}'.")

            # if the right word was guessed, the player wins the riddle
            if answer == solution:
                print(f"That's correct! It's »{solution}«. Here is your train ticket.")

            # if solved, change state, add ticket to bag, and take money from player
            if answer in ["###", solution]:
                player.set_state(State.TRAIN_1)
                player.put_ticket_into_bag()
                player.set_money(player.get_money() - 5)
            else:
                print("I'm sorry, that's not the searched word. Try again!")
                print(f"»{output_sentence}«")


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
            print("Sorry, this action is not possible! Try something else.")


def on_train_2(player):
    while player.get_state() is State.TRAIN_2:
        action = input(">>> ").lower()
        if standard_interactions(player, action):
            continue

        if action == "get to golm":
            player.set_state(State.COFFEE)
        else:
            print("Sorry, this action is not possible! Try something else.")


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
            print("Sorry, this action is not possible! Try something else.")


def fee(player):
    while player.get_state() is State.FEE:
        action = input(">>> ").lower()
        if standard_interactions(player, action):
            continue

        if action == "pay fee":
            player.set_state(State.LIBRARY)
            player.set_money(player.get_money() - 15)
        else:
            print("Sorry, this action is not possible! Try something else.")


def got_book(player):
    while player.get_state() is State.GOT_BOOK:
        action = input(">>> ").lower()
        if standard_interactions(player, action):
            continue

        if action == "read book":
            player.set_state(State.BOOK)
        elif action == "get coffee":
            if player.get_money() > 0:
                player.set_state(State.COFFEE)
            else:
                print("no money left for buying a coffee")
        else:
            print("Sorry, this action is not possible! Try something else.")


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
    """
    This function starts the second game in which the player has to guess the animal
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
        while player.get_state() is State.LIBRARY:
            # get random animal
            animal_name = random.choice(list(reader))[0]
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
                    print(f"The animal was {animal_name}.")
                    print("Congratulations! You cheated your way through this game, "
                          "your parents must be proud. Go take your book")
                # if player's guess is the random animal
                elif action == animal_name:
                    # they won the game and get the book
                    print("Congratulations! You guessed the animal! Now you can finally "
                          "take the book home with you ")

                if action in [animal_name, "###"]:
                    player.put_book_into_bag()
                    player.set_state(State.GOT_BOOK)
                    continue
                else:
                    print("Unfortunately that's not the searched animal. Have another guess!")

            if player.get_state() is State.LIBRARY:
                print(f"The animal was {animal_name}. Here is a new animal to guess. Good Luck.")


def standard_interactions(player, action):
    matched = False
    if action == "inspect bag":
        player.inspect_bag()
        matched = True
    elif action == "exit":
        player.set_state(State.REPLAY)
        matched = True
    return matched


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
            player.set_state(State.REPLAY)
            state = player.get_state()
            continue

        scene_description(state)
        query_player(state)

        if state is State.POTSDAM_HBF:
            potsdam_hbf(player)
        elif state is State.TICKET_AUTOMAT:
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
        elif state is State.REPLAY:
            replay(player)

        state = player.get_state()


def main():
    game_loop()
    print("The game has ended!")


if __name__ == "__main__":
    # player = Player()
    # player.set_state(State.LIBRARY)
    # second_riddle(player)
    main()
