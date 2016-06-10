from nltk.corpus import wordnet

import FileHandler
import NLTK_Functions

__author__ = 'thorofasgaard'

dictionary = {}
translation = {}
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

    return list


def returnEnglish(klingon):
    """

    :param klingon:
    :return:
    """
    for key, value in dictionary.items():
        if klingon.upper() in str(key).upper():
            value = value.replace(",", "").strip()
            return value


def returnKlingon(english):
    """


    :rtype : string
    :param english:
    :return:
    """
    for key, value in dictionary.items():
        if english.upper() in str(value).upper():
            key = key.replace(",", "").strip()
            return key


def returnword(word):
    ret = ""
    for key, value in dictionary.items():
        if word.upper() in str(key).upper() or word.upper() in str(value).upper():
            value = value.replace(",", "").strip()
            ret = str(key) + ":" + value
    return ret


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
    # Pronunciation.loadpronunciationpatrix()
    for key, value in dictionary.items():
        if word.upper() in str(key).upper() or word.upper() in str(value).upper():
            value = value.replace(",", "").strip()
            ret = str(key) + ":" + value
            #       pron = "" + Pronunciation.getklingon(key) + ""
            #      ret = ret + " " + pron
            # chars = Pronunciation.getWriting(key)
            # ret = ret + chars
            retArray.append(ret)

    if ret is "":

        ret = 'Unable to find "' + word + '" in the dictionary'
    else:
        ret = word + ': ' + str(ret)

    print(retArray)
    return retArray

    # lookup()
