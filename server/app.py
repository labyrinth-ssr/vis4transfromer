from flask.json import load
from attn_process import attnProcess
from head_importance import process_impo
from functools import reduce
import re
import json
from flask_cors import CORS
from flask import Flask, jsonify

# jsonify : 直接将python中的字符（dump）转入到json，to do:从本地读取json，放到服务器上


# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

# sanity check route

@app.route('/data', methods=['GET'])
def all_data():
    with open("./data/attn_head.json", 'r') as load_f:
        load_dict = json.load(load_f)
    return jsonify({# 需要一个python对象
        'data': load_dict
    })

@app.route('/attn-head',methods=['GET'])

def attn_data_process():
    with open('./data_generation/output/att_score_zero_base_exp5.json','r') as load_f1:
        py_data1=json.load(load_f1)
    with open('./data_generation/output/head_importance_attr.json','r') as load_f2:
        py_data2=json.load(load_f2)
    with open('./data/tokens.json','r') as load_f3:
        py_data3=json.load(load_f3)
    print(process_impo(py_data2))
    
    return jsonify({
        'importance':process_impo(py_data2),
        'detail': attnProcess(py_data1),
        'tokens': py_data3
    })



@app.route('/attr-tree', methods=['GET'])
def attr_tree_data():
    with open("./data/edges_list.json", 'r') as load_f:
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

    for inx, val in enumerate(py_data2):
        nodes_list.append({'node':str(inx),'name':val})

    data = reduce(run_function, [[], ] + nodes_list)
    node_link_data = {'nodes': data, 'links': links_list}

    return jsonify({
        'node_link': node_link_data,
        'tokens': py_data2
    })

if __name__ == '__main__':
    app.run()
