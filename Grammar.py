__author__ = 'ntallmon'

import nltk
# Grammar rules for Kilngon translation
# https://en.wikipedia.org/wiki/Klingon_grammar

grammarList = {}
grammarList['S'] = '-> NP VP'
grammarList['VP'] = '-> V NP | V NP PP'
grammarList['V'] = []  # based off of the tokens, we 'add' to this
grammarList['NP'] = []
grammarList['Det'] = []
grammarList['N'] = []

sentenceOrder = []
nouns = {'NNP', 'NN'}
verbs = {'VBZ'}
det = {'DT'}
pronouns = {'PRP'}

def buildNewGrammar(grammar):
    print("TODO:  foo")
def wordorder(tokens, sentence):
    # global englishGrammar1
    global nouns, grammarList
    englishGrammar1 = nltk.CFG.fromstring("""
  S -> NP VP
  VP -> V NP | V NP PP
  PP -> P NP
  V -> "saw" | "ate" | "walked" | is | VBZ
  NP -> "John" | "Mary" | "Bob" | Det N | Det N PP | NN
  Det -> "a" | "an" | "the" | "my" | DT
  N -> "man" | "dog" | "cat" | "telescope" | "park"
  P -> "in" | "on" | "by" | "with"
  """)

    rd_parser = nltk.RecursiveDescentParser(englishGrammar1)
    sentence = sentence.split()
    for x in tokens:
        if any(x[1] in n for n in nouns):
            grammarList['N'].append(x[0])
        if any(x[1] in v for v in verbs):
            grammarList['V'].append(x[0])
        if any(x[1] in d for d in det):
            grammarList['Det'].append(x[0])
        if any(x[1] in p for p in pronouns):
            grammarList['N'].append(x[0])

    # for tree in rd_parser.parse(sentence):
    #    print(tree)
    print(grammarList)
