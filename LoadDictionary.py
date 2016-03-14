import FileHandler

__author__ = 'thorofasgaard'

dictionary = {}
translation = {}
mode = ""


def loadDictionary(language):
    global mode
    mode = language
    file = FileHandler.loadFile("Resources/" + language + ".csv", "r")
    for line in file:
        vals = line.split(',')
        # check to make sure their not blank
        if vals[0] == '':
            continue
        value = ""

        for i in range(1, len(vals)):
            if vals[i].strip() != '':
                value += vals[i].strip() + ","
        dictionary.update({vals[0].strip(): value.strip()})

        translation.update({value.strip(): vals[0].strip()})

    print("**************** Dictionary Loaded ****************")
    return dictionary


def lookup():
    ret = None
    word = input('Enter your query, type "Q" to quit:')
    if word.upper() == 'Q':
        return
    else:
        # keys = dictionary.keys()
        for item in dictionary.items():

            if word.upper() in str(item).upper():
                if ret is None:
                    ret = ""
                ret = ret + str(item)
                # elif word.upper() in item[1].upper():
            #                ret = item[1].upper()
        if ret is None:
            print('Unable to find "' + word + '" anywhere')
        else:
            print(word + ': ' + str(ret))
        lookup()
