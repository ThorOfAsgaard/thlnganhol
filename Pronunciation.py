from setuptools.compat import unicode

__author__ = 'thorofasgaard'

import FileHandler
import re
import sys
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
    #print(pronunciation_list)

def getIPA(word):
    ret = ""
    #tlh, ng
    p = re.compile('[a-z][A-Z]+')
    word = word.strip()
    if word.find('tlh') > 0:
        word =word.replace('tlh', unicode(pronunciation_list.get('tlh'), "utf-8", 'replace'))
    if word.find('ng') > 0:
        word = word.replace('ng', unicode(pronunciation_list.get('ng'), "utf-8", 'replace'))
    if word.find('ch') > 0:
        word = word.replace('ch', unicode(pronunciation_list.get('ch'), 'utf-8', 'replace'))
    for char in str(word):
      newchar = pronunciation_list.get(char)
      #word = word.replace(char, unicode(pronunciation_list.get(char), 'utf-8', 'replace'))
    return word

def getWriting(word):
    ret = ""
    for char in str(word):
        ret +="<image src='"+Writing.getLetter(char)+"' width='20' height='20' />"

    return ret


