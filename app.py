from flask import Flask
from flask import request
from flask import json

import dialogflow

app = Flask(__name__)

@app.route("/dialogflowwebhook", methods=['POST'])
def handler():
	data = request.get_json()

	print(json.dumps(data, indent=4))
	
	df = dialogflow.Parser()
	response = df.parse(data)

	return response