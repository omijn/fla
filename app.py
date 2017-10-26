from flask import Flask
from flask import request
from flask import json

app = Flask(__name__)

@app.route("/dialogflowwebhook")
def handler():
	print(request.get_json())
	return json.jsonify("{'key':1}")