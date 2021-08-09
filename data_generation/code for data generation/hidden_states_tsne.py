# from sklearn.manifold import TSNE
import json
import numpy as np
from sklearn.manifold import TSNE
from typing import List

with open('output/encoded_layers_1.json') as f:
    hidden_states = json.load(f)
hidden_states = np.array(hidden_states).reshape(12, 128, 768)
with open('output/tokens_and_pred_1.json') as f:
    tokens_and_pred = json.load(f)
tokens = tokens_and_pred[0]['tokens']


def token_2d_vector(x: float, y: float, token_index: int):
    x = x.item()
    y = y.item()
    token_vectors[token_index]['tsne'].append([x, y])


def reduce(data: List, method: str, dims: int) -> List:
    """Apply reduction method on current vector list."""
    if method == "tsne":
        reduction = TSNE(n_components=dims)
    else:
        raise KeyError

    reduced = reduction.fit_transform(data)
    return reduced.transpose()


token_vectors = []
for token in tokens:
    flag = 1
    if token == "[SEP]":
        flag = 2
    label = "sentence 1" if flag == 1 else "sentence 2"
    if token == "[CLS]":
        label = None
    token_vector = {'token': token, 'label': label, 'tsne': []}
    token_vectors.append(token_vector)

for layer_index, layer in enumerate(hidden_states):
    token2vectors: List = layer[:len(tokens)]
    layer_reduced: List = reduce(data=token2vectors,
                                 method="tsne",
                                 dims=2)
    for token_index, value in enumerate(layer_reduced[0]):
        token_2d_vector(x=value,
                        y=layer_reduced[1][token_index],
                        token_index=token_index)

with open('output/tsne_1.json', "w") as fout:
    fout.write(json.dumps(token_vectors, indent=2) + "\n")
