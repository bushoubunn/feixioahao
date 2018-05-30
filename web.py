#coding:utf-8
from flask import Flask,render_template,request,jsonify
import json 
from crawl import get_cooin_info
app=Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/get_json')
def get_json():
    data=get_cooin_info()
    return data






if __name__=="__main__":

    app.run(debug=True)