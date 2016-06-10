__author__ = 'ntallmon'

import nltk

import Dictionary

# See: http://www.nltk.org/book/ch08.html#ex-elephant
# Grammar rules for Kilngon translation
# https://en.wikipedia.org/wiki/Klingon_grammar

grammarList = {'S': ['NP', 'VP'], 'VP': [['V', 'NP'], ['V' 'NP', 'PP']], 'PP': ['P', 'NP'], 'V': [],
               'NP': ['Det', 'N', 'PP'], 'Det': [], 'N': [], 'P': []}

# This will definitely need to be revised
klingonGrammar = {'S': [['VP', 'NP'], ['NP', 'VP', 'NP']], 'VP': [['NP', 'V'], ['NP', 'PP', 'VP']], 'PP': ['P', 'NP'],
                  'NP': ['Det', 'N', 'PP'], 'V': [],
                  'N': [], 'P': [], 'Det': []}

sentenceOrder = []
nouns = {'NNP', 'NN', 'NNS'}
verbs = {'VBZ', 'VB', 'VBP'}
questionWords = {'WP'}
adjectives = {'RP'}
preposition = {'IN'}
det = {'DT'}
pronouns = {'JJ', 'PRP'}


# create/print a tree based off of the grammar
def print_tree(grammar,sentence):
    tokens =  nltk.word_tokenize(sentence)
    acceptableSentences = ' | '.join(grammar['S'])
    nouns = ' | '.join(grammar['N'])
    verbs = ' | '.join(grammar['V'])


    # todo: format like the groucho grammar
    newGrammar = """
  S -> """ + acceptableSentences + """
  VP -> V NP | V NP PP
  PP -> P NP
  V -> """+verbs+""" | VBZ
  NP -> "John" | "Mary" | "Bob" | Det N | Det N PP | NN
  Det -> "a" | "an" | "the" | "my" | DT
  N -> """+nouns+"""
  P -> "in" | "on" | "by" | "with"
  """

    parser = nltk.ChartParser(newGrammar)
    for tree in parser.parse(tokens):
        print(tree)
    #print(newGrammar)


# This will basically take the words assigned in the input grammar, map them to the target grammar in the right places
def buildNewGrammar():
    global grammarList, klingonGrammar
    klingonGrammar['N'] = grammarList['N']
    klingonGrammar['V'] = grammarList['V']
    klingonGrammar['P'] = grammarList['P']
    klingonGrammar['Det'] = grammarList['Det']


def substituteWords():
    global klingonGrammar
    for noun in klingonGrammar['N']:
        ret = Dictionary.returnKlingon(noun)
        if ret is not None:
            klingonGrammar['N'].append(ret)
            klingonGrammar['N'].remove(noun)
    for verb in klingonGrammar['V']:
        ret = Dictionary.returnKlingon(verb)
        if ret is not None:
            klingonGrammar['V'].append(ret)
            klingonGrammar['V'].remove(verb)
    for prep in klingonGrammar['P']:
        ret = Dictionary.returnKlingon(prep)
        if ret is not None:
            klingonGrammar['P'].append(ret)
            klingonGrammar['P'].remove(prep)
    for DET in klingonGrammar['Det']:
        ret = Dictionary.returnKlingon(DET)
        if ret is not None:
            klingonGrammar['Det'].append(ret)
            klingonGrammar['Det'].remove(DET)

    print("Klingon Grammar:" + str(klingonGrammar))


def wordorder(tokens, sentence):
    # global englishGrammar1
    """

    :param tokens: - Tuple
    :param sentence:
    """
    global nouns, grammarList, klingonGrammar
    print(tokens)
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

    # rd_parser = nltk.RecursiveDescentParser(englishGrammar1)
    # sentence = sentence.split()
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
    # print(grammarList)
    buildNewGrammar()
    substituteWords()
    print_tree(grammarList, sentence)
