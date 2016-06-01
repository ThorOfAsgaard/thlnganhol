from setuptools.compat import unicode

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
    returnword = []

    glyphmap = ""
    charmap = []

    found = ""
    for x in word:

        # Todo: iterate over every character, but checking 'complex' first
        # adding word[x+y] until nomore matches found
        # charmap.append(x)
        found = ""
        for seq in complex:
            y = 0
            if seq.find(x):
                found = x
                while True and y + word.index(x) < len(word):

                    found = found + word[y]
                    print(found)
                    if not seq.find(found):
                        charmap.append(found)
                        print("advancing")
                        break
                    y += 1
                    #else:

                    #    break
                # get index of x

#                print("Got:" + "".join(charmap))
#                found = "".join(charmap)
#                glyphmap += getWriting("".join(charmap))
                charmap = []
                # found = True
                continue
            else:
                found = ""
                continue
                # else:
                #     print("checking simple")
                #     for seq in simple:
                #         if "".join(charmap) == seq:
                #             glyphmap +=getWriting(seq)
                #             charmap = []
                #             continue
        if found == "":
            for seq in simple:
                if "".join(charmap) == seq:
                    glyphmap += getWriting(seq)
                    charmap = []

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
