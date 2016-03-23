from setuptools.compat import unicode

from Classes.GrowingList import GrowingList

__author__ = 'thorofasgaard'

import FileHandler
import re
import Writing

pronunciation_list = {}


def loadpronunciationpatrix():
    print("Loading Pronunciation File")
    file = FileHandler.loadFile("Resources/pronunciation.csv", "r")
    for line in file:
        vals = line.split(',')

        val = vals[0] + ":" + vals[1].replace('/', '').strip()
        print(unicode.encode(vals[1].replace('/', '').strip(), 'utf-8'))
        pronunciation_list.update({vals[0]: unicode.encode(vals[1].replace('/', '').strip(), "utf-8")})
        # print(pronunciation_list)


def getIPA(word):
    ret = ""
    images = GrowingList()
    returnword = word
    p = re.compile('[a-z][A-Z]+')
    word = word.strip()
    if word.find('tlh') > -1:
        images[word.index('tlh')] = getWriting('tlh')
        returnword = returnword.replace('tlh', unicode(pronunciation_list.get('tlh'), "utf-8", 'replace'))
        word = word.replace('tlh', '')
        print('replacing tlh')
    if word.find('ng') > -1:
        images[word.index('ng')] = getWriting('ng')
        returnword = returnword.replace('ng', unicode(pronunciation_list.get('ng'), "utf-8", 'replace'))
        word = word.replace('ng', '')
        print('replacing ng')
    if word.find('ch') > -1:
        images[word.index('ch')] = getWriting('ch')
        returnword = returnword.replace('ch', unicode(pronunciation_list.get('ch'), 'utf-8', 'replace'))
        word = word.replace('ch', '')
        print('replacing ch:' + word)
    for char in str(word):
        print(char)
        newchar = pronunciation_list.get(char)
        if newchar != None:
            returnword = returnword.replace(char, unicode(pronunciation_list.get(char), 'utf-8', 'replace'))
        if returnword.index(char) > -1 and images[word.index(char)] is None or images[word.index(char)] is 'None':
            images[returnword.index(char)] = getWriting(char)

            # print(word.index(char))
            #  images[word.index(char)] = getWriting(char)
    print(str(images))
    return returnword + str(images)


def getWriting(char):
    ret = ""
    #for char in str(word):
    ret += "<image src='" + Writing.getLetter(char) + "' width='20' height='20' />"

    return ret
