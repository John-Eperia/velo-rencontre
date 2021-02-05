import flask
import os
from flask import request, jsonify
import requests

PORT = os.getenv('PORT')

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    return "<h1>Distant Reading Archive</h1><p>coucou loulou </p>" 

# A route to return all of the available entries in our catalog.
@app.route('/map', methods=['GET'])
def api_all():
    return requests.get('http://map:5000/').content

if __name__ == "__main__":
	app.run(host='0.0.0.0', debug=True, port=PORT)