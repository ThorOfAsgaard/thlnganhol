from collections import OrderedDict
import random

__author__ = 'thorofasgaard'
import LoadDictionary
import math
# A basic Flashcard game

deck = []
correct = []
incorrect = []
asked = []

def createdeck():
    deckname = input("Enter the name of your deck");


def opendeck():
    # TODO: get a list of the decks available
    deckname = input("Which deck would you like to open?");




def menu():
    print('==================== FLASHCARDS MENU ====================')
    print('(P)lay the game')
    print('(R)eturn to main menu')
    choice = input('Select an option:')
    if choice.upper() == 'P':
        playgame()
    else:
        return


def playgame():
    correct = []
    incorrect = []
    print('Game starting')
    while len(deck) > 0:
        ask_question()
    print("Your score:" + str(len(correct)) +"/" + str(len(correct)+len(incorrect)))
    choice = input("Would you like to see which questions you missed? Y/N")
    if choice.upper() == 'Y':
        for item in incorrect:
            print(item +"\n")

    menu()

def ask_question():
    num = random.randrange(0, len(deck))
    question = deck[num]
    asked.append(question)
    answers = [question]

    # print(question)
    del deck[num]
    x = 0
    while x < 4 and len(deck) > 0:
        answers.append(deck[random.randrange(0, len(deck))])
        x += 1
    x = 0
    (key, value) = question
    print("========================= QUESTION " + str(len(asked)) + ":   " + key.upper() + "  =========================")
    randanswers = []
    x = 0;
    while len(answers) > 0:
        num = random.randrange(0, len(answers))
        randanswers.append(answers[num])
        (key, value) = answers[num]
        print("(" + str(x+1) + ")" + value)
        x += 1
        del answers[num]

    print("(Q)uit")
    choice = input("Choose the correct answer:")
    if choice.upper() == 'Q':
        menu()
    elif randanswers[int(choice)-1] == question:
        print("==================== Correct ====================")
        correct.append(asked[0])
    else:
        print("==================== Incorrect ====================")
        incorrect.append(asked[0])
    del asked[0]


def loaddeck(numcards):
    global deck
    tempDict = OrderedDict(LoadDictionary.loadDictionary("klingon"))
    tempDeck = []
    for key, value in tempDict.items():
        item = {key, value}
        tempDeck.append(item)

    x = 0
    while x < numcards:
        num = random.randrange(0, len(tempDeck) - 1)
        deck.append(tempDeck[num])
        del (tempDeck[num])
        x += 1

    menu()
