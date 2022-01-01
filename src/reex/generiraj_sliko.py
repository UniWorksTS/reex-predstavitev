## parsers and such.
import logging
logging.basicConfig(format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')
logging.getLogger().setLevel(logging.INFO)
import pandas as pd
import time
import gzip
import networkx as nx
import obonet
import timeit
from collections import defaultdict
import sys
import os
import nltk
from nltk.corpus import wordnet as wn
import numpy as np
from matplotlib import pyplot as plt
from tqdm import tqdm
from textblob import Word
#from networkx.drawing.nx_pydot import graphviz_layout
#from networkx.drawing.nx_agraph import write_dot, graphviz_layout


def get_ontology_text_custom(mapping):
    nltk.download('wordnet')
    G = nx.DiGraph()

    for word in mapping.keys():
       node = wn.synset(mapping[word])
       temp_graph = closure_graph_fn(node, lambda s: s.hypernyms())
       G = nx.compose(G, temp_graph)

    print(nx.info(G))
    return G

def get_ontology_text():
    """
    Loads ontology for textual datasets
    """
    nltk.download('wordnet')
    G = nx.DiGraph()

    
    entity = wn.synset('entity.n.01')
    G = closure_graph_fn(entity, lambda s: s.hyponyms())
    print(nx.info(G))

    #print(set([x[0] for x in G.in_edges((wn.synset('meeting.n.01').name()))]))
    return G


onto_grapf = get_ontology_text_custom({"sea.n.01"})
pos = nx.spring_layout(k)
plt.title("Terms for class " + class_name)
nx.draw(k, pos = pos, with_labels=True, node_color = color_map)
plt.show()
plt.clf()