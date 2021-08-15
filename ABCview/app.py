from flask import (
	Flask, app, flash, g, request, json, jsonify
)
from flask_cors import CORS # 前后端分离跨域
import pandas as pd
import numpy as np
import os
FILENAME1 = './sentence_token_pred_100.json'
FILENAME2 = './tsne_100.json'

app = Flask(__name__)
CORS(app)

@app.route('/query_all')
def query_all():
	with open(FILENAME1) as f:
		jsonStr = json.load(f)
		return jsonify(jsonStr)

@app.route('/query_tsne')
def query_tsne():
	with open(FILENAME2) as f:
		jsonStr = json.load(f)
		return jsonify(jsonStr)
if __name__ == "__main__":
	app.run(debug=True)
