# coding=utf-8
# author: veficos
# time: 2016-03-08

from flask import Flask,render_template


flask = Flask(__name__)




@flask.route('/')
def index():
    return render_template('index.html')

flask.run()
