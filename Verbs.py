import FileHandler
import nltk
__author__ = 'thor'
import Dictionary
import Grammar
suffixes = {}
modals = {}
person = {}
imperitive = {}


def loadfiles():
    Dictionary.loadDictionary('klingon')
    global suffixes, modals, person, imperitive

    file = FileHandler.loadFile("Resources/person.csv", "r")
    for line in file:
        line = line.strip()
        p = line.split(',')
        print(len(p))
        person.update({p[0]: [p[1], p[2], p[3], p[4], p[5], p[6], p[7]]})
    file.close()
    file = FileHandler.loadFile("Resources/modals.csv", "r")
    for line in file:
        line = line.strip()
        p = line.split(',')
        modals.update({p[0]: [p[1]]})
    file.close()
    file = FileHandler.loadFile("Resources/suffixes.csv", "r")
    for line in file:
        line = line.strip()
        p = line.split(',')
      #  print(str(p))
        suffixes.update({p[0]: [p[1]]})
    file.close()
    file = FileHandler.loadFile("Resources/imperative.csv", "r")
    for line in file:
        line = line.strip()
        p = line.split(',')
        imperitive.update({p[0]: [ p[1], p[2], p[3], p[4]]})


def conjugatetable():
    word = input("Conjugate a word (English to Klingon or Klingon to English:")
    #print("Conjugating " + word)
    if word == "":
        return
    word = Dictionary.returnword(word).split(":")
    print("First Person Singular:")

    firstsing = person.get('1st sing')
    print(firstsing)
    print('No Object:' + firstsing[0] + word[0] + " -- I " + word[1])
    print('1st Singular:' + firstsing[1] + word[0] + " -- I  " + word[1] + " (Myself)")
    print('2nd Singular:' + firstsing[2] + word[0] + " -- I  " + word[1] + " You")
    print('3rd Singular:' + firstsing[3] + word[0] + " -- I  " + word[1] + " Him/Her")
    print('1st Plural:' + firstsing[4] + word[0] + " -- I  " + word[1] + " Us")
    print('2nd Plural:' + firstsing[5] + word[0] + " -- I  " + word[1] + " You guys")
    print('3rd Plural:' + firstsing[6] + word[0] + " -- I  " + word[1] + " Them")
    ret = ""
    firstsing = person.get('2nd sing')
    print('No Object:' + firstsing[0] + word[0] + " -- You " + word[1])
    print('1st Singular:' + firstsing[1] + word[0] + " -- You  " + word[1] + " Me")
    print('2nd Singular:' + firstsing[2] + word[0] + " -- You  " + word[1] + " Yourself")
    print('3rd Singular:' + firstsing[3] + word[0] + " -- You  " + word[1] + " Him/Her")
    print('1st Plural:' + firstsing[4] + word[0] + " -- You  " + word[1] + " Us")
    print('2nd Plural:' + firstsing[5] + word[0] + " -- You  " + word[1] + " Yourselves")
    print('3rd Plural:' + firstsing[6] + word[0] + " -- You  " + word[1] + " Them")
    return ret

def translate():
    sentence = input("Enter your sentence and watch crazy things happen:")
    tokens = nltk.word_tokenize(sentence)
    tagged = nltk.pos_tag(tokens)
    print(type(tagged))
    print("Tagged:" + str(tagged))
    Grammar.wordorder(tagged,sentence)
    ##TODO: use tagged to build a grammar

def print_menu():
    print("(C)onjugate a verb")
    print("(T)ranslate a sentence")
    print("(Q)uit")
    choice = input("?")
    if choice.upper() == "Q":
        quit()
    if choice.upper() == "C":
        conjugatetable()
    if choice.upper() == "T":
        translate()

def main():
    print("yI'el!")
    print_menu()

loadfiles()
main()

if __name__ == "__main__":
    main()
