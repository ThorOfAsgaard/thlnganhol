from collections import OrderedDict
import random

__author__ = 'ntallmon'
import LoadDictionary
import math
# A basic Flashcard game

deck = []
correct = []
incorrect = []
asked = []


def menu():
    print('(P)lay the game')
    print('(R)eturn to main menu')
    choice = input('Select an option:')
    if choice.upper() == 'P':
        playgame()


def playgame():
    print('Game starting')
    while len(deck) > 0:
        ask_question()
    print("Your score:" + str(len(correct)) +"/" + str(len(correct)+len(incorrect)))
    menu()

def ask_question():
    num = random.randrange(0, len(deck))
    question = deck[num]
    asked.append(question)
    print(question)
    answers = [question]

    # print(question)
    del deck[num]
    x = 0
    while x < 4 and len(deck) > 0:
        answers.append(deck[random.randrange(0, len(deck))])
        x += 1
    x = 0
    (key, value) = question
    print("Question " + str(len(asked)) + ":   " + key + "")

    while x < len(answers):
        (key, value) = answers[x]
        print("(" + str(x) + ")" + value)
        x += 1
    choice = input("Choose the correct answer:")
    if answers[int(choice)] == question:
        print("Correct")
        correct.append(asked[0])
    else:
        print("Incorrect")
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
