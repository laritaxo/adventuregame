import csv
import random

from nltk.corpus import wordnet


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
        # for loop for the 3 tries the player gets
        for i in range(1,4):
            try:
                guess = input("Can you guess the animal? >>> ")
            # if EOFError get out of the for loop
            except EOFError:
                print("EOFError")
                break
            # if player's guess is not the random animal or cheat
            if guess != animal_name and guess != '###':
                # goes on to next loop
                print("Sorry. You guessed wrong. Try again.")
            # if player's guess is cheat
            elif guess == '###':
                # get out of for loop
                break
            # if player's guess is either right or the 3 guesses are over, get out of loop
            else:
                break
        # if player's guess is not the random animal or cheat after 3 guesses they lose
        if guess != animal_name and guess != '###':
            print(f"The animal was {animal_name}. Here is a new animal to guess. Good Luck.")
            # player doesn't get the book
            get_book(False)
            # game starts again
            guess_animal_name()
        # if player's guess is the cheat
        elif guess == "###":
            # animal gets revealed
            print(f"The animal was {animal_name}.")
            # player gets the book and finishes the game
            print("Congratulations! You cheated your way through this game, "
                  "your parents must be proud. Go take your book")
            get_book(True)
        # if player's is the random animal
        elif guess == animal_name:
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