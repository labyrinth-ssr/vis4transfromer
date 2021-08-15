import json
import re
from functools import reduce

def process(py_data):


    nodes_list=[]
    links_list=[]

    for ele in py_data:
        tar_index=re.findall(r'\d+',ele[0])[0]
        tar_text=re.sub(r'[^A-Za-z]', '', ele[0])
        soc_index=re.findall(r'\d+',ele[1])[0]
        soc_text=re.sub(r'[^A-Za-z]', '', ele[1])

        link_dict = {'source':soc_index , 'target': tar_index ,'value' : 0.5}
        links_list.append(link_dict)

        node_dict1 = {'node': tar_index , 'name': tar_text}
        nodes_list.append(node_dict1)
        node_dict2 = {'node': tar_index , 'name': soc_text}
        nodes_list.append(node_dict2)

    run_function = lambda x,y : x if y in x else x + [y]
    nodes_list = reduce(run_function,[[],] + nodes_list)
    node_link_data = {'nodes':nodes_list,'links':links_list}

    print(node_link_data)




# 对于大列表中每个小列表，第一个元素的数字是link中的target，第二个元素的数字是source。
# 生成一个dict后存入lists_list
# 对于每个小列表中的前两个元素，生成一个含node和name的dict，如果该dict未在node_list中出现，则加入。