# -*- coding: utf-8 -*-
# Zweck der Datei
# Lara Hoppe
# 25.07.2021
import time

exit = ['exit']
no = ['n', 'no']
yes = ['y', 'yes']
gettrain = ['get train', 'train']
buyticket = ['buy ticket', 'train ticket']
inspectbag = ['inspect bag', 'open bag', 'look in bag']
gettogolm = ['get to golm', 'golm station', 'go to golm']
showticket = ['show ticket', 'present ticket', 'show the ticket']
payfee = ['pay fee', 'pay up', 'pay the fee', 'pay the charge', 'pay the sum']
getcoffee = ['get coffee', 'get espresso', 'get cappuccino', 'get latte macchiato']
readbook = ['read book', 'read the book', 'study for exam', 'study book', 'study the book']
bag_inventory = ['20€']


def potsdam_centralstation():
    '''

    This function starts the game with an introduction text and lets the player choose if they wanna
    get the train and continue with the game, exit or start again. If the player doesnt say 'exit' or continue
    with the game, it will start again.

    '''


print('\n You are sitting on a Bench at the Tram Station at Potsdam Central Station. You look at the timetable '
      'and see that you tram will arrive in 7 minutes. You close your eyes and feel the sunlight on your face.')
time.sleep(2)
print("\n When suddenly, you remember that you forgot that you didn't got the book from the library, "
      "which you need to study for next weeks exam.")
print("Do you want to hurry and go get the next train to Golm before the library closes?")
answer = input('>>>')
if answer in gettrain or yes:
    print("It seems like you've lost your semester ticket. "
          "You need to buy a ticket to get on the train. What do you wanna do?")
    answer = input('>>>')
    if answer in buyticket:
        ticket_machine()
    else:
        print('You should have bought the ticket when you still could.')
        start_again()
if answer in inspectbag:
    print('You have ' + string(bag_inventory) + ' in your bag')
if answer in gettogolm:
    if 'ticket' is in bag_inventory and get_train == True:
        get_to_golm()
    else:
        print('Its not possible to just beam yourself to Golm. Try getting the train instead.')
if answer in exit:
    print('Do you really wanna quit now and fail the exam?')
    leave_game()
if answer in no:
    print("No, doesn't answer the question ...")
    start_again()
else:
    print("You are really something, you've managed to say literally nothing.")
    start_again()


def leave_game():
    answer = input('>>>')
    if answer in yes:
        exit()
    if answer in no:
        print('You have to start again as punishment for wanting to leave for a second.')
        potsdam_centralstation()
    if answer in exit:
        exit()
    else:
        print("It's a simple yes or no question, let's try again. "
              "Do you wanna fail your exam because you quit the game? Yes or No?")
        leave_game()


def ticket_machine():
    print('---- TICKET MACHINE ----')


def start_again():
    pass