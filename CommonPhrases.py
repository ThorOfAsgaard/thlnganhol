import FileHandler
__author__ = 'ntallmon'

phrases = {}


def loadPhrases():
    file = FileHandler.loadFile('Resources/CommonPhrases.csv', 'r')
    for line in file:
        details = line.split(',')
        values = ""
        for x in range(1, len(details)):
            values +=details[x].strip()+ ","

        entry = {details[0]: {values}}
        phrases.update(entry)
    phrases_menu()


def phrases_menu():
    print('(S)earch for a phrase\n')
    print('(L)ist all phrases\n')
    print('(R)eturn to main menu\n')
    choice= input('Select an option')

    if choice.upper() == 'S':
        search_phrases()
    elif choice.upper() == 'L':
        list_phrase()
    elif choice.upper() == 'R':
        return


def list_phrase():
    for key, value in phrases.items():
        print(key.upper() + ":" + str(value) +'\n')
    phrases_menu()


def search_phrases():
    phrase = input("Enter query to search for a phrase:")
    ret = "UNABLE TO FIND " + phrase
    for key, value in phrases.items():
        if phrase.lower() in key.lower():
            ret = "MATCH FOUND:" + phrase + ":" + str(value)
    print(ret)
    phrases_menu()



