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


# Eventually will return the IPA equivalents

def getklingon(word):
    syllabry = ['tlh', 'ng', 'ch', 'gh', 'a', 'b', 'D', 'e', 'gh', 'H', 'I', 'j', 'l', 'm', 'n', 'ng', 'o', 'p', 'q',
                'Q', 'r', 'S', 't', 'u', 'v', 'w', 'y', '\'']
    returnword = []

    glyphmap = ""
    charmap = ""
    for char in word:
        charmap += char
        for x in syllabry:
            if charmap == x:
                glyphmap += getWriting(charmap)
                charmap = ""
    return "<h2>" +glyphmap +"</h2>"


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
    #  print(ret)
    return ret
