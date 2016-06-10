__author__ = 'ntallmon'

import nltk

def get_parts_of_speech(String):
    if String is None:
        return
    tokens = nltk.word_tokenize(String)
    tagged = nltk.pos_tag(tokens)
    if tagged is not None:
        try:
            print(tagged)
        except:
            pass
        return tagged