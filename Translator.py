__author__ = 'thorofasgaard'

import nltk

import Dictionary
import KlingonTranslator
import Verbs
import Grammar

# Will eventually allow for english to klingon / vice versa translation -
# requires NLTK

server = False
previous = ""


def translate(sentence):
    if sentence is None or server is False:
        sentence = input("Enter your sentence and watch crazy things happen:")
    tokens = nltk.word_tokenize(sentence)
    tagged = nltk.pos_tag(tokens)
    print(type(tagged))
    print("Tagged:" + str(tagged))
    Grammar.wordorder(tagged, sentence)


def main():
    print("""MENU:
    (T)ranslate
    (P)revious screen
    (H)ome screen
    (Q)uit


    """)
    choice = input("What would you like to do?")
    if choice.upper() == "T":
        translate()
    elif choice.upper() == "P":
        if previous.upper == "VERBS":
            Verbs.main()
        elif previous.upper == "DICTIONARY":
            Dictionary.main()
        elif previous.upper == "HOME":
            KlingonTranslator.main()
        else:
            main()


#if __name__ == "__main__":
#    main()
