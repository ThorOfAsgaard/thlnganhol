from setuptools.compat import unicode

from Classes.GrowingList import GrowingList

__author__ = 'thorofasgaard'

import FileHandler
import Writing

pronunciation_list = {}


def loadpronunciationpatrix():
    print("Loading Pronunciation File")
    file = FileHandler.loadFile("Resources/pronunciation.csv", "r")
    for line in file:
        vals = line.split(',')

        val = vals[0] + ":" + vals[1].replace('/', '').strip()
        # pronunciation_list.update({vals[0]: unicode.encode(vals[1].replace('/', '').strip(), "utf-8")})
        pronunciation_list.update({vals[0]: vals[1].replace('/', '').strip()})
        # print(pronunciation_list)


def getIPA(word):
    ret = ""
    images = GrowingList()
    returnword = word
    word = word.strip()
    replacementTable = {}
    if word.find('tlh') > -1:
        images[word.index('tlh')] = getWriting('tlh')
    #    returnword = returnword.replace('tlh', unicode(pronunciation_list.get('tlh'), "utf-8", 'replace'))
        replacementTable.update({'tlh': getWriting('tlh')})
        word = word.replace('tlh', '')
        print('replacing tlh')
    if word.find('ng') > -1:
        images[word.index('ng')] = getWriting('ng')
       # returnword = returnword.replace('ng', unicode(pronunciation_list.get('ng'), "utf-8", 'replace'))
        replacementTable.update({'ng': getWriting('ng')})
        word = word.replace('ng', '')
        print('replacing ng')
    if word.find('ch') > -1:
        images[word.index('ch')] = getWriting('ch')
    #    returnword = returnword.replace('ch', pronunciation_list.get('ch'))
        replacementTable.update({'ch': getWriting('ch')})
        word = word.replace('ch', '')
        print('replacing ch:' + word)
    if word.find('gh') > -1:
        images[word.index('ch')] = getWriting('gh')
     #   returnword = returnword.replace('gh', unicode(pronunciation_list.get('gh'), 'utf-8', 'replace'))
        replacementTable.update({'gh': getWriting('gh')})
        word = word.replace('gh', '')
        print('replacing gh:' + word)
    for char in str(word):
      #  newchar = pronunciation_list.get(char)
        replacementTable.update({char: getWriting(char)})

       # if newchar != None:
     #       returnword = returnword.replace(char, pronunciation_list.get(char))
    imageString = "<h1>"
    for char in str(word):
        imageString = imageString + replacementTable.get(char)
    imageString = imageString + "</h1>"
    return word + imageString


def getLetter(letter):
    ret = pronunciation_list.get(letter)
    substitution = ""
    for key, value in ret:
        value = value.split(" ")
        for v in value:
            substitution = substitution + unicode(v, "hex", "replace")

    return substitution


def getWriting(char):
    ret = ""
    # for char in str(word):
    ret += Writing.getLetter(char)

    return ret
