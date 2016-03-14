__author__ = 'ntallmon'

# reads/writes files


def loadFile(filename, method):
    try:
        file = (open(filename, method))
        return file
    except:
        print("Unable to open " + filename)
        pass

def write(file, string):
        print("Do something useful here")







