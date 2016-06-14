__author__ = 'ntallmon'

import nltk

import Dictionary

# See: http://www.nltk.org/book/ch08.html#ex-elephant
# Grammar rules for Klingon translation
# https://en.wikipedia.org/wiki/Klingon_grammar


possibleGrammar = """
  S  -> NP VP
  NP -> Det Nom | PropN
  Nom -> Adj Nom | N
  VP -> V Adj | V NP | V S | V NP PP
  PP -> P NP
  PropN -> 'Buster' | 'Chatterer' | 'Joe'
  Det -> 'the' | 'a'
  N -> 'bear' | 'squirrel' | 'tree' | 'fish' | 'log'
  Adj  -> 'angry' | 'frightened' |  'little' | 'tall'
  V ->  'chased'  | 'saw' | 'said' | 'thought' | 'was' | 'put'
  P -> 'on'
  """
grammarList = {'S': ['NP VP'], 'VP': [['V', 'NP'], ['V' 'NP', 'PP']], 'PP': ['P', 'NP'], 'V': [],
               'NP': ['Det', 'N', 'PP'], 'Det': [], 'N': [], 'P': [], 'Adj': []}

# This will definitely need to be revised
klingonGrammar = {'S': [['VP NP'], ['NP VP NP']], 'VP': [['NP', 'V'], ['NP', 'PP', 'VP']], 'PP': ['P', 'NP'],
                  'NP': ['Det', 'N', 'PP'], 'V': [],
                  'N': [], 'P': [], 'Det': [], 'Adj': []}

sentenceOrder = []
nouns = {'NNP', 'NN', 'NNS'}
verbs = {'VBZ', 'VB', 'VBP', 'VBG'}
questionWords = {'WP'}
adjectives = {'RP', 'RB', 'JJ'}
preposition = {'IN'}
det = {'DT'}
pronouns = {'PRP', 'PRP$'}


# create/print a tree based off of the grammar
def print_tree(grammar, sentence):
    """

    :param grammar: which grammar structure to base the replacements off of
    :param sentence: string that will be tokenized to parse
    """
    print("----Printing Tree for:" + sentence + "----")
    tokens = nltk.word_tokenize(sentence)
    acceptableSentences = ' | '.join(grammar['S'])
    nouns = ' | '.join(grammar['N'])
    verbs = ' | '.join(grammar['V'])
    dets = ' | '.join(grammar['Det'])
    preps = ' | '.join(grammar['P'])
    adj = ' | '.join(grammar['Adj'])

    # todo: format like the groucho grammar
    newGrammar = """
  S -> """ + acceptableSentences + """
  VP -> V NP | V NP PP
  PP -> P NP
  V -> """ + verbs + """
  NP -> Det N | Det N PP
  Det -> """ + dets + """
  N -> """ + nouns + """
  P -> """ + preps + """
  Adj -> """ + adj + """
  """
    print(newGrammar)
    gram = nltk.CFG.fromstring(newGrammar)
    parser = nltk.ChartParser(gram)
    for tree in parser.parse(tokens):
        print(tree)
        print(newGrammar)


# This will basically take the words assigned in the input grammar, map them to the target grammar in the right places
def buildNewGrammar():
    global grammarList, klingonGrammar
    print("---------Building new Grammar---------")
    klingonGrammar['N'] = grammarList['N']
    klingonGrammar['V'] = grammarList['V']
    klingonGrammar['P'] = grammarList['P']
    klingonGrammar['Det'] = grammarList['Det']
    klingonGrammar['Adj'] = grammarList['Adj']


def substituteWords():
    global klingonGrammar
    print("---------Substituting Words---------")
    for noun in klingonGrammar['N']:
        print(noun)
        ret = Dictionary.returnKlingon(noun)
        if ret is not None:
            klingonGrammar['N'].append("\"" + ret + "\"")
            klingonGrammar['N'].remove(noun)
    for verb in klingonGrammar['V']:
        ret = Dictionary.returnKlingon(verb)
        if ret is not None:
            klingonGrammar['V'].append("\"" + ret + "\"")
            klingonGrammar['V'].remove(verb)
    for prep in klingonGrammar['P']:
        ret = Dictionary.returnKlingon(prep)
        if ret is not None:
            klingonGrammar['P'].append("\"" + ret + "\"")
            klingonGrammar['P'].remove(prep)
    for DET in klingonGrammar['Det']:
        ret = Dictionary.returnKlingon(DET)
        if ret is not None:
            klingonGrammar['Det'].append("\"" + ret + "\"")
            klingonGrammar['Det'].remove(DET)
    for ADJ in klingonGrammar['Adj']:
        ret = Dictionary.returnKlingon(ADJ)
        if ret is not None:
            klingonGrammar['Adj'].append("\"" + ret + "\"")
            klingonGrammar['Adj'].remove(ADJ)

    print("Klingon Grammar:" + str(klingonGrammar))


def wordorder(tokens, sentence):
    # global englishGrammar1
    """

    :param tokens: - Tuple
    :param sentence:
    """
    global nouns, grammarList, klingonGrammar
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
        if any(x[1] in a for a in adjectives):
            grammarList['Adj'].append(x[0])

#    print(grammarList)
    buildNewGrammar()
    substituteWords()
  #  print_tree(grammarList, sentence)
