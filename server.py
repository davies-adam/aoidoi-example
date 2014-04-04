# -*- coding: utf-8 -*-


import os
import flask
import json

app = flask.Flask(__name__)

@app.route('/works/<author>/<name>')
def main(author, name):
  path = "./works/" + author + "/" + name +".json"
  with open(path) as file:
    info = file.read()
    return flask.render_template("main.html", data=json.loads(info))
  
