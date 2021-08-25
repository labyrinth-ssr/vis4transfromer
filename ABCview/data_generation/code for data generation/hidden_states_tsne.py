# from sklearn.manifold import TSNE
import json
import numpy as np
from sklearn.manifold import TSNE
from typing import List

with open('output/encoded_layers_100.json') as f:
    hidden_states = json.load(f)
hidden_states = np.array(hidden_states).reshape(100, 12, 128, 768)
with open('output/tokens_and_pred_100.json') as f:
    tokens_and_pred = json.load(f)
tokens = []
for i in range(100):
    tokens.append(tokens_and_pred[i]['tokens'])


def token_2d_vector1(x: float, y: float, label: str, token_index: int, layer_index: int, sentence_index: int):
    x = x.item()
    y = y.item()
    token_vector1 = {'tokens': tokens[sentence_index][token_index], 'label': label, 'tsne': [x, y], 'layer': layer_index}
    token_vectors1.append(token_vector1)


def reduce(data: List, method: str, dims: int) -> List:
    """Apply reduction method on current vector list."""
    if method == "tsne":
        reduction = TSNE(n_components=dims)
    else:
        raise KeyError

    reduced = reduction.fit_transform(data)
    return reduced.transpose()


token_vectors_all = []
for i in range(100):
    token_vectors = []
    token_vectors1 = []
    for token in tokens[i]:
        label = "sentence2" if tokens[i].index(token) > tokens[i].index("[SEP]") else "sentence1"
        if token == "[CLS]":
            label = None
        token_vector = {'token': token, 'label': label, 'tsne': []}
        token_vectors.append(token_vector)

    for layer_index, layer in enumerate(hidden_states[i]):
        token2vectors: List = layer[:len(tokens[i])]
        layer_reduced: List = reduce(data=token2vectors,
                                     method="tsne",
                                     dims=2)
        for token_index, value in enumerate(layer_reduced[0]):
            token_2d_vector1(x=value,
                             y=layer_reduced[1][token_index],
                             label=token_vectors[token_index]['label'],
                             token_index=token_index,
                             layer_index=layer_index,
                             sentence_index=i)
    token_vectors_all.append(token_vectors1)

with open('output/tsne_100.json', "w") as fout:
    fout.write(json.dumps(token_vectors_all, indent=2) + "\n")
