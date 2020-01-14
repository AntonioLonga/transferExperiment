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
   inputfile = ''
   outputfile = ''
   try:
      opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
   except getopt.GetoptError:
      print ('test.py -i <inputfile> -o <outputfile>')
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print ('test.py -i <inputfile> -o <outputfile>')
         sys.exit()
      elif opt in ("-i", "--ifile"):
         inputfile = arg
      elif opt in ("-o", "--ofile"):
         outputfile = arg
   print ('Input file is ', inputfile)
   print ('Output file is ', outputfile)

   execute(inputfile,outputfile)

def execute(inputFile,outputFile):

    
    

    n_edges = []
    times = []
    for i in [0.01,0.02,0.03,0.04,0.05,0.06,0.07,0.08]:
        start_time = time.time()
        p = i
        g = nx.fast_gnp_random_graph(242,p)
        n_edges.append(len(g.edges()))
        
        res1 = mt.getAllSubgraphs(g,4)
        unique_data1 = [list(x) for x in set(tuple(x) for x in res1)]
        auto1 = mt.automorphism_groups(g,unique_data1)
        
        times.append(time.time() - start_time)
        print("fine GIRO")
        print(n_edges)
        print(times)


if __name__ == "__main__":
   main(sys.argv[1:])