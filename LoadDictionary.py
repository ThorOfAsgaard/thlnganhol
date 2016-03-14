import FileHandler
__author__ = 'thorofasgaard'


dictionary = {}
translation = {}
mode = ""
def loadDictionary(language):
    global mode
    mode = language
    file = FileHandler.loadFile("Resources/"+language+".csv", "r")
    for line in file:
        vals = line.split(',')
        # check to make sure their not blank
        if vals[0] == '':
            continue
        dictionary.update({vals[0].strip(): vals[1].strip()})

        translation.update({vals[1].strip(): vals[0].strip()})

    return dictionary


def lookup():
    word = input('Enter your query, type "Q" to quit:')
    if word.upper() == 'Q':
        return
    else:
        ret = dictionary.get(word)
        if ret == None:
            ret = translation.get(word)
            if ret == None:
                print('Unable to find '+ word + ' anywhere')
            else:
                print(word+ ': ' + ret)
        else:
            print(word + ': ' + ret)
        lookup()




