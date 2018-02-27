from flask import Flask, session, redirect, url_for, escape, request, render_template
from flask_cors import CORS, cross_origin
import requests
import json
import os
import codebuilder

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return '<h1>welcome</h1>'

#simple post request to get json data from frontent h
@app.route('/post', methods = ['POST'])
def get_post_javascript_data():
    
    #get data from the request
	
    #jsdata = request.form['javascript_data']

    #load the json
    jsonData = request.get_json(silent=True)

    #generate code
    with open(codebuilder.generate_code(jsonData), 'r') as myfile:
        code = myfile.read()
    
        #add code to new json file
        jsonData['code'] = str(code)

    newJsonData = json.dumps(jsonData)
    
    resp = requests.post('http://ec2-34-203-220-180.compute-1.amazonaws.com:5002/post',json=newJsonData)

    return  newJsonData

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5001))
    app.run(host='0.0.0.0', port=port)
