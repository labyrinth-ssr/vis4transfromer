import data_process
from functools import reduce
import re
import json
from flask_cors import CORS
from flask import Flask, jsonify
BOOKS = [
    {
        'title': 'On the Road',
        'author': 'Jack Kerouac',
        'read': True
    },
    {
        'title': 'Harry Potter and the Philosopher\'s Stone',
        'author': 'J. K. Rowling',
        'read': False
    },
    {
        'title': 'Green Eggs and Ham',
        'author': 'Dr. Seuss',
        'read': True
    }
]
# jsonify : 直接将python中的字符（dump）转入到json，to do:从本地读取json，放到服务器上


with open("./data/attn_head.json", 'r') as load_f1:
    load_dict = json.load(load_f1)

with open("./data/edges_list.json", 'r') as load_f2:
    py_data = json.load(load_f2)

# data_process.process()

# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})


# sanity check route
@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')


@app.route('/data', methods=['GET'])
def all_data():
    return jsonify({
        'data': load_dict
    })


@app.route('/books', methods=['GET'])
def all_books():
    return jsonify({
        'books': BOOKS
    })


@app.route('/attr-tree', methods=['GET'])
def attr_tree_data():
    nodes_list = []
    links_list = []
    def run_function(x, y): return x if y in x else x + [y]

    for ele in py_data:
        tar_index = re.findall(r'\d+', ele[0])[0]
        tar_text = re.sub(r'[^A-Za-z]', '', ele[0])
        soc_index = re.findall(r'\d+', ele[1])[0]
        soc_text = re.sub(r'[^A-Za-z]', '', ele[1])

        link_dict = {'source':
                     soc_index, 'target': tar_index, 'value': 2}
        links_list.append(link_dict)

        node_dict1 = {'node': tar_index, 'name': tar_text}
        nodes_list.append(node_dict1)
        node_dict2 = {'node': soc_index, 'name': soc_text}
        nodes_list.append(node_dict2)
    data = reduce(run_function, [[], ] + nodes_list)
    node_link_data = {'nodes': data, 'links': links_list}
    # node_link_dict = {'node_link'}

    # with open ('node_link.json','w') as to_json:
    #     json.dump(node_link_data,to_json)

    return jsonify({
        'node_link': node_link_data
    })


@app.route('/test', methods=['GET'])
def test_data():
    return jsonify({
        "nodes": [
            {"node": '0', "name": "node0"},
            {"node": '1', "name": "node1"},
            {"node": '2', "name": "node2"},
            {"node": '3', "name": "node3"},
            {"node": '4', "name": "node4"}
        ],
        "links": [
            {"source": '0', "target": '2', "value": 5},
            {"source": '1', "target": '2', "value": 5},
            {"source": '1', "target": '3', "value": 5},
            {"source": '0', "target": '4', "value": 5},
            {"source": '2', "target": '3', "value": 5},
            {"source": '2', "target": '4', "value": 5},
            {"source": '3', "target": '4', "value": 5}
        ]})


if __name__ == '__main__':
    app.run()
