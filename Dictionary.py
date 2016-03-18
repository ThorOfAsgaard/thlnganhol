from nltk.corpus import wordnet

import FileHandler

__author__ = 'thorofasgaard'

dictionary = {}
translation = {}
mode = ""


def loadDictionary(language):
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
            if vals[i].strip() != '':
                value += vals[i].strip() + ","

        ret = {vals[0].strip(): value.strip()}
        ret2 = {value.strip(): vals[0].strip()}
        dictionary.update(ret)
        translation.update(ret2)

    print("**************** Dictionary Loaded ****************")
    return dictionary


def find_synonyms(query):
    ret = None
    list = []
    synonyms = wordnet.synsets(query)
    if synonyms is not None:
        for syn in synonyms:
            r = syn.lemma_names()  # list

            # (key, value) in r

            list.append(r)

    return str(list)


def lookup(query):
    ## TODO: use nltk to find synonyms
    ret = ""
    if query is None:
        word = input('Enter your query, type "Q" to quit:')
        if word.upper() == 'Q':
            return
    else:
        word = query
    # word = input('Enter your query, type "Q" to quit:')
    # keys = dictionary.keys()

    retArray = []

    for key, value in dictionary.items():
        if word.upper() in str(key).upper() or word.upper() in str(value).upper():
            ret = str(key) + ":" + value
            retArray.append(ret)

    if ret is "":

        ret = 'Unable to find "' + word + '" in the dictionary'
    else:
        ret = word + ': ' + str(ret)

    return retArray

    # lookup()
