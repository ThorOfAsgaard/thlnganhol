__author__ = 'thor'
from flask import Flask, request, render_template

import CommonPhrases
import Dictionary
import Pronunciation

# import KlingonTranslator

app = Flask(__name__)
app.debug = True


@app.route("/")
def index():
    return render_template("index_new.html")


@app.route('/common-phrases', methods=['POST', 'GET'])
def commonphrases():
    CommonPhrases.loadPhrases()
    ret = CommonPhrases.list_phrases_web()
    html = ""
    for phrase in ret:
        html += "<div class='well well-sm'>"
        html += str(phrase)
        html += "</div>"
    return html


@app.route('/pronunciation', methods=['POST', 'GET'])
def getPronunciation():
    ret = str(request.args['klingon'])
    Pronunciation.loadpronunciationpatrix()
    word = Pronunciation.getIPA(ret)
    return word


@app.route('/search', methods=['POST', 'GET'])
def search():
    ret = str(request.args['query'])
    Dictionary.loadDictionary('dictionary')
    # retString = LoadDictionary.lookup(ret)
    ret = Dictionary.lookup(ret)
    retHtml = ""
    for item in ret:
        retHtml += "<div class='well well-sm'>"
        retHtml += str(item)
        retHtml += "</div>"

    return retHtml


@app.route('/synonyms', methods=['POST', 'GET'])
def synonyms():
    ret = str(request.args['query'])
    html = ""
    synonyms = Dictionary.find_synonyms(ret)
    for syn in synonyms:
        html = html + "<li class='list-group-item'>" + str(syn) + "</li>"

    return html


if __name__ == "__main__":
    app.run()
