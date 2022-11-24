from flask import Flask
from flask import request
from flask import json
import requests


app = Flask(__name__)

def return_description(sessionid):
  data = """{"session":{"id":"%s","params":{}},"prompt":{"override":false,"firstSimple":{"speech":"Hello World.","text":"Hello World"}},"scene":{"name":"SceneName","slots":{},"next":{"name":"actions.scene.END_CONVERSATION"}}}"""  % sessionid
  response = app.response_class(
        response=json.dumps(data ),
        status=200,
        mimetype='application/json'
    )
  return data 

@app.route('/')  
def hello_world():
    return "It works!"

@app.route('/webhook', methods=['POST','GET'])
def webhook():

  if "handler" in request.json: #This is a sample.
   msg = return_description(request.json['session']['id'])
   return msg

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8000)
              
