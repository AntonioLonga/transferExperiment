import utilities as ut
import construction as cs
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import motifs as mt
import time

import sys, getopt

def main(argv):
   execute()

def execute():

    n_edges = []
    times_get_graphs = []
    times_get_groups = []
    n_graphs = []
    n_group = []

    for i in [0.01,0.02]:
        print("Fatto1")
        p = i
        g = nx.fast_gnp_random_graph(200,p,seed=11)
        n_edges.append(len(g.edges()))
        
        res1 = mt.getAllSubgraphs(g,5)
        unique_data1 = [list(x) for x in set(tuple(x) for x in res1)]
        auto1 = mt.automorphism_groups(g,unique_data1)
        
        n_graphs.append(len(res1))
        n_group.append(len(auto1))

        print("archi",n_edges)
        print("number of graphs",n_graphs)
        print("automorphism group",n_group)

if __name__ == "__main__":
   main(sys.argv[1:])