__author__ = 'thor'
from flask import Flask, request, session, url_for, redirect, render_template, abort, _app_ctx_stack
import Dictionary
import CommonPhrases
# import KlingonTranslator

app = Flask(__name__)
app.debug = True

@app.route("/")
def index():
    return render_template("index.html")


@app.route('/common-phrases', methods=['POST', 'GET'])
def commonphrases():
    CommonPhrases.loadPhrases()
    ret = CommonPhrases.return_all()
    html = ""
    for phrase in ret:
        html +="<div class='well well-sm'>"
        html += phrase
        html += "</div>"


@app.route('/search', methods=['POST', 'GET'])
def search():

    ret = str(request.args['query'])
    Dictionary.loadDictionary('dictionary')
    #retString = LoadDictionary.lookup(ret)
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
    return Dictionary.find_synonyms(ret)

if __name__ == "__main__":
    app.run()
