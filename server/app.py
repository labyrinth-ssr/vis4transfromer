import data_process
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
    return jsonify({
        'data': load_dict
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
