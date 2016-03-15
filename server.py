__author__ = 'thor'
from flask import Flask, request, session, url_for, redirect, render_template, abort
#import KlingonTranslator

app = Flask(__name__)

@app.route("/")
def index():

    return render_template("index.html")

@app.route("/search")
def search(str):
    return "Search =" + str

if __name__ == "__main__":
    app.run()

