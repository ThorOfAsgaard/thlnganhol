__author__ = 'thorofasgaard'

# Creates the glyph representation of the klingon writing system
# Will need to create individual pngs for each letter

def getLetter(letter):
    if letter == "Q":
        letter = "Qupper"
    return "./static/image/alphabet/"+letter+".png"