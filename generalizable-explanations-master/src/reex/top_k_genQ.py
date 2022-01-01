import json
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from matplotlib import rc, font_manager
from collections import defaultdict
import gzip
import logging
import os

def read_generic_gaf(gaf_file):
    symmap = defaultdict(set)
    with gzip.open(gaf_file,"rt") as gf:
        for line in gf:
            line = line.strip().split("\t")
            if "UniProt" in line[0] and len(line) > 5:
                symmap[line[2]].add(line[4])
    logging.info("Found {} mappings.".format(len(symmap)))
    return symmap

def IC_of_a_term(term, mapping, mc, normalization):
    IC = 0
    if term in mc:
        p = mc[term] / normalization
        IC += (-np.log(p))
    else:
        ## 1000 as in impossibly high IC
        IC = 1000

    return IC

def visualize_top_k_terms(k_number, json_path, mapping):
    """
    Uses json output of ReEx to visualize top **k terms according to genQ
    """
    font_size = 6
    font_properties = {'family': 'serif', 'serif': ['Computer Modern Roman'],
                       'weight': 'normal', 'size': font_size}

    font_manager.FontProperties(family='Computer Modern Roman', style='normal',
                                size=font_size, weight='normal', stretch='normal')
    rc('text', usetex=True)
    rc('font', **font_properties)
    sns.set_style("white")

    ## go through mapping
    mc = {}
    all_terms = set()
    mappings = read_generic_gaf(mapping)
    for k, v in mappings.items():
        for el in v:
            all_terms.add(el)
            if el in mc:
                mc[el] += 1
            else:
                mc[el] = 1
    normalization = len(all_terms)


    genQ_dict = {}
    try:
        path = json_path
        json_file = open(path)
        data = json.load(json_file)
        json_data = json.loads(data)

        for keyClass in json_data["resulting_generalization"]:
            if keyClass != "average_depth" and keyClass != "average_association":
                for term in json_data["resulting_generalization"][keyClass]["terms"]:
                    IC = IC_of_a_term(term, mappings, mc, normalization)
                    genQ = 1 - IC/9.82
                    genQ_dict[term] = genQ
    except Exception as e:
        print(e)
        pass

    ## find top k genQ terms
    top_k_genQ = []
    top_k_term = []

    for termKey in genQ_dict:
        if len(top_k_genQ) < k_number:
            top_k_term.append(termKey)
            top_k_genQ.append(genQ_dict[termKey])
        else:
            # find and replace min
            min = 0
            minI = 0
            for c in range(len(top_k_genQ)):
                if top_k_genQ[c] < min:
                    min = top_k_genQ[c]
                    minI = c
            if top_k_genQ[minI] < genQ_dict[termKey]:
                top_k_genQ[minI] = genQ_dict[termKey]
                top_k_term[minI] = termKey


     ## we now have top k genQ terms in list

    # plot
    dfx = pd.DataFrame(zip(top_k_term, top_k_genQ))
    print(dfx)
    dfx.columns = ['Term', 'genQ']
    dfx = dfx.sort_values(by=['genQ'])
    # Custom x axis
    sns.barplot(dfx['Term'], dfx['genQ'], errwidth=1.2, palette="coolwarm", capsize=.11)
    plt.tight_layout()
    plt.show()
    plt.clf()

visualize_top_k_terms(10, '../../results/json/2297646704323106148.json', '../../mapping/goa_human.gaf.gz')