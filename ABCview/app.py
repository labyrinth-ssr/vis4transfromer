from flask import (
    Flask, app, flash, g, request, json, jsonify
)
from flask_cors import CORS  # 前后端分离跨域
# import pandas as pd
# import numpy as np
# import os
from attn_process import attnProcess
from head_importance import process_impo
from functools import reduce
from attribution_tree import attribution_tree
import re



import ndjson

FILENAME1 = './sentence_token_pred_100.json'
FILENAME2 = './tsne_100.json'
threshold={'a':1}


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


@app.route("/query_attn_head/<int:sentence_id>")
def query_attn_head(sentence_id):
    with open('./att_attr_all/att_score_zero_base_exp'+str(sentence_id)+'.ndjson') as load_f:
        py_data = ndjson.load(load_f)
    with open('./data_generation/output/head_importance_attr.json', 'r') as load_f2:
        py_data2 = json.load(load_f2)
    with open('./data/tokens.json', 'r') as load_f3:
        py_data3 = json.load(load_f3)
        return jsonify({
            'importance': process_impo(py_data2),
        'detail': attnProcess(py_data),
        'tokens': py_data3
        })

@app.route('/query_attr_tree/<int:sentence_id>',methods=['GET', 'POST'])# 请求：
def query_attr_tree(sentence_id):
    global threshold
    node_link_data={}
    py_data2=[]
    if request.method=='POST':
        post_data= request.get_json()
        threshold=post_data
        
        # main(post_data)
    else:
        with open("./attr_tree/edges_list"+str(sentence_id)+".json", 'r') as load_f:
            py_data = json.load(load_f)
        with open("./data/tokens.json", 'r') as load_f2:
            py_data2 = json.load(load_f2)

        nodes_list = []
        links_list = []
        def run_function(x, y): return x if y in x else x + [y]

        for ele in py_data:
            tar_index = re.findall(r'\d+', ele[0])[0]
            soc_index = re.findall(r'\d+', ele[1])[0]
            link_dict = {'source':
                        soc_index, 'target': tar_index, 'value': 2}
            links_list.append(link_dict)

        for inx, val in enumerate(py_data2):# remember to delete static data
            nodes_list.append({'node': str(inx), 'name': val})

        data = reduce(run_function, [[], ] + nodes_list)
        node_link_data = {'nodes': data, 'links': links_list}

    return jsonify({
        'threshold':threshold,
            'node_link': node_link_data,
            'tokens': py_data2
        })

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')
