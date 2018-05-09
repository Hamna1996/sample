#!/usr/bin/env python
import urllib
import json
import os
import sys

from flask import Flask
from flask import request,jsonify
from flask import make_response
app=Flask(__name__)
@ app.route('/webhook',methods=['GET','POST'])
def webhook():
 print("came")
 resp={"fulfillmentText":"this is a text response","speech":"response from webhook deployed in cloud"}
 return make_response(jsonify(resp))
@app.route('/',methods=['GET','POST'])
def webhook():
 return jsonify({"hello":"iam here"})
if __name__=='__main__':
 app.run()
