import flask
from flask import Flask
from flask import request, redirect, url_for, jsonify
from flask import make_response
import requests
import json
import dialogflow

app = Flask(__name__)

@app.route('/')
def showKeyboard():
    return '<html><body><h1>this is a test from code</h1></body></html>'

@app.route('/webhook', methods=["GET","POST"])
def showWebhookInfo():
    if request.method == 'POST':
        test1 = request.get_json()
        print "test1 message", test1["message"]
        if  "photo" in test1["message"]:
            print 'This is test1', test1
            return "ok image"
            # print '<html><body><h1>Webhook installed</h1></body></html>'
            # return test1
        else:
            print 'Nothing'
            return 'nothing'
	    # message = request.form['message']
        #     project_id = os.getenv('DIALOGFLOW_PROJECT_ID')
        #     fulfillment_text = detect_intent_texts(project_id, "unique", message, 'en')
        #     response_text = { "message":  fulfillment_text }
        #     return jsonify(response_text)
    return '<html><body><h1>Webhook installed GET method</h1></body></html>'

#def detect_intent_texts(project_id, session_id, text, language_code):
#        session_client = dialogflow.SessionsClient()
#        session = session_client.session_path(project_id, session_id)

#        if text:
#            text_input = dialogflow.types.TextInput(
#                text=text, language_code=language_code)
#            query_input = dialogflow.types.QueryInput(text=text_input)
#            response = session_client.detect_intent(
#                session=session, query_input=query_input)

#            return response.query_result.fulfillment_text


@app.route('/message', methods=['GET', 'POST'])
def showMessage():
   if request.method == 'POST':
       print 'this is Dialogueflow message printed'
       test = request.get_json()
       print(test)
       # num = int(test["queryResult"]["outputContexts"][0]["parameters"]["telegram_chat_id"])
       # print 'test', num
   #     return '<html><body><h1>this is Dialogflow message</h1></body></html>'
   # flash( '<html><body><h1>this is dialog flow message not GET</h1></body></html>'
  # print 'all good'
  # return '<html><body><h1>This is a message for Message request</h1></body></html>'
    #data ='{"name": "brian", "city":"Seattle"}'
   data = json.load(open('/var/www/calapp/public_html/calapp/test1.json'))
   # print 'OK data'
   # console.log(data)
   # response1 = data["fulfillmentText"]
   # response2 = data["fulfillmentMessages"][0]["card"]["buttons"][0]["text"]
   # print response
   # return'<html><body><h1>{response1}</h1></body></html>'
   # print data
   bot_token = 'bot676384079:AAE4ZOkoocrP7hnX1ruYf-8G0flqZ1HKRMA'
   reply_markup = {"keyboard":[ ["one"],["two"], ["three"]]}
   url = "https://api.telegram.org/" + bot_token+ "/sendMessage"+"?chat_id=739151409&text=Select one option&reply_markup="+json.dumps(reply_markup)
    #test = json.dumps(reply_markup)
    #print 'Test', test
    #new_test = json.stringify(test)
    #print 'New test', new_test
   print url
   info = {"chat_id": "739151409", "text":"Select one option", "reply_markup": json.dumps(reply_markup)}
   print "Printing", info
   r = requests.get(url)
   print r.json()
   return make_response(json.dumps(data))

   if __name__ == "__main__":
       app.run(debug=True, port=8000)