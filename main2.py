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
    data_in = cs.load_data('face-to-face/sequentialID/InVS13.dat')
    data = data_in
    nodes = cs.individuals(data)
    n_nodes = len(nodes)

    graphs, pos = cs.build_graphs(data,1000000)
    print("# di grafi",len(graphs))
    print("# di nodi ",n_nodes)
    print("# di archi",len(graphs[0].edges()))
    
    g = graphs[0]
    now = time.time()
    res = mt.getAllSubgraphs(g,5)
    print("time per tirare fuori i grafi",time.time() - now)

    unique_data = [list(x) for x in set(tuple(x) for x in res)]

    times = []
    for i in [10,100,500,1000,2000,3000,5000,10000,20000]:
        now = time.time()
        tmp_data = unique_data[0:i]
        auto = mt.automorphism_groups2(g,tmp_data)
        time_elapsed = time.time() - now
        times.append(time_elapsed)
        print("gruppi",len(auto))
        print(times)



if __name__ == "__main__":
    main(sys.argv[1:])