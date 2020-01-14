import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def get_weights(G,dictionary = False):
    weights = dict()
    for node in G.nodes():
        weight = 0
        for e in G.edges(node):
            weight = weight + G[e[0]][e[1]]["weight"]
        weights[node] = weight
    if (dictionary == False):
        weights = np.array(list(weights.values()))
    return(weights)




def get_neigh_weights(G,dictionary = False):
    w = get_weights(G,True)
    neig_w = dict()
    for node in G.nodes():
        neig = []
        for e in G.edges(node):
            neig.append(w[e[1]])
        neig_w[node] = np.mean(neig)
        
    if (dictionary == False):
        neig_w = np.array(list(neig_w.values()))
    return(neig_w)




def clustering_coeff(G,dictionary=False):
    clustering = nx.clustering(G)
    if not (dictionary):
        clustering = np.array(list(clustering.values()))
    
    return(clustering)



def betweenness_centrality(G,dictionary=False):
    betweenness_centrality = nx.betweenness_centrality(G)
    if not (dictionary):
        betweenness_centrality = np.array(list(betweenness_centrality.values()))
    
    return(betweenness_centrality)



def closeness_centrality(G,dictionary=False):
    closeness_centrality = nx.closeness_centrality(G)
    if not (dictionary):
        closeness_centrality = np.array(list(closeness_centrality.values()))
    
    return(closeness_centrality)


def degree_centrality(G,dictionary=False):
    degree_centrality = nx.degree_centrality(G)
    if not (dictionary):
        degree_centrality = np.array(list(degree_centrality.values()))
    
    return(degree_centrality)







def spectral_gap(G,binary_adj_matrix=False):
    if (binary_adj_matrix):
        adj = nx.adj_matrix(G).A 
        
        for i in range(len(adj)):    # binarizze adj matrix
            for j in range(len(adj[i])):
                if not(adj[i][j] == 0):
                    adj[i][j] = 1

        G1 = nx.from_numpy_matrix(adj)        
        L = nx.normalized_laplacian_matrix(G1)   
    else:
        L = nx.normalized_laplacian_matrix(G)
    
    e = np.linalg.eigvals(L.A)
    e = (np.sort(e)) + np.abs(np.min(e))
    spectral_gap = e[1]
    
    return(spectral_gap)





def find_a_c_cut(data,min_bin=40,max_bin=150,interval=1):
    binss = np.arange(min_bin,max_bin,interval)
    a = []
    c = []
    cut = []
    for bins in binss:
        aa, cc, cuts= fit_hist(data,bins)
        a.append(float("{0:.2f}".format(aa)))
        c.append(cc)
        cut.append(cuts)
    
    final_a = np.mean(a)
    final_c = np.mean(c)
    final_cut = np.mean(cut)
    
    return(final_a,final_c,int(final_cut))


def fit_hist(X,bins):

    y_data,x_data = np.histogram(X,bins=bins)
    x_data = x_data[0:-1]
    cut = (np.argmax(y_data))*(np.max(X)/bins)

    x_data_cut = []
    y_data_cut = []
    for i in range(len(x_data)):
        if x_data[i] > cut:
            x_data_cut.append(x_data[i])
            y_data_cut.append(y_data[i])

    from scipy.optimize import curve_fit

    def poly(x, a, c):
        return c*x**(-a)
    result = curve_fit(poly, x_data_cut, y_data_cut, method='dogbox')


    return (result[0][0],result[0][1],cut)