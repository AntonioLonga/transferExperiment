import networkx as nx
import numpy as np



def getAllSubgraphs(g,k):
    Vext = set()
    res = []
    for v in list(g.nodes()):
        neig = set(list(g.neighbors(v)))
        Vext = Vext.union(neig)
        Vext = neig.difference(set(np.arange(1,v)))
        extendSubGraph({v},Vext,v,k,res,g)
    return(res)


def extendSubGraph(Vsb,Vex,v,k,res,g):
    if (len(Vsb) == k):
        #print("res \t",Vsb)
        res.append(list(Vsb))
        return(Vsb)
    else:
        #print(len(Vex))
        while not(len(Vex) == 0):
            w = Vex.pop()
            nexcl = list(Nexcl(g,w,Vsb))
            nexcl = [x for x in nexcl if x > v]
            nexcl = set(nexcl)
            extendSubGraph(Vsb.union({w}),Vex.union(nexcl),v,k,res,g)
            
#Nexcl
def Nexcl(g,v,V1):
    V1_set = set(V1)
    neig_V1 = subgraph_neighbors(g,V1)
    neig = set(list(g.neighbors(v)))
    neig_V_V= V1_set.union(neig_V1)
    Nexcl = list(neig.difference(neig_V_V))
    Nexcl = [x for x in Nexcl if x > v]
    Nexcl = np.sort(Nexcl)
    return(set(Nexcl))


def subgraph_neighbors(g,nodes):
    neig = set()
    for i in nodes:
        list_neigh = list(g.neighbors(i))
        for j in list_neigh:
            neig.add(j)
        neig = neig.difference(set(nodes))

    neig = set(np.sort(list(neig)))
    return(neig)



def automorphism_groups(g,graphs):
    unique_graphs = [[graphs[0]]]
    for i in range(1,len(graphs)):
        add = True
        for j in range(len(unique_graphs)):
            uniq_g = unique_graphs[j][0]
            g1 = nx.subgraph(g,graphs[i])
            g2 = nx.subgraph(g,uniq_g)
            if (nx.is_isomorphic(g1,g2)):
                add = False
                unique_graphs[j].append(graphs[i])
        if (add):
            unique_graphs.append([graphs[i]])
            
    return(unique_graphs)