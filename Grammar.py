import copy

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

pairs = {}
# create/print a tree based off of the grammar
def print_tree(grammar, sentence):
    """

    :param grammar: which grammar structure to base the replacements off of
    :param sentence: string that will be tokenized to parse
    """
    print("----Printing Tree for:" + sentence + "----")
    tokens = nltk.word_tokenize(sentence)
    #for token in tokens:
    #    tokens[tokens.index(token)] = pairs.get(token)
 #   print(grammarList)
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
    ##FIXME: doesn't print a new chart, probably need to go off of english
    for tree in parser.parse(tokens):
        print(tree)
        print(newGrammar)


# This will basically take the words assigned in the input grammar, map them to the target grammar in the right places
def buildNewGrammar():
    global grammarList, klingonGrammar
    print("---------Building new Grammar---------")
    gList = copy.deepcopy(grammarList)
    klingonGrammar['N'] = gList['N']
    klingonGrammar['V'] = gList['V']
    klingonGrammar['P'] = gList['P']
    klingonGrammar['Det'] = gList['Det']
    klingonGrammar['Adj'] = gList['Adj']


def substituteWords(sentence):
    global klingonGrammar, pairs, grammarList
    kGrammar = klingonGrammar
    gList = grammarList
    print("---------Substituting Words---------")
    for noun in kGrammar['N']:
        print("Looking up:" + noun)
        ret = Dictionary.returnKlingon(noun)
        if ret is not None:
            #sentence = sentence.replace(noun, ret)
            kGrammar['N'][kGrammar['N'].index(noun)] = "\"" + ret + "\""

            pairs.update({noun: ret})
            #kGrammar['N'].remove(noun)
        else:
            print("Couldn't find:" + noun)
    for verb in klingonGrammar['V']:

        ret = Dictionary.returnKlingon(verb)
        if ret is not None:
            #sentence = sentence.replace(verb, ret)
            kGrammar['V'][kGrammar['V'].index(verb)] = "\"" + ret + "\""
            pairs.update({verb: ret})

    for prep in kGrammar['P']:
        ret = Dictionary.returnKlingon(prep)
        if ret is not None:
            #sentence = sentence.replace(prep, ret)
            kGrammar['P'][kGrammar['P'].index(prep)] = "\"" + ret + "\""
            pairs.update({prep: ret})
    for DET in klingonGrammar['Det']:
        ret = Dictionary.returnKlingon(DET)
        if ret is not None:
            #sentence = sentence.replace(DET, ret)
            kGrammar['Det'][kGrammar['Det'].index(DET)] = "\"" + ret + "\""
            pairs.update({DET: ret})
    for ADJ in kGrammar['Adj']:
        ret = Dictionary.returnKlingon(ADJ)
        if ret is not None:
            #sentence = sentence.replace(ADJ, ret)
            kGrammar['Adj'][kGrammar['Adj'].index(ADJ)] = "\"" + ret + "\""
            pairs.update({ADJ: ret})

    print("Klingon Grammar:" + str(klingonGrammar))
    print("Glossed Sentence:" + sentence)
    sent = sentence.split(" ")
    for s in sent:
        print(s)
        sent[sent.index(s)] = pairs.get(s.strip())
    print(sent)
    print(' '.join(sent))
    return ' '.join(sent)


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
    newSentence = copy.deepcopy(sentence)
    print_tree(grammarList, newSentence)
    sentence = substituteWords(sentence)
    print_tree(grammarList, sentence)
