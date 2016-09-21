"""
Vincent Liok
SoftDev1 pd8
HW02 -- Fill Your Flask
2016-09-20
"""

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "HELLO WORLD!"

@app.route("/nextpage")
def wassup():
    return "WASSUP"

@app.route("/nextnextpage")
def rawr():
    return "RAWR!"

if __name__ == "__main__" :
    app.run()
