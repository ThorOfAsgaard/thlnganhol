import Dictionary
import CommonPhrases
import Flashcard

__author__ = 'thorofasgaard'
# A little program to translate and learn Klingon (tlhlngan Hol)
import FileHandler

Phrases = []
def print_menu():
    print("MENU:\n")
    print("(P)ronunciation - Using IPA \n")
    print("(D)ictionary - English/Klingon word lookup\n")
    print("(F)lashcard Game - Randomly selected words in both Klingon and English\n")
    print("(T)ranslate\n")
    print("(C)ommon Phrases - Bootstrap your tlhngan Hol knowledge\n")
    print("(A)bout\n")
    print("(Q)uit\n")
    choice = input("Select an option from above:")
    if choice.upper() == 'P':
        print("FOO")
    elif choice.upper() == "T":
        print("Foo")
    elif choice.upper() == 'F':
        Flashcard.loaddeck(20)
    elif choice.upper() == 'D':
        Dictionary.loadDictionary('dictionary')
        Dictionary.lookup(None)
    elif choice.upper() == 'C':
        CommonPhrases.loadPhrases()

    elif choice.upper() == 'Q':
        exit()
    else:
        print_menu()


def main():
    print("yI'el!")
    print_menu()
main()

if __name__ == "__main__":
    main()