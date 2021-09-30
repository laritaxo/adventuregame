import csv
import random
from enum import Enum, auto

from nltk.corpus import wordnet


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


def standard_interactions(player, action):
    if action == "inspect bag":
        player.inspect_bag()
    elif action == "exit":
        player.set_state(State.REPLAY)


def guess_loop(player, animal_name):
    # for loop for the 3 tries the player gets
    for _ in range(1, 4):
        try:
            action = input("Can you guess the animal? >>> ")
        # if EOFError get out of the for loop
        except EOFError:
            print("EOFError")
            break
        standard_interactions(player, action)
        # if player's guess is cheat
        if action == '###':
            # get out of for loop
            break
        elif action == animal_name:
            break
        # if player's guess is not the random animal or cheat
        elif action != animal_name:
            # goes on to next loop
            print("Sorry. You guessed wrong. Try again.")


def guess_animal_name():
    '''
    This function starts the second game in which the player has to guess the animal
    just by reading the definition of it. The player gets 3 guesses for each randomly
    chosen animal. If the player guesses the animal correct or puts in the cheat "###"
    they win the game and get the book from the library. Else the game goes on til the
    player gets it right. The player can always exit the game with "exit()" or inspect
    their bag with "inspect_bag()".
    '''

    # open animal.csv file
    with open('/temp/animals.csv', 'r') as file:
        string1 = " "
        reader = csv.reader(file)
        # get random animal
        animal_name = random.choice((list(reader)))
        # change from list to string
        animal_name = (string1.join(animal_name))
        # get definition of the random animal
        definition = wordnet.synset(animal_name + '.n.01').definition()
        print("Definition: " + definition)
            # if player's guess is either right or the 3 guesses are over, get out of loop
        # if player's guess is not the random animal or cheat after 3 guesses they lose
        if action != animal_name and action != '###':
            print(f"The animal was {animal_name}. Here is a new animal to guess. Good Luck.")
            # player doesn't get the book
            get_book(False)
            # game starts again
            guess_animal_name()
        # if player's guess is the cheat
        elif action == "###":
            # animal gets revealed
            print(f"The animal was {animal_name}.")
            # player gets the book and finishes the game
            print("Congratulations! You cheated your way through this game, "
                  "your parents must be proud. Go take your book")
            get_book(True)
        # if player's is the random animal
        elif action == animal_name:
            # they won the game and get the book
            print("Congratulations! You guessed the animal! Now you can finally "
                  "take the book home with you ")
            get_book(True)



def get_book(got_book):
    if got_book == True:
        #put book in bag
        print("yay")
    else:
        pass


if __name__ == "__main__":
    guess_animal_name()

