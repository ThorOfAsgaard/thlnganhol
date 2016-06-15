from nltk.corpus import wordnet

import FileHandler
import NLTK_Functions
import Pronunciation as p

__author__ = 'thorofasgaard'

dictionary = {}
complete_dictionary = {}
translation = {}
server = False  # global flag to indicate whether or not to use__main__ and print menus
mode = ""


## dictionary.csv = Klingon/English

def tag_part_of_speech(line):
    return NLTK_Functions.get_parts_of_speech(line)

    ##TODO - grab part of speech for English translation, if possible


def loadDictionary(language):
    """

    :param language:
    :return:
    """
    global mode
    mode = language
    file = FileHandler.loadFile("Resources/" + language + ".csv", "r")
    for line in file:
        vals = line.split(',')
        # check to make sure their not blank
        if vals[0] == '':
            continue
        value = ""
        for i in range(1, len(vals)):
            if vals[i].strip() != '' and vals[i] is not None:
                value += vals[i].strip() + " ,"
        ret = {vals[0].strip(): value.strip()}
        dictionary.update(ret)

    #create the reverse
    for key, value in dictionary.items():
        vals = value.split(",")
        for v in vals:
           translation.update({v.strip(): key})
    print("**************** Dictionary File Loaded ****************")
    return dictionary


def find_synonyms(query):
    word = ""
    if query is None:
        word = input('Enter the word you want to find Synonyms for:')
        query = word
    ret = None
    list = []
    synonyms = wordnet.synsets(query)
    if synonyms is not None:
        for syn in synonyms:
            r = syn.lemma_names()  # list
            # (key, value) in r
            list.append(r)
  #  print(str(list))
    return list


def global_menu():
    print("Global Menu\n")
    print("(H)ome screen\n")
    print("(R)eturn to previous screen\n")
    print("(Q)uit\n")


def returnEnglish(klingon):
    """

    :param klingon:
    :return:
    """
    word = ""

    if klingon is None:
        word = input('Enter your query, type "Q" to quit:')
        if word.upper() == 'Q':
            return
        klingon = word
    for key, value in dictionary.items():
        if klingon.upper() in str(key).upper():
            value = value.replace(",", "").strip()
            return value
    if not server:
        returnEnglish(None)


def returnKlingon(english):
    """


    :rtype : string
    :param english:
    :return:
    """
    print("""
    English -> Klingon
    """)
    word = english

    if word is None:
        word = input("Enter the English query:")
        if word.upper() == "Q":
            return

    #first, check the translation dictionary
    if word in translation:
        print("Got "+word +" in translation:" + translation.get(word))
        return translation.get(word)
    syns = find_synonyms(english)

    for key, value in dictionary.items():
        vals = value.split(",")
        for v in vals:
            if word.upper() == v.upper().strip():
                return key.replace(",", "").strip()

    ##
    # for key, value in dictionary.items():
    #     for syn in syns:
    #         for s in syn:
    #             if word.upper() == s.upper().strip():
    #                 print("foo")

        # if word.upper() in str(value).upper():
        #     word = key.replace(",", "").strip()
        #     print(word)
        #     return word

        # TODO: Maybe use 'synonyms' first
        # if not server:
        #     returnKlingon(None)


def returnword(word):
    ret = ""
    for key, value in dictionary.items():
        if word.upper() in str(key).upper() or word.upper() in str(value).upper():
            value = value.replace(",", "").strip()
            ret = str(key) + ":" + value
    return ret


def lookup(query):
    global server, complete_dictionary
    ## TODO: use nltk to find synonyms
    ret = ""
    if query is None:
        word = input('Enter your query, type "Q" to quit:')
        if word.upper() == 'Q':
            return
        if word.upper() == 'M':
            main()
    else:
        word = query

    # word = input('Enter your query, type "Q" to quit:')
    # keys = dictionary.keys()

    retArray = []
    # Pronunciation.loadpronunciationpatrix()
    ret = returnKlingon(word.strip())

    # for key, value in dictionary.items():
    #     if (key is not None and value is not None) and (
    #                     word.upper() in str(key).upper() or word.upper() in str(value).upper()):
    #         value = value.replace(",", "").strip()
    #         ret = str(key) + ":" + value
    #         #       pron = "" + Pronunciation.getklingon(key) + ""
    #         #      ret = ret + " " + pron
    #         # chars = Pronunciation.getWriting(key)
    #         # ret = ret + chars
    #         print("Found a match, getting definition for " + key + ":" + str(complete_dictionary.get(key)))
    #         retArray.append(ret)
    #         if server:
    #             retArray.append(str(p.getklingon(key)))

    if ret is "" or ret is None:
        ret = 'Unable to find "' + word + '" in the dictionary'
    else:
        ret = ret + p.getklingon(ret)
        ret = word + ': ' + ret

    retArray = ret

    print(retArray)

    if not server:
        lookup(None)
    return retArray


def main():
    loadDictionary("dictionary")
    update_definitions()
    print("""
    MENU:
    (L)ookup
    (S)ynonyms
    (K)lingon
    (E)nglish""")
    global_menu()
    choice = input("Select an option from above:")
    if choice.upper() == 'L':
        lookup(None)
    elif choice.upper() == 'S':
        find_synonyms(None)
    elif choice.upper() == 'K':
        returnKlingon(None)
    elif choice.upper() == 'E':
        returnEnglish(None)
    elif choice.upper() == 'Q':
        quit()
    elif choice.upper() == 'M':
        main()
    elif choice.upper() == 'R':
        main()
    else:
        main()


def update_definitions():
    global complete_dictionary
    print("**************** Grabbing Definitions from Wordnet ****************")
    for key, value in dictionary.items():
        definitions = []
        values = value.split(",")
        list = []
        for val in values:
            if val.strip() is None:
                return
            synonyms = wordnet.synsets(val.strip())
            if synonyms is not None and val.strip() is not None:
                # print("#grabbing the definition for  " + val)
                for syn in synonyms:
                    definition = syn.definition()
                    list.append(definition)
                    # print("Defintion for " + val + ":" + definition)

        complete_dictionary.update({key: list})

    # if __name__ == "__main__":
    #     main()


    ##TODO: use synonyms or wordnet to grab definition
    ##TODO: write definition to the csv file first time
loadDictionary("dictionary")