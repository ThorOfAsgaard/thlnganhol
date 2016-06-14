import re
from setuptools.compat import unicode

__author__ = 'thorofasgaard'

import FileHandler
import Writing
from gtts import gTTS
pronunciation_list = {}
server = False

simple = ['a', 'b', 'D', 'e', 'gh', 'H', 'I', 'j', 'l', 'm', 'n', 'ng', 'o', 'p', 'q',
              'Q', 'r', 'S', 't', 'u', 'v', 'w', 'y', '\'']
complex = ['tlh', 'ng', 'ch', 'gh']


def loadpronunciationmatrix():
    print("Loading Pronunciation File")
    file = open("Resources/pronunciation.csv", "r", encoding='utf-8')
    for line in file:
        vals = line.split(',')

        val = vals[0] + ":" + vals[1].replace('/', '').strip()
        # pronunciation_list.update({vals[0]: unicode.encode(vals[1].replace('/', '').strip(), "utf-8")})
        pronunciation_list.update({vals[0]: vals[1].replace('/', '').strip()})
        # print(pronunciation_list)


def write_pronunciation(word):
    global complex, simple
    charmap = []
    output = ""
    if word is None:
        word = input("Enter the klingon word ->")
    for seq in complex:
        for m in re.finditer(seq, word):
            charmap.insert(m.start(), getLetter(seq))
            word = word[m.start()].replace(seq, '_')
    for seq in simple:
        for m in re.finditer(seq, word):
            charmap.insert(m.start(), getLetter(seq))
            word = word[m.start()].replace(seq, '_')
    output = "".join(charmap)
    #print(output)
    #print(charmap)

##move to Writing.py probably
def getklingon(word):
    global complex, simple
    if word is None:
        word = input("Enter the klingon word ->")
    charmap = []

    #TODO: get index of sequence
    #TODO: add key/value pairs, then reconstruct the word?
    for seq in complex:
        for m in re.finditer(seq, word):
            charmap.insert(m.start(), getWriting(seq))
            word = word.replace(seq, '_')

    for seq in simple:
          for m in re.finditer(seq, word):

            charmap.insert(m.start(), getWriting(seq))
        #if seq in word:
#
 #           charmap.insert(word.index(seq), getWriting(seq))
  #          word = word.replace(seq, '_')
            #word = word[word.index(seq)].replace(seq, getWriting(seq))

    print(word)
    print(charmap)
    return "<h2>" + ' '.join(charmap) + "</h2>"


def getLetter(letter):
    v = pronunciation_list.get(letter)
    #print(v)
    return v.strip()
    #substitution = unicode(v, "hex", "replace")
    #for key, value in ret:
    #    value = value.split(" ")
    #    for v in value:
    #substitution = substitution + unicode(v, "hex", "replace")

    #return substitution


def getWriting(char):
    ret = ""
    # for char in str(word):
    ret += Writing.getLetter(char)
    #  print(ret)
    return ret

def main():
    loadpronunciationmatrix()
    print("""
    Menu:
    (G)et hex values




    """)
    choice = input("choice:")
    if choice.upper() == "G":
        getklingon(None)


if __name__ == "__main__":
    main()