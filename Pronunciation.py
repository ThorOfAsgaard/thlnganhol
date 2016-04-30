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
    simple = ['a', 'b', 'D', 'e', 'gh', 'H', 'I', 'j', 'l', 'm', 'n', 'ng', 'o', 'p', 'q',
                'Q', 'r', 'S', 't', 'u', 'v', 'w', 'y', '\'']
    complex = ['tlh', 'ng', 'ch', 'gh']
    complex_replacements = ['11111111', '22222222', '33333333', '44444444']
    returnword = []

    glyphmap = ""
    charmap = ""
    for char in word:
        charmap += char

        for y in complex:
            cunt = True
            if y.find(charmap) > -1 and cunt:
                print("nookin fo:" + charmap)
                if y == charmap:
                    print("got:" + charmap)
                    glyphmap += getWriting(charmap)
                    cunt = False
                else:
                    print("Advancing")
                    break

            else:
                print("searching basic syllabry")
                for x in simple:
                    if charmap == x:
                        print("Found in basic:" + x)
                        glyphmap += getWriting(charmap)
                        charmap = ""

    return "<h2>" + glyphmap + "</h2>"


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
